def user_input(): # creates an if loop to have programming continue running over and over again, asking the user to choose number after number to input into the program
    x = input("Write a number: ")
    while True: # ignore this part, was an experiment and us pointless line of code
        if x.isdigit():  # This checks if the input string contains only digits
            return int(x)
        else: # if it checks and finds that the input the user gave was not a digit, then they get an error
            print("Error: Please enter a valid number! ")
            return None # this line of code is relevant for the rest of the code that comes after it, and to make the error code handling function work correctly, WIP though

def error_handling(number):
    if number is not None: # while if number == not None:
        return number # keep looping, as long as the user does not turn the variable into a value of None, which happens if the user inputs anything other than digits
    else:
        return "Invalid input! " # anything else entered that is not what the program expects, that is, digits/numbers, then the user is warned that their input was wrong

# Run the program
while True: # loops so that the program does not end and exit after running it just once
    result = user_input() # keep running the main function, which is the user_input function
    print(error_handling(result)) # prevents the program from crashing by checking if the value the user has inputed is what python expects to see