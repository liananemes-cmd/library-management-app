import pandas as pd
import db

# ---------- FRIENDS ----------------
def create_friend(name, max_loans=2,notes=None):
    engine = db.get_engine()
    df = pd.DataFrame([[name, max_loans, notes]], 
                      columns=["name", 
                               "max_loans",
                               "notes"])

    df.to_sql("friends", if_exists="append", con=engine, index=False)

    message = f"Added '{name}' to 'friends'."

    return message

# ---------- BOOKS ----------------

def create_book(title, author, genre, isbn):
    engine = db.get_engine()

    df = pd.DataFrame(
        [[title, author, genre, isbn]],
        columns=["title", "author", "genre", "isbn"]
    )

    df.to_sql(
        "books",
        if_exists="append",
        con=engine,
        index=False
    )

    message = f"Added '{title}' to 'books'."

    return message

# ---------- LOANS ----------------

def create_loan(isbn, friend_id, loan_date, last_contact, next_contact, notes):
    engine = db.get_engine()

    df = pd.DataFrame(
        [[
            isbn,
            friend_id,
            loan_date,
            last_contact,
            next_contact,
            notes
        ]],
        columns=[
            "isbn",
            "friend_id",
            "loan_date",
            "last_contact",
            "next_contact",
            "notes"
        ]
    )

    df.to_sql(
        "loans",
        if_exists="append",
        con=engine,
        index=False
    )

    return "Loan added."