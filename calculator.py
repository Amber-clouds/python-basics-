calculator.py

# This mini project is a simple calculator that performs basic operations
# using user input and conditional statements.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")
