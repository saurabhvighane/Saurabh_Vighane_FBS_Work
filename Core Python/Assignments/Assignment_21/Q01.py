# 1. Develop a simple calculator program that performs basic arithmetic operations (+,
# -, *, /) on two numbers provided by the user. The program should ask the user for
# the numbers and the operator. However, the program should handle the following
# exceptions:
# a. Invalid Number: If the user enters a number that is not valid, catch the
# exception and display an error message.
# b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
# "/", catch the exception and display an error message.
# c. Division by Zero: If the user tries to divide by zero, catch the exception and
# display an error message.
# Write a program that performs the requested arithmetic operation and
# handles the exceptions as described above.

# Custom exception for handling invalid operators
class InvalidOperatorError(Exception):
    pass


def calculate():
    try:
        # a. Invalid Number Exception Handling (ValueError)
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ").strip()

        # b. Invalid Operator Exception Handling
        if operator not in ('+', '-', '*', '/'):
            raise InvalidOperatorError(f"Invalid Operator '{operator}'. Please use only +, -, *, or /.")

        num2 = float(input("Enter second number: "))

        # Performing arithmetic operation
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            # c. Division by Zero Exception Handling (ZeroDivisionError)
            result = num1 / num2

        print(f"Result: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Error: Invalid Number! Please enter valid numeric values.")
    except InvalidOperatorError as e:
        print(f"Error: {e}")
    except ZeroDivisionError:
        print("Error: Division by Zero! Denominator cannot be zero.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    while True:
        calculate()


