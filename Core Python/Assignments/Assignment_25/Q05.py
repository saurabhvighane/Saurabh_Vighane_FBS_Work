# 5. Write a Python function that takes an email address as input and uses a regular
# expression to validate if it is a valid email address. The function should return True for
# valid emails and False for invalid ones.

import re


def validate_email(email):

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        return True
    else:
        return False


email = input("Enter email address: ")

if validate_email(email):
    print("Valid Email")

else:
    print("Invalid Email")