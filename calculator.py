def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed!"

print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

try:
    choice = int(input("Choose an operation (1/2/3/4): "))
    if choice not in [1, 2, 3, 4]:
        print("Invalid choice! Please select a valid option.")
    else:
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
except ValueError:
    print("Invalid input! Please enter numbers only.")

