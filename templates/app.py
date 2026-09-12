from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, manager, Person, Expense

app = Flask(__name__)
app.secret_key = "dev-key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///splitz.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    stats = {
        "num_expenses": len(manager.expenses),
        "num_people": len(manager.people)
    }
    return render_template("home.html", stats=stats)


@app.route("/expenses")
def expenses_page():
    return render_template(
        "expenses.html",
        expenses=manager.expenses
    )


@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        try:
            description = request.form.get("description", "").strip()
            amount = request.form.get("amount", "").strip()
            paid_by = request.form.get("paid_by", "").strip()
            participants = request.form.getlist("participants")

            # validation
            if not description or not amount or not paid_by:
                flash("All fields are required!", "danger")
                return redirect(url_for("add_expense"))

            amount = float(amount)

            manager.add_expense(description, amount, paid_by, participants)

            flash("Expense added successfully!", "success")
            return redirect(url_for("expenses_page"))

        except ValueError as e:
            flash(str(e), "danger")
            return redirect(url_for("add_expense"))

        except Exception as e:
            flash(f"Unexpected error: {str(e)}", "danger")
            return redirect(url_for("add_expense"))

    return render_template(
        "addexpenses.html",
        people=manager.people
    )


@app.route("/expenses/<int:expense_id>/edit", methods=["GET", "POST"])
def edit_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)

    if request.method == "POST":
        try:
            description = request.form.get("description", "").strip()
            amount = request.form.get("amount", "").strip()
            paid_by = request.form.get("paid_by", "").strip()
            participants = request.form.getlist("participants")

            if not description or not amount or not paid_by:
                flash("All fields are required!", "danger")
                return redirect(url_for("edit_expense", expense_id=expense_id))

            manager.update_expense(expense_id, description, amount, paid_by, participants)

            flash("Expense updated successfully!", "success")
            return redirect(url_for("expenses_page"))

        except ValueError as e:
            flash(str(e), "danger")
            return redirect(url_for("edit_expense", expense_id=expense_id))

        except Exception as e:
            flash(f"Unexpected error: {str(e)}", "danger")
            return redirect(url_for("edit_expense", expense_id=expense_id))

    return render_template(
        "editexpense.html",
        expense=expense,
        people=manager.people
    )


@app.route("/expenses/<int:expense_id>/delete", methods=["POST"])
def delete_expense(expense_id):
    try:
        manager.delete_expense(expense_id)
        flash("Expense deleted successfully!", "success")
    except ValueError as e:
        flash(str(e), "danger")

    return redirect(url_for("expenses_page"))


@app.route("/summary")
def summary():
    balances = manager.calculate_balances()
    return render_template("summary.html", balances=balances)


@app.route("/addperson", methods=["GET", "POST"])
def add_person():
    if request.method == "POST":
        username = request.form.get("username", "").strip()

        if not username:
            flash("Username is required!", "danger")
            return redirect(url_for("add_person"))

        manager.add_person(username)
        flash("User added successfully!", "success")
        return redirect(url_for("add_person"))

    return render_template(
        "addperson.html",
        existing_people=Person.query.order_by(Person.username).all()
    )


@app.route("/people/<int:person_id>/edit", methods=["GET", "POST"])
def edit_person(person_id):
    person = Person.query.get_or_404(person_id)

    if request.method == "POST":
        try:
            username = request.form.get("username", "").strip()
            manager.update_person(person_id, username)
            flash("Person updated successfully!", "success")
            return redirect(url_for("add_person"))
        except ValueError as e:
            flash(str(e), "danger")
            return redirect(url_for("edit_person", person_id=person_id))

    return render_template("editperson.html", person=person)


@app.route("/people/<int:person_id>/delete", methods=["POST"])
def delete_person(person_id):
    try:
        manager.delete_person(person_id)
        flash("Person deleted successfully!", "success")
    except ValueError as e:
        flash(str(e), "danger")

    return redirect(url_for("add_person"))


if __name__ == "__main__":
    app.run(debug=True)