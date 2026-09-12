from app import app
from models import db

with app.app_context():
    uri = app.config["SQLALCHEMY_DATABASE_URI"]
    db_type = "PostgreSQL" if uri.startswith("postgresql://") else "SQLite"

    confirm = input(
        f"You are about to delete ALL data from the {db_type} database. "
        "Type 'yes' to confirm: "
    )

    if confirm.strip().lower() != "yes":
        print("Operation cancelled.")
    else:
        db.drop_all()
        db.create_all()
        print("Database cleared.")