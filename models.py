class Expense:
    def __init__(self, description, amount, paid_by, participants):
        self.description = description
        self.amount = float(amount)
        self.paid_by = paid_by
        self.participants = participants


class ExpenseManager:
    def __init__(self):
        self.expenses = []
        self.people = []

    def add_person(self, name):
        name = name.strip()
        if name and name not in self.people:
            self.people.append(name)

    def add_expense(self, description, amount, paid_by, participants):
        amount = float(amount)

        if paid_by not in self.people:
            raise ValueError("Payer must be in people list")

        if not participants:
            raise ValueError("At least one participant is required")

        for p in participants:
            if p not in self.people:
                raise ValueError(f"Unknown participant: {p}")

        self.expenses.append(
            Expense(description, amount, paid_by, participants)
        )

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