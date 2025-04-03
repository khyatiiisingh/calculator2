# Simple Calculator Application with Enhanced Features
# This calculator performs basic arithmetic operations: addition, subtraction, multiplication, and division.
# It also includes support for power and modulo operations.
# The calculator provides error handling for invalid input and division by zero.

import math
import os

history = []

def add(a, b):
    result = a + b
    history.append(f"{a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    history.append(f"{a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    history.append(f"{a} * {b} = {result}")
    return result

def divide(a, b):
    try:
        result = a / b
        history.append(f"{a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        return "Division by zero is not allowed!"

def modulus(a, b):
    result = a % b
    history.append(f"{a} % {b} = {result}")
    return result

def power(a, b):
    result = a ** b
    history.append(f"{a} ** {b} = {result}")
    return result

def sqrt(a):
    result = math.sqrt(a)
    history.append(f"sqrt({a}) = {result}")
    return result

def show_history():
    if not history:
        print("No calculations performed yet!")
    else:
        print("Calculation History:")
        for item in history:
            print(item)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Simple Calculator")

while True:
    print("\nOptions:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. View Calculation History")
    print("9. Clear Screen")
    print("0. Exit")

    try:
        choice = int(input("Choose an operation (0-9): "))

        if choice == 0:
            print("Exiting the calculator. Goodbye!")
            break

        if choice == 8:
            show_history()
            continue
        
        if choice == 9:
            clear_screen()
            continue

        if choice not in [1, 2, 3, 4, 5, 6, 7]:
            print("Invalid choice! Please select a valid option.")
            continue

        if choice == 7:
            x = float(input("Enter a number: "))
            print(f"Result: {sqrt(x)}")
            continue

        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == 1:
            print(f"Result: {add(x, y)}")
        elif choice == 2:
            print(f"Result: {subtract(x, y)}")
        elif choice == 3:
            print(f"Result: {multiply(x, y)}")
        elif choice == 4:
            print(f"Result: {divide(x, y)}")
        elif choice == 5:
            print(f"Result: {modulus(x, y)}")
        elif choice == 6:
            print(f"Result: {power(x, y)}")

    except ValueError:
        print("Invalid input! Please enter numbers only.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

