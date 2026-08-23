# 2. WAP a menu driven program to perform following operations using
# files :

# a. Add a record
# b. Search for a record using id
# c. Delete a record using id
# d. Edit a record using id.
# e. Display all records.

import pickle
import os
from Q01 import Emp

file_name='Emp.dat'

def add_emp():
    eid=int(input("Enter Employee Id: "))
    ename=input("Enter Employee Name: ")
    basic=float(input("Enter basic salary: "))

    emp=Emp(eid,ename,basic)

    with open (file_name,'ab') as f:
        pickle.dump(emp,f)

    print("Employee Added Successfully")

def search_emp():
    eid=int(input("Enter Employee ID: "))
    found=False

    try:
        with open (file_name,'rb') as f:
            while True:
                try:
                    emp=pickle.load(f)

                    if emp.eid==eid:
                        print("Employee Found")
                        print(emp)
                        found=True
                        break
                except EOFError:
                    break

    except FileNotFoundError:
        print("Employee Records Not Found")
        return
    if not found:
        print("Employee Not Found")


# Delete Employee
def delete_emp():

    eid = int(input("Enter Employee ID to delete: "))
    found = False

    try:
        with open(file_name, "rb") as f, open("temp.dat", "wb") as temp:

            while True:
                try:
                    emp = pickle.load(f)

                    if emp.eid == eid:
                        found = True
                        print("Employee deleted successfully.")
                    else:
                        pickle.dump(emp, temp)

                except EOFError:
                    break

        os.remove(file_name)
        os.rename("temp.dat", file_name)

        if not found:
            print("Employee not found.")

    except FileNotFoundError:
        print("No employee records found.")


# Edit Employee
def edit_emp():

    eid = int(input("Enter Employee ID to edit: "))
    found = False

    try:
        with open(file_name, "rb") as f, open("temp.dat", "wb") as temp:

            while True:
                try:
                    emp = pickle.load(f)

                    if emp.eid == eid:

                        print("Current Employee Details:")
                        print(emp)

                        emp.ename = input("Enter new name: ")
                        emp.basic = float(input("Enter new basic salary: "))

                        found = True

                    pickle.dump(emp, temp)

                except EOFError:
                    break

        os.remove(file_name)
        os.rename("temp.dat", file_name)

        if found:
            print("Employee updated successfully.")
        else:
            print("Employee not found.")

    except FileNotFoundError:
        print("No employee records found.")


# Display All Employees
def display_emp():

    try:
        with open(file_name, "rb") as f:

            print("\n----- Employee Records -----")

            while True:
                try:
                    emp = pickle.load(f)
                    print(emp)

                except EOFError:
                    break

    except FileNotFoundError:
        print("No employee records found.")


# Menu
while True:

    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Delete Employee")
    print("4. Edit Employee")
    print("5. Display All Employees")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_emp()

    elif choice == 2:
        search_emp()

    elif choice == 3:
        delete_emp()

    elif choice == 4:
        edit_emp()

    elif choice == 5:
        display_emp()

    elif choice == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")