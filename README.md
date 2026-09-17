# 📚 Liana's Library

A simple library management application built with **Python, Streamlit, MySQL, SQLAlchemy, and pandas**.

The application allows a library owner to manage books, friends, and book loans through a simple web interface.

## ✨ Features

The application provides full **CRUD functionality** (Create, Read, Update, Delete) for:

### 👥 Friends

* View all friends
* Add a new friend
* Update friend information
* Delete a friend
* Set the maximum number of loans for each friend
* Add notes about friends

### 📚 Books

* Display all books
* Add a new book
* Update book information
* Delete a book

### 🔄 Loans

* Display current loans
* Add a loan
* Update loan information
* Delete a loan
* Track loan dates and contact dates
* Add notes about loans

## 🛠️ Technologies

* **Python** – application logic
* **Streamlit** – web interface
* **MySQL** – relational database
* **SQLAlchemy** – database connection
* **pandas** – reading and writing database data
* **MySQL Workbench** – database creation and management

## 🗄️ Database Structure

The application uses three related tables:

```text
FRIENDS
│
├── friend_id (Primary Key)
├── name
├── max_loans
└── notes

BOOKS
│
├── isbn (Primary Key)
├── title
├── author
└── genre

LOANS
│
├── isbn (Foreign Key → books)
├── friend_id (Foreign Key → friends)
├── loan_date
├── last_contact
├── next_contact
└── notes
```

The `loans` table connects **friends** with **books**.

The primary key of the `loans` table consists of:

```text
isbn + friend_id
```

Foreign key relationships are used to maintain the connections between the tables.

## 📁 Project Structure

```text
library_management_app/
│
├── src/
│   ├── app.py
│   ├── db.py
│   ├── create.py
│   ├── read.py
│   ├── update.py
│   ├── delete.py
│   │
│   └── .streamlit/
│       └── secrets.toml
│
├── sql_scripts/
│
├── notebooks/
│
└── .gitignore
```

### Python files

**`app.py`**
Contains the Streamlit user interface and connects the different CRUD functions to the interface.

**`db.py`**
Stores and provides access to the SQLAlchemy database engine.

**`create.py`**
Contains functions for creating new friends, books, and loans.

**`read.py`**
Contains functions for reading data from the database and preparing it for display.

**`update.py`**
Contains functions for updating existing friends, books, and loans.

**`delete.py`**
Contains functions for deleting friends, books, and loans.

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd library_management_app
```

### 2. Create and activate a virtual environment

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

**Mac/Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 3. Install the required packages

```bash
pip install streamlit pandas sqlalchemy pymysql
```

### 4. Set up MySQL

Open **MySQL Workbench** and run the SQL scripts located in:

```text
sql_scripts/
```

These scripts create the database, tables, and initial data.

The application expects a MySQL database named:

```text
my_library
```

### 5. Configure the database password

Create the following file:

```text
src/.streamlit/secrets.toml
```

Add your MySQL password:

```toml
[mysql]
password = "YOUR_MYSQL_PASSWORD"
```

**Important:** Never commit your `secrets.toml` file to GitHub.

The file is included in `.gitignore` to keep the database password private.

## ▶️ Run the Application

From the project directory, activate your virtual environment and run:

```bash
streamlit run src/app.py
```

Streamlit will open the application in your browser.

## 🔄 How the Application Works

The basic data flow is:

```text
Streamlit UI
     │
     ▼
   app.py
     │
     ├──────────────┐
     ▼              ▼
CRUD functions    db.py
     │              │
     └───────┬──────┘
             ▼
        SQLAlchemy
             │
             ▼
          MySQL
```

The application creates a SQLAlchemy database engine in `app.py`.

The CRUD modules then use the shared database engine from `db.py` to communicate with MySQL.

For example:

```python
import db

engine = db.get_engine()
```

This allows the `create.py`, `read.py`, `update.py`, and `delete.py` modules to work with the same database connection setup.

## 🎯 Project Goal

The goal of this project was to build a simple, practical database application while learning how different technologies work together.

It demonstrates the complete workflow:

```text
MySQL
  ↓
SQLAlchemy
  ↓
Python
  ↓
pandas
  ↓
Streamlit
  ↓
Interactive Web Application
```

## 🚀 Possible Future Improvements

Some features that could be added in the future include:

* Search and filtering
* More advanced input validation
* Loan-limit validation based on each friend's `max_loans`
* Returning books / tracking returned dates
* More detailed loan status
* Improved error messages
* Deployment so the application can be accessed online

These features are outside the scope of the current MVP.

## 👩‍💻 Author

**Liana**

Built as a learning and portfolio project while developing skills in **Python, SQL, data handling, and data applications**.
