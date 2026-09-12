import sqlite3

con = sqlite3.connect("splitz.db")
cur = con.cursor()

print("Tabelle:", cur.execute(
    "SELECT name FROM sqlite_master WHERE type='table'"
).fetchall())

print("Persone:", cur.execute("SELECT * FROM person").fetchall())
print("Spese:", cur.execute("SELECT * FROM expense").fetchall())
print("Partecipanti:", cur.execute("SELECT * FROM expense_participants").fetchall())