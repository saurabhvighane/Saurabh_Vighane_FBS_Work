from flask import Flask, render_template, request, redirect, url_for, session
from models.account import Account

app = Flask(__name__)

app.secret_key = "change-this-secret-key"


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():

    error = None

    if request.method == "POST":

        account_id = request.form["account_id"].strip()
        pin = request.form["pin"].strip()

        account = Account()

        account_data = account.login(account_id, pin)

        if account_data:

            session["account_id"] = account_data["account_id"]
            session["name"] = account_data["name"]

            return redirect(url_for("dashboard"))

        else:

            error = "Invalid Account ID or PIN."

    return render_template(
        "login.html",
        error=error
    )


@app.route("/register", methods=["GET", "POST"])
def register():

    error = None
    account_id = None

    if request.method == "POST":

        name = request.form["name"].strip()
        phone = request.form["phone"].strip()
        email = request.form["email"].strip()
        pin = request.form["pin"].strip()
        confirm_pin = request.form["confirm_pin"].strip()

        if not name or not phone or not email:
            error = "All fields are required."

        elif len(phone) != 10 or not phone.isdigit():
            error = "Phone number must contain exactly 10 digits."

        elif "@" not in email or "." not in email:
            error = "Please enter a valid email."

        elif len(pin) != 4 or not pin.isdigit():
            error = "PIN must be exactly 4 digits."

        elif pin != confirm_pin:
            error = "PINs do not match."

        else:

            account = Account(
                name,
                phone,
                email,
                pin
            )

            account_id = account.create_account()

            if account_id is None:
                error = "Account creation failed."

    return render_template(
        "register.html",
        error=error,
        account_id=account_id
    )


@app.route("/dashboard")
def dashboard():

    if "account_id" not in session:
        return redirect(url_for("login"))

    account = Account()

    balance = account.check_balance(
        session["account_id"]
    )

    return render_template(
        "dashboard.html",
        name=session["name"],
        balance=balance
    )


@app.route("/deposit", methods=["GET", "POST"])
def deposit():

    if "account_id" not in session:
        return redirect(url_for("login"))

    error = None
    success = None

    if request.method == "POST":

        amount = request.form["amount"].strip()

        try:
            from decimal import Decimal

            amount = Decimal(amount)

            if amount <= 0:
                error = "Amount must be greater than 0."

            elif amount.as_tuple().exponent < -2:
                error = "Amount can have maximum 2 decimal places."

            else:
                account = Account()

                result = account.deposit(
                    session["account_id"],
                    amount
                )

                if result == "success":
                    success = f"₹{amount:.2f} deposited successfully."

                elif result == "account_not_found":
                    error = "Account not found."

                else:
                    error = "Deposit failed."

        except Exception:
            error = "Please enter a valid amount."

    return render_template(
        "deposit.html",
        error=error,
        success=success
    )

@app.route("/check-balance")
def check_balance():

    if "account_id" not in session:
        return redirect(url_for("login"))

    account = Account()

    balance = account.check_balance(
        session["account_id"]
    )

    if balance is None:
        return redirect(url_for("login"))

    return render_template(
        "check_balance.html",
        name=session["name"],
        balance=balance
    )


@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():

    if "account_id" not in session:
        return redirect(url_for("login"))

    error = None
    success = None

    if request.method == "POST":

        amount = request.form["amount"].strip()

        try:
            from decimal import Decimal, InvalidOperation

            amount = Decimal(amount)

            if amount <= 0:
                error = "Amount must be greater than 0."

            elif amount.as_tuple().exponent < -2:
                error = "Amount can have maximum 2 decimal places."

            else:

                account = Account()

                result = account.withdraw(
                    session["account_id"],
                    amount
                )

                if result == "success":

                    success = (
                        f"₹{amount:.2f} "
                        "withdrawn successfully."
                    )

                elif result == "account_not_found":

                    error = "Account not found."

                elif result == "insufficient_balance":

                    error = "Insufficient balance."

                else:

                    error = "Withdrawal failed."

        except (InvalidOperation, ValueError):

            error = "Please enter a valid amount."

    return render_template(
        "withdraw.html",
        error=error,
        success=success
    )


@app.route("/transfer", methods=["GET", "POST"])
def transfer():

    if "account_id" not in session:
        return redirect(url_for("login"))

    error = None
    success = None

    if request.method == "POST":

        receiver_id = request.form["receiver_id"].strip()
        amount = request.form["amount"].strip()

        try:
            from decimal import Decimal, InvalidOperation

            if not receiver_id.isdigit():
                error = "Receiver account ID must contain only numbers."

            elif int(receiver_id) <= 0:
                error = "Invalid receiver account ID."

            else:

                receiver_id = int(receiver_id)

                amount = Decimal(amount)

                if amount <= 0:
                    error = "Amount must be greater than 0."

                elif amount.as_tuple().exponent < -2:
                    error = "Amount can have maximum 2 decimal places."

                else:

                    account = Account()

                    result = account.transfer(
                        session["account_id"],
                        receiver_id,
                        amount
                    )

                    if result == "success":

                        success = (
                            f"₹{amount:.2f} "
                            f"transferred successfully."
                        )

                    elif result == "same_account":

                        error = (
                            "You cannot transfer money "
                            "to your own account."
                        )

                    elif result == "sender_not_found":

                        error = "Your account was not found."

                    elif result == "receiver_not_found":

                        error = "Receiver account not found."

                    elif result == "insufficient_balance":

                        error = "Insufficient balance."

                    else:

                        error = "Transfer failed."

        except (InvalidOperation, ValueError):

            error = "Please enter a valid amount."

    return render_template(
        "transfer.html",
        error=error,
        success=success
    )

@app.route("/transactions")
def transactions():

    if "account_id" not in session:
        return redirect(url_for("login"))

    account = Account()

    transaction_data = account.get_transactions(
        session["account_id"]
    )

    return render_template(
        "transactions.html",
        transactions=transaction_data
    )

@app.route("/change-pin", methods=["GET", "POST"])
def change_pin():

    if "account_id" not in session:
        return redirect(url_for("login"))

    error = None
    success = None

    if request.method == "POST":

        current_pin = request.form["current_pin"].strip()
        new_pin = request.form["new_pin"].strip()
        confirm_pin = request.form["confirm_pin"].strip()

        # Validate PIN format
        if (
            len(current_pin) != 4
            or not current_pin.isdigit()
        ):
            error = "Current PIN must be exactly 4 digits."

        elif (
            len(new_pin) != 4
            or not new_pin.isdigit()
        ):
            error = "New PIN must be exactly 4 digits."

        elif new_pin != confirm_pin:
            error = "New PINs do not match."

        elif current_pin == new_pin:
            error = "New PIN must be different from current PIN."

        else:

            account = Account()

            result = account.change_pin(
                session["account_id"],
                current_pin,
                new_pin
            )

            if result == "success":

                success = "PIN changed successfully."

            elif result == "wrong_pin":

                error = "Current PIN is incorrect."

            elif result == "account_not_found":

                error = "Account not found."

            else:

                error = "PIN change failed."

    return render_template(
        "change_pin.html",
        error=error,
        success=success
    )



@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
