import pandas as pd
import db

# --------- FRIENDS -------------

def prettify_df(df):
    df.columns = [c.upper() if c == "isbn" else c.replace("_"," ").capitalize() for c in df.columns]
    return df.fillna("")

def read_friends():
    engine = db.get_engine()
    return pd.read_sql("friends", con=engine)

def display_friends():
    friends = read_friends()
    return friends.pipe(prettify_df).loc[:, "Name":]

# --------- BOOKS -------------

def read_books():
    engine = db.get_engine()
    return pd.read_sql("books", con=engine)

def display_books():
    books = read_books()
    return books.pipe(prettify_df)

# --------- LOANS -------------

def read_loans():
    engine = db.get_engine()

    query = """
        SELECT
            l.isbn,
            b.title,
            l.friend_id,
            f.name,
            l.loan_date,
            l.last_contact,
            l.next_contact,
            l.notes
        FROM loans l
        JOIN books b ON l.isbn = b.isbn
        JOIN friends f ON l.friend_id = f.friend_id
    """

    return pd.read_sql(query, con=engine)


def display_loans():
    loans = read_loans()
    return loans.pipe(prettify_df)