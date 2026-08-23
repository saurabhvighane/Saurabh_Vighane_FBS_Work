# 2. Build a currency converter application that converts between different currencies. The
# user should be able to enter an amount, select the input currency, select the output
# currency, and see the converted amount.

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def convert():

    try:
        amount = float(amount_entry.get())

        from_currency = from_currency_box.get()
        to_currency = to_currency_box.get()

        # Conversion rates compared to INR
        rates = {
            "INR": 1,
            "USD": 83,
            "EUR": 90
        }

        # Convert selected currency to INR first
        amount_in_inr = amount * rates[from_currency]

        # Convert INR to selected currency
        result = amount_in_inr / rates[to_currency]

        result_label.config(text=f"Converted Amount: {result:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount")


root = Tk()

root.title("Currency Converter")
root.geometry("400x300")


Label(root, text="Currency Converter", font=("Arial", 16)).pack(pady=15)


Label(root, text="Enter Amount").pack()

amount_entry = Entry(root)
amount_entry.pack(pady=5)


Label(root, text="From Currency").pack()

from_currency_box = ttk.Combobox(
    root,
    values=["INR", "USD", "EUR"]
)

from_currency_box.pack(pady=5)
from_currency_box.current(0)


Label(root, text="To Currency").pack()

to_currency_box = ttk.Combobox(
    root,
    values=["INR", "USD", "EUR"]
)

to_currency_box.pack(pady=5)
to_currency_box.current(1)


Button(
    root,
    text="Convert",
    command=convert
).pack(pady=15)


result_label = Label(root, text="Converted Amount: ")
result_label.pack()


root.mainloop()