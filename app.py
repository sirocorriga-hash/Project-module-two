from flask import Flask, render_template, request, redirect, url_for
from models import manager 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/expenses")
def expenses_page():
    return render_template("expenses.html", expenses=manager.expenses)

@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        manager.add_expense(
            request.form["description"], 
            request.form["amount"], 
            request.form["paid_by"]
        )
        return redirect(url_for("expenses_page"))
    return render_template("addexpenses.html", people=manager.people)

@app.route("/summary")
def summary():
    balances = manager.calculate_balances()
    return render_template("summary.html", balances=balances)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        manager.add_person(request.form["username"])
        return redirect(url_for("home"))
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)