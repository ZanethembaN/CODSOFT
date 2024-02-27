import math
from pyfiglet import Figlet
from colours import *

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
        if math.isinf(result):
            raise ZeroDivisionError
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero!"

def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Cannot calculate square root of a negative number!"


def calculator():

    table_label = "CALCULATOR"
    custom_fig = Figlet(font='standard')
    ascii_art = custom_fig.renderText(table_label)
    ascii_art = f'{CYAN}{BOLD}{ascii_art}{RESET}'
    print(ascii_art)
    print(f"{BOLD}OPERATIONS:{RESET}\n")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)\n")

    try:
        operation_choice = input(f"{CYAN}{BOLD}Choose operation (1-6):{RESET} ").strip()
        num1 = float(input(f"{CYAN}{BOLD}Enter the first number:{RESET} "))


        if operation_choice in ["1", "2", "3", "4"]:
            num2 = float(input(f"{CYAN}{BOLD}Enter the second number:{RESET} "))
        
        if operation_choice == "1":
            result = add(num1, num2)
        elif operation_choice == "2":
            result = subtract(num1, num2)
        elif operation_choice == "3":
            result = multiply(num1, num2)
        elif operation_choice == "4":
            result = divide(num1, num2)
        elif operation_choice == "5":
            num2 = float(input("Enter the exponent: "))
            result = power(num1, num2)
        elif operation_choice == "6":
            result = square_root(num1)
        else:
            result = "Invalid operation choice."

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    calculator()