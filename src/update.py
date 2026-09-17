from sqlalchemy import text
import db

def get_column_name(field_choice):
    if field_choice == "Name":
        return "name"
    elif field_choice == "Max loans":
        return "max_loans"
    elif field_choice == "Notes":
        return "notes"

# --------- FRIENDS ----------------
def update_friend(friend, field_choice, new_data):
    engine = db.get_engine()
    column = get_column_name(field_choice)

    update_query = text(f"""
        UPDATE friends
        SET {column} = :new_data
        WHERE friend_id = :friend_id
    """)

    with engine.begin() as connection:
        connection.execute(
            update_query,
            {"new_data": new_data, "friend_id": friend["friend_id"]}
        )
    return f"{field_choice} updated."

# --------- BOOKS ----------------

def update_book(book, field_choice, new_data):
    engine = db.get_engine()

    if field_choice == "Title":
        column = "title"
    elif field_choice == "Author":
        column = "author"
    elif field_choice == "Genre":
        column = "genre"

    update_query = text(f"""
        UPDATE books
        SET {column} = :new_data
        WHERE isbn = :isbn
    """)

    with engine.begin() as connection:
        connection.execute(
            update_query,
            {
                "new_data": new_data,
                "isbn": book["isbn"]
            }
        )

    return f"{field_choice} updated."

# --------- LOANS ----------------

def update_loan(loan, field_choice, new_data):
    engine = db.get_engine()

    if field_choice == "Loan date":
        column = "loan_date"
    elif field_choice == "Last contact":
        column = "last_contact"
    elif field_choice == "Next contact":
        column = "next_contact"
    elif field_choice == "Notes":
        column = "notes"

    update_query = text(f"""
        UPDATE loans
        SET {column} = :new_data
        WHERE isbn = :isbn
        AND friend_id = :friend_id
    """)

    with engine.begin() as connection:
        connection.execute(
            update_query,
            {
                "new_data": new_data,
                "isbn": loan["isbn"],
                "friend_id": loan["friend_id"]
            }
        )

    return f"{field_choice} updated."