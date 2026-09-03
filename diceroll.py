import random

def diceroll():
    dice = random.randint(1, 6) # from the random library, you use the randint command, and choose its range to be between 1 to 6 that it is able to randomly choose from a pool of numbers, nothing may exceed this range when the random library is choosing a random integer number
    if dice == 1:
        print("You have rolled: 1 ")
    elif (dice > 1 and dice < 6) or dice == 5: # the roll is more than 1 but equal to or less than 5, print that number. Check if the roll is more than 1 but equal to or less than 5
        print(f"You have rolled: {dice}")
    else:
        print("You have rolled a 6, the highest amount possible! ")

print("press enter ")
input()# when enter key is pressed, proceed to this function:
diceroll()