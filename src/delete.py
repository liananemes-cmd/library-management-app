import pandas as pd
from sqlalchemy import text
import db

# ------- FRIENDS ----------------

def delete_friend(friend):
    engine= db.get_engine()

    delete_query = """
        DELETE FROM friends
        WHERE friend_id = :val;
    """

    with engine.begin() as connection:
        connection.execute(
            text(delete_query),
            {"val": friend["friend_id"]}
        )

    return f"Removed '{friend['name']}' from 'friends'."

# --------- BOOKS ----------------

def delete_book(book):
    engine = db.get_engine()

    delete_query = """
        DELETE FROM books
        WHERE isbn = :isbn;
    """

    with engine.begin() as connection:
        connection.execute(
            text(delete_query),
            {"isbn": book["isbn"]}
        )

    return f"Removed '{book['title']}' from 'books'."

# --------- LOANS ----------------

def delete_loan(loan):
    engine = db.get_engine()

    delete_query = """
        DELETE FROM loans
        WHERE isbn = :isbn
        AND friend_id = :friend_id;
    """

    with engine.begin() as connection:
        connection.execute(
            text(delete_query),
            {
                "isbn": loan["isbn"],
                "friend_id": loan["friend_id"]
            }
        )

    return "Loan deleted."