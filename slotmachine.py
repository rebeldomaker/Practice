import random

def slot_roll():
    while True:
        items = ["oran-berry", "pokeball", "everstone"]
        slot1 = random.choice(items) #
        slot2 = random.choice(items)
        slot3 = random.choice(items)
        slot_machine = slot1, slot2, slot3
        print(slot_machine)
        print("press enter to reroll ")
        input() # awaiting input
        continue
#    if dice == 1:
#        print("You have rolled: 1 ")
#    elif (dice > 1 and dice < 6) or dice == 5: # the roll is more than 1 but equal to or less than 5, print that number. Check if the roll is more than 1 but equal to or less than 5
#        print(f"You have rolled: {dice}")
#    else:
#        print("You have rolled a 6, the highest amount possible! ")

print("press enter ")
input()# when enter key is pressed, proceed to this function:
slot_roll()
