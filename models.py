from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


expense_participants = db.Table(
    "expense_participants",
    db.Column("expense_id", db.Integer, db.ForeignKey("expense.id"), primary_key=True),
    db.Column("person_id", db.Integer, db.ForeignKey("person.id"), primary_key=True),
)


class Person(db.Model):
    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return self.username

    def __str__(self):
        return self.username


class Expense(db.Model):
    __tablename__ = "expense"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    paid_by_id = db.Column(db.Integer, db.ForeignKey("person.id"), nullable=False)
    payer = db.relationship("Person", foreign_keys=[paid_by_id])

    participant_list = db.relationship(
        "Person", secondary=expense_participants, backref="expenses"
    )


    @property
    def paid_by(self):
        return self.payer.username

    @property
    def participants(self):
        return [p.username for p in self.participant_list]


class ExpenseManager:
    """Same interface as the old in-memory manager, now backed by the
    Flask-SQLAlchemy database instead of plain Python lists."""

    @property
    def people(self):
        return [p.username for p in Person.query.order_by(Person.username).all()]

    @property
    def expenses(self):
        return Expense.query.order_by(Expense.date).all()

    def add_person(self, name):
        name = name.strip()
        if not name:
            return
        already_exists = Person.query.filter_by(username=name).first() is not None
        if not already_exists:
            db.session.add(Person(username=name))
            db.session.commit()

    def add_expense(self, description, amount, paid_by, participants):
        amount = float(amount)

        payer = Person.query.filter_by(username=paid_by).first()
        if payer is None:
            raise ValueError("Payer must be in people list")

        if not participants:
            raise ValueError("At least one participant is required")

        participant_people = []
        for name in participants:
            person = Person.query.filter_by(username=name).first()
            if person is None:
                raise ValueError(f"Unknown participant: {name}")
            participant_people.append(person)

        expense = Expense(
            description=description,
            amount=amount,
            payer=payer,
            participant_list=participant_people,
        )
        db.session.add(expense)
        db.session.commit()

    def delete_person(self, person_id):
        person = Person.query.get(person_id)
        if person is None:
            raise ValueError("Person not found")

        is_payer = Expense.query.filter_by(paid_by_id=person.id).first() is not None
        is_participant = len(person.expenses) > 0

        if is_payer or is_participant:
            raise ValueError(
                f"Cannot delete {person.username}: still linked to one or more expenses. "
                "Remove those expenses first."
            )

        db.session.delete(person)
        db.session.commit()

    def calculate_balances(self):
        balances = {p: 0.0 for p in self.people}

        for e in self.expenses:
            participants = e.participants
            share = e.amount / len(participants)

            # everyone in the split owes their share
            for p in participants:
                balances[p] -= share

            # payer gets reimbursed full amount
            balances[e.paid_by] += e.amount

        return balances


manager = ExpenseManager()
