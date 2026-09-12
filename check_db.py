import sqlite3

con = sqlite3.connect("splitz.db")
cur = con.cursor()

print(
    "Tables:",
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall(),
)

print("People:", cur.execute("SELECT * FROM person").fetchall())
print("Expenses:", cur.execute("SELECT * FROM expense").fetchall())
print("Participants:", cur.execute("SELECT * FROM expense_participants").fetchall())
