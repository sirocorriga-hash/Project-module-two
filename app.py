from flask import Flask, render_template, request, redirect, url_for
from data import expenses, people

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/expenses")
def expenses_page():
    return render_template("expenses.html", expenses=expenses)

@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        expenses.append({
            "description": request.form["description"],
            "amount": float(request.form["amount"]),
            "paid_by": request.form["paid_by"]
        })
        return redirect(url_for("expenses_page"))

    return render_template("add_expense.html", people=people)

@app.route("/summary")
def summary():
    balances = {p: 0 for p in people}

    for e in expenses:
        share = e["amount"] / len(people)

        for p in people:
            if p == e["paid_by"]:
                balances[p] += e["amount"] - share
            else:
                balances[p] -= share

    return render_template("summary.html", balances=balances)

if __name__ == "__main__":
    app.run(debug=True)