# 1. Develop a simple login system with a username and password field. Implement user
# authentication, and show a success message if the login is successful, or an error
# message if the login fails.

from tkinter import *
from tkinter import messagebox


def login():

    user = username.get()
    pwd = password.get()

    if user == "Saurabh" and pwd == "1234":
        messagebox.showinfo("Success", "Login Successful")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")


root = Tk()

root.title("Login System")
root.geometry("400x250")


Label(root, text="Username").pack(pady=10)

username = Entry(root)
username.pack()


Label(root, text="Password").pack(pady=10)

password = Entry(root, show="*")
password.pack()


Button(root, text="Login", command=login).pack(pady=20)


root.mainloop()
