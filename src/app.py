import streamlit as st
import pandas as pd 
from sqlalchemy import create_engine
from datetime import date, timedelta
import db
from create import *
from delete import *
from read import *
from update import *


# ---------- DATABASE SETUP ---------------------

DB_USER = "root"
DB_PORT = 3306
DB_HOST = "127.0.0.1"
DB_NAME = "my_library"
SQL_PASS = st.secrets["mysql"]["password"]

connection_string = f"mysql+pymysql://{DB_USER}:{SQL_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


if "engine" not in st.session_state:
    st.session_state['engine'] =create_engine(connection_string)

db.set_engine(st.session_state['engine'])


st.title("Welcome to Liana's Library", text_alignment="center")
# this section makes the buttons look like folder sections
st.markdown("""
<style>

div.stButton > button {
    border: none;
    border-radius: 10px 10px 0 0;
    padding: 12px 20px;
    font-weight: bold;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# ---------- MAIN NAVIGATION ---------------------

def change_section(section):
    st.session_state["section"] = section


col1, col2, col3 = st.columns(3)

with col1:
    st.button(
        "🧑‍🤝‍🧑 FRIENDS" if st.session_state["section"] == "Friends" else "👥 Friends",
        use_container_width=True,
        on_click=change_section,
        args=("Friends",)
    )

with col2:
    st.button(
        "📖 BOOKS" if st.session_state["section"] == "Books" else "📚 Books",
        use_container_width=True,
        on_click=change_section,
        args=("Books",)
    )

with col3:
    st.button(
        "📂 LOANS" if st.session_state["section"] == "Loans" else "🔄 Loans",
        use_container_width=True,
        on_click=change_section,
        args=("Loans",)
    )

section = st.session_state["section"]

st.divider()
#------------ FRIENDS Radio-button Menu ------------

if section == "Friends":

    action = st.radio(
        "Selection:",
        options=[
            "Read friends",
            "Create friend",
            "Update friend",
            "Delete friend"
        ]
    )

#---------------- FRIENDS CRUD --------------------------

    if action == "Read friends":
        friends_df = display_friends()
        st.dataframe(friends_df, hide_index=True)

    if action == "Create friend":
        friend_name = st.text_input("Name:")
        max_loans = st.number_input(
            "Max Loans:",
            min_value=1,
            value=2
)
        notes = st.text_area("Notes:")

        if st.button("Submit"):
            st.success(create_friend(friend_name, max_loans, notes))
            st.balloons()

    if action == "Update friend":
        friends_df = read_friends()

        friend_name = st.selectbox(
            "Select a friend...",
            friends_df["name"]
        )

        friend = friends_df[
            friends_df["name"] == friend_name
        ].iloc[0]

        field_choise = st.selectbox(
            "Choose a field",
            options=["Name", "Max loans", "Notes"]
        )

        if field_choise == "Max loans":
            current_max_loans = friend["max_loans"]

            if pd.isna(current_max_loans): # we need this code to make sure when we update it streamlit does not scream that NAN is not an integer
                current_max_loans = 2

            new_val = st.number_input(
                 "New Amount:",
                  min_value=1,
                 value=int(current_max_loans)
            )
        if field_choise == "Notes":
            new_val = st.text_area(
                "New note:",
                value=friend["notes"]
            )

        if st.button("Submit"):
            st.success(
                update_friend(friend, field_choise, new_val)
            )

    if action == "Delete friend":
        friends_df = read_friends()

        friend_name = st.selectbox(
            "Select a friend to delete:",
            friends_df["name"]
        )

        friend = friends_df[
            friends_df["name"] == friend_name
        ].iloc[0]

        if st.button("Submit"):
            st.success(delete_friend(friend))

#------------ BOOKS Radio-button Menu ------------

if section == "Books":

    action = st.radio(
        "Selection:",
        options=[
            "Display books",
            "Add book",
            "Update book",
            "Delete book"
        ]
    )

#-------------------- BOOKS CRUD -----------------

    if action == "Display books":
        books_df = display_books()
        st.dataframe(books_df, hide_index=True)

    if action == "Add book":
        title = st.text_input("Title:")
        author = st.text_input("Author:")
        genre = st.text_input("Genre:")
        isbn = st.text_input("ISBN:")

        if st.button("Submit"):
            st.success(
                create_book(title, author, genre, isbn)
            )
    if action == "Update book":
        books_df = read_books()

        book_title = st.selectbox(
            "Select a book...",
            books_df["title"]
        )

        book = books_df[
            books_df["title"] == book_title
        ].iloc[0]

        field_choice = st.selectbox(
            "Choose a field",
            options=["Title", "Author", "Genre"]
        )

        if field_choice == "Title":
            new_val = st.text_input(
                "New Title:",
                value=book["title"]
            )

        if field_choice == "Author":
            new_val = st.text_input(
                "New Author:",
                value=book["author"]
            )

        if field_choice == "Genre":
            new_val = st.text_input(
                "New Genre:",
                value=book["genre"]
            )

        if st.button("Submit"):
            st.success(
                update_book(book, field_choice, new_val)
            )
    if action == "Delete book":
        books_df = read_books()

        book_title = st.selectbox(
            "Select a book to delete:",
            books_df["title"]
        )

        book = books_df[
            books_df["title"] == book_title
        ].iloc[0]

        if st.button("Submit"):
            st.success(delete_book(book))

#------------ LOANS Radio-button Menu ------------

if section == "Loans":

    action = st.radio(
        "Selection:",
        options=[
            "Display loans",
            "Add loan",
            "Update loan",
            "Delete loan"
        ]
    )

#-------------------- LOANS CRUD -----------------
    
    if action == "Display loans":
        loans_df = display_loans()
        st.dataframe(loans_df, hide_index=True)

    if action == "Add loan":

        books_df = read_books()
        friends_df = read_friends()

        book_title = st.selectbox(
            "Select a book:",
            books_df["title"]
        )

        book = books_df[
            books_df["title"] == book_title
        ].iloc[0]

        friend_name = st.selectbox(
            "Select a friend:",
            friends_df["name"]
        )

        friend = friends_df[
            friends_df["name"] == friend_name
        ].iloc[0]

        loan_date = st.date_input(
            "Loan date:"
        )

        last_contact = st.date_input(
            "Last contact:",
            value=None
        )

        next_contact = st.date_input(
            "Next contact:",
            value=date.today() + timedelta(days=30)
        )

        notes = st.text_area(
            "Notes:"
        )

        if st.button("Submit"):
            st.success(
                create_loan(
                    book["isbn"],
                    friend["friend_id"],
                    loan_date,
                    last_contact,
                    next_contact,
                    notes
                )
            )
    if action == "Update loan":

        loans_df = read_loans()

        loan_options = (
            loans_df["title"]
            + " → "
            + loans_df["name"]
        )

        selected_loan = st.selectbox(
            "Select a loan:",
            loan_options
        )

        loan_index = loan_options[
            loan_options == selected_loan
        ].index[0]

        loan = loans_df.loc[loan_index]

        field_choice = st.selectbox(
            "Choose a field:",
            options=[
                "Loan date",
                "Last contact",
                "Next contact",
                "Notes"
            ]
        )

        if field_choice == "Loan date":
            new_val = st.date_input(
                "New loan date:",
                value=loan["loan_date"]
            )

        if field_choice == "Last contact":

            current_last_contact = loan["last_contact"]

            if pd.isna(current_last_contact): # this makes sure there is no empty value when we wish to update
                current_last_contact = date.today() # because if this field is empty when we wish to update it strem sees NULL and expects date and returns error

            new_val = st.date_input(
                "New last contact:",
                value=current_last_contact
            )

        if field_choice == "Next contact":
            new_val = st.date_input(
                "New next contact:",
                value=loan["next_contact"]
            )

        if field_choice == "Notes":

            current_notes = loan["notes"]

            if pd.isna(current_notes):#same as with last contact field in loans and max loans field in friends, 
                current_notes = "" #sql allows these fields to be empty but streamlit will expect a value when we try to update and thus we need this code

            new_val = st.text_area(
                "New note:",
                value=loan["notes"]
            )

        if st.button("Submit"):
            st.success(
                update_loan(
                    loan,
                    field_choice,
                    new_val
                )
            )
    if action == "Delete loan":

        loans_df = read_loans()

        loan_options = (
            loans_df["title"]
            + " → "
            + loans_df["name"]
        )

        selected_loan = st.selectbox(
            "Select a loan to delete:",
            loan_options
        )

        loan_index = loan_options[
            loan_options == selected_loan
        ].index[0]

        loan = loans_df.loc[loan_index]

        if st.button("Submit"):
            st.success(delete_loan(loan))