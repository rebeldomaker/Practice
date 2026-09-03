def main():
    x = input("type in a number to check if it is an odd or even number ")
    if not x.isdigit():
        print("error, non-number detected!\n")
    elif int(x) % 2 == 0:
        print(f"{x} is even.\n")
    else:
        print(f"{x} is odd.\n")

while True:
    main()
