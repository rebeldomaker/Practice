def main(user_input): # convert LT grades (numbers 1 - 10) US grades (F - A grading)
    try: # commonly used in functions
        if user_input in (9, 10): # in ranges 9 to 10, say a more conventional example can be: in ranges 4 to 10, anything between those two numbers is what the program will pull out or put inside of a variable. the if statement also begins a loop
            print("Your grade is A.") # think of this as a sort of dictionary book of definitions
        elif user_input in (7, 8): # if x then do y. else if z then do q, as an analogy to explain the elif code lines in this context
            print("Your grade is B.")
        elif user_input in (5, 6):
            print("Your grade is C.")
        elif user_input == 4:
            print("Your grade is D.")
        elif user_input == 3:
            print("Your grade is E.")
        elif user_input in (1, 2):
            print("Your grade is F.")
        else: # user has input something that was not expected from the program, something it was asking for were valid numbers instead of letters, for example
            print("Hey retard, enter a valid number. ")
    except ValueError: # error handling to prevent aggressive crashes
        print("Great job, retard. You've caused an error. You're meant to type in a NUMBER! ")

print("This program converts LT grading system (1 - 10) into US style F - A grading system. \nType in numbers, receive the American equivalent")
user_input = int(input("What grade did you receive (1-10)? ")) # user gets prompted an interactive question, this is where now they can type and enter a number. it is then converted into an integer number.
while True: # continues the loop
    try:
        user_input == int # python asks itself, is this an integer? if yes, then proceed to run the main() function that was defined earlier in this script
        main()
    finally: # a simple way to end and exit the program once the user got their intended purpose of the program, aka, conversion from numbers to letters/LT to US grade is complete
        break