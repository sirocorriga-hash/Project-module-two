

from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, manager

app = Flask(__name__)
app.secret_key = "dev-key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///splitz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
        return redirect(url_for("home"))

    return render_template("addperson.html")


if __name__ == "__main__":
    app.run(debug=True)