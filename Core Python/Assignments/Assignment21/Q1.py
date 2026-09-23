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

class InvalidOperatorError(Exception):
    pass

def calculator():
    print("--- Simple Calculator ---")
    try:
        # Request inputs from the user
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ").strip()
        num2 = float(input("Enter the second number: "))

        # Validate the operator
        if operator not in ['+', '-', '*', '/']:
            raise InvalidOperatorError(f"'{operator}' is not a valid operator.")

        # Perform the requested arithmetic operation
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2

        print(f"Result: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Error: Invalid Number. Please enter valid numeric values.")
    except InvalidOperatorError as e:
        print(f"Error: Invalid Operator. {e}")
    except ZeroDivisionError:
        print("Error: Division by Zero is not allowed.")

if __name__ == "__main__":
    calculator()
