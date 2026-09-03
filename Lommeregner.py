def operationFunction():

    operation = input()

    if operation == "1":
        num1 = float(input("Skriv dit tal: "))
        num2 = float(input("Skriv dit næste tal: "))
        print(num1 + num2)
    elif operation == "2":
        num1 = float((input("Skriv dit tal: ")))
        num2 = float(input("Skriv dit næste tal: "))
        print(num1 - num2)
    elif operation == "3":
        num1 = float((input("Skriv dit tal: ")))
        num2 = float(input("Skriv dit næste tal: "))
        print(num1 * num2)
    elif operation == "4":
        num1 = float((input("Skriv dit tal: ")))
        num2 = float(input("Skriv dit næste tal: "))
        print(num1 / num2)
    else:
        operation = "-1"
        while operation == "-1":
            print("Invalid input")

print("Vælg hvad du vil udregne: ")
print("1. for at pludse")
print("2. for at minus")
print("3. for at gange")
print("4. for at dividere")

operationActive = True

if operationActive == True:
    operationFunction()