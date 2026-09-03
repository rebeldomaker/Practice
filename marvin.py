import random # a built in library that allows you to "roll the dice" so to speak, like you would in DND. this is important so that the program chooses a secret number that the user must guess. this program is inspired by tamagotchi's number guessing game, and will later on get an upgrade to where it loops, and if after 3 tries the guesses are wrong, it will exit the program after telling the user he has lost.

def marvin():
    pass # ??? no idea why, but removing this or erasing the indent causes the program to fail to run, exiting with an error

print("godt gået du får lov til at leve en dag endnu \nDu skal gætte et nummer  fra 1-10") # instructions how to use this program
secret_number = random.randint(0, 10) # the correct answer the user must guess in order to win

while True: # game loop starts here
    try: # ??? try is often used in functions?
        number = int(input("Enter a number: ")) # the user is expected to type a number they will guess with, which then is converted into an interger
        if number == secret_number: # == sign is not a literal = but rather, it is a question python asks itself. this checks to see if the user has guessed the the correct hidden secret number that python randomly chose using the random library that gets imported at the start of the script.
            print("correct, you have won!")
            break # once it is confirmed the user guessed the right hidden secret number, it proceeds to print out a statement they won, and the program ends
        else: # otherwise, if their guess was not the correct number (randomly chosen secret number chosen at the start of the script's launch), they are told they did wrong, and then the game continues to loop until the user guesses correctly
            print("Ej hvor er du dårlig. HA HA HA \nPrøv igen, HA HA")
    except ValueError: # error handling, which tells python if something unexpected was entered, that is not a number, then normally python gets an error and crashes, but instead python is told that an error has occured, and is instructed what to do instead, so as not to simply crash and exit
        print("wtf dude, wrong value... skill issue")