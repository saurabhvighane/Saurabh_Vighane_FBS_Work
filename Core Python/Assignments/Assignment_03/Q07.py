# Write a program to check if user has entered correct userid and password.


user=input("Enter username: ")
p=input("Enter password: ")

username="admin1"
password="@123"

if(username==user and password==p):
    print('Login Successful')
else:
    print("Login failed!")