import math

def add(x, y):
    input("Choose two numbers to add together: ")
    return x + y

def subtract(x, y):
    input("Choose two numbers to subtract together: ")
    return x - y

def multiply(x, y):
    input("Choose two numbers to multiply together: ")
    return x * y

def divide(x, y):
    input("Choose two numbers to divide together: ")
    return x / y

def square(x):
    input("Choose a number to square: ")
    return x * x

def cube(x):
    input("Choose a number to cube: ")
    return x * x * x

def sqrt(x):
    input("Choose a number to make a square root of: ")
    return math.sqrt(x)

def cbrt(x):
    input("Choose a number to make a cubic root of: ")
    return math.cbrt(x)

def menu():
    while True:
        try:
            print("Welcome to Calculator 1.0\nPlease choose one of the following options:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Square\n6. Cube\n7. Square Root\n8. Cubic Root\Press Q to Exit\n ")
            choice = input("> ")
            if choice == "1":
                add(x, y)
            elif choice == "2":
                subtract(x, y)
            elif choice == "3":
                multiply()
            elif choice == "4":
                divide()
            elif choice == "5":
                square()
            elif choice == "6":
                cube()
            elif choice == "7":
                sqrt()
            elif choice == "8":
                cbrt()
        except ValueError:
            print("Human error, wrong value typed into console.")
            continue

menu()