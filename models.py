
class Expense:
    def __init__(self, description, amount, paid_by):
        self.description = description
        self.amount = float(amount)
        self.paid_by = paid_by

class ExpenseManager:
    def __init__(self):
        self.expenses = []
        self.people = []

    def add_expense(self, description, amount, paid_by):
        new_expense = Expense(description, amount, paid_by)
        self.expenses.append(new_expense)

    def add_person(self, name):
        if name not in self.people:
            self.people.append(name)

    def calculate_balances(self):
        balances = {p: 0 for p in self.people}
        if not self.people:
            return balances
            
        for e in self.expenses:
            share = e.amount / len(self.people)
            for p in self.people:
                if p == e.paid_by:
                    balances[p] += e.amount - share
                else:
                    balances[p] -= share
        return balances

manager = ExpenseManager()