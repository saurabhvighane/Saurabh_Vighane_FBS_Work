# 3. Design a basic calculator to perform +,-,/,*

from tkinter import *
from tkinter import messagebox


def calculate():

    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())

        operator = operator_entry.get()

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            result = num1 / num2

        else:
            messagebox.showerror("Error", "Invalid operator")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")


root = Tk()

root.title("Calculator")
root.geometry("400x350")


Label(root, text="Basic Calculator", font=("Arial", 18)).pack(pady=15)


Label(root, text="Enter First Number").pack()

num1_entry = Entry(root)
num1_entry.pack(pady=5)


Label(root, text="Enter Operator (+, -, *, /)").pack()

operator_entry = Entry(root)
operator_entry.pack(pady=5)


Label(root, text="Enter Second Number").pack()

num2_entry = Entry(root)
num2_entry.pack(pady=5)


Button(
    root,
    text="Calculate",
    command=calculate
).pack(pady=15)


result_label = Label(root, text="Result: ", font=("Arial", 14))
result_label.pack()


root.mainloop()