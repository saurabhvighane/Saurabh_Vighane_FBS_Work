🏦 Bank Management System

A web-based Bank Management System built using Python, Flask, MySQL,
HTML, and CSS.

This project was developed as a practical learning project to understand
how a Python backend, web interface, SQL queries, and a relational
database work together in a complete application.

🚀 Features

🔐 User Registration

🔑 User Login with Account ID and PIN

💰 Check Account Balance

➕ Deposit Money

➖ Withdraw Money

🔄 Transfer Money between accounts

📊 View Transaction History

🔒 Change PIN

🚪 Logout

🗄️ MySQL database integration

🌐 Flask web application

📱 Responsive and user-friendly interface

🛠️ Technologies Used

Technology               Purpose

Python                   Application logic
Flask                    Web framework and routing
MySQL                    Database
HTML                     Web page structure
CSS                      User interface and styling
mysql-connector-python   Python-MySQL connection
Jinja2                   Dynamic HTML rendering

📁 Project Structure

Bank Management System/
│
├── app.py
│
├── database/
│   ├── __init__.py
│   └── connection.py
│
├── models/
│   ├── __init__.py
│   └── account.py
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── check_balance.html
│   ├── deposit.html
│   ├── withdraw.html
│   ├── transfer.html
│   ├── transactions.html
│   └── change_pin.html
│
├── static/
│   └── css/
│       └── style.css
│
├── requirements.txt
├── .gitignore
└── README.md

⚙️ How It Works

The application follows a simple layered structure:

Browser
   ↓
HTML / CSS
   ↓
Flask Routes
   ↓
Python Account Logic
   ↓
MySQL Database

For example, when a user transfers money:

Transfer Form
     ↓
Flask /transfer route
     ↓
Account.transfer()
     ↓
SQL queries using cursor.execute()
     ↓
Update sender balance
     ↓
Update receiver balance
     ↓
Record transactions
     ↓
Database commit

🗄️ Database

The application uses MySQL to store account and transaction data.

Main tables include:

accounts

transactions

transfers

The application uses parameterized SQL queries with %s placeholders
when communicating with MySQL.

Example:

query = """
SELECT *
FROM accounts
WHERE account_id = %s
AND pin = %s
"""

cursor.execute(query, (account_id, pin))

🔧 Installation

1. Clone the repository

git clone https://github.com/saurabhvighane/Saurabh_Vighane_FBS_Work.git

Navigate to the project directory:

cd "Saurabh_Vighane_FBS_Work/Python Projects/Bank Management System"

2. Create a virtual environment

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Configure MySQL

Create a MySQL database and the required tables.

Update the database connection settings in:

database/connection.py

Do not upload your actual database password or secret keys to
GitHub.

5. Run the application

python app.py

Open the application in your browser:

http://127.0.0.1:5000

🧪 Main Operations

Create Account

A user provides basic information such as:

Name

Phone

Email

PIN

The application creates an account and generates an account ID.

Login

The user logs in using:

Account ID + PIN

After successful authentication, the user is redirected to the
dashboard.

Deposit

The entered amount is added to the user's account balance and a
transaction is recorded.

Withdraw

The application checks the available balance before deducting the
requested amount.

Transfer

The application:

Identifies the sender.

Identifies the receiver.

Checks the sender's balance.

Deducts the amount from the sender.

Adds the amount to the receiver.

Records the transaction.

Commits the database changes.

Transaction History

Users can view their previous deposits, withdrawals, and transfers.

Change PIN

Users can change their PIN after providing their current PIN and a valid
new PIN.

📚 What I Learned

Through this project, I practiced:

Python OOP

Flask routing

HTTP GET and POST requests

HTML forms

Jinja2 templates

Sessions and authentication flow

MySQL connectivity

SQL SELECT, INSERT, and UPDATE

Parameterized SQL queries

Database transactions

commit() and rollback()

CRUD-style database operations

Project folder organization

HTML/CSS UI development

Debugging Flask and database errors

🔮 Future Improvements

Possible improvements for future versions:

Password/PIN hashing

Environment variables for database configuration

CSRF protection

Better authentication and session security

Pagination for transaction history

Transaction filtering

Email notifications

Admin dashboard

Account statements

Deployment to a cloud platform

👨‍💻 Author

Saurabh Vighane

This project was created as part of my practical Python and web
development learning journey.

⭐ If you find this project useful, feel free to explore the repository
and follow my learning journey.
