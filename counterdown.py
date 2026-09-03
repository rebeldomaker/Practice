import time
import os

number = 60

def daugyba():
    pass

def beep():
    pass

while number > 0:
    for i in range(number):
        number -= 1
        print(number)
        time.sleep(1)

        if number == 20:
            print("--->", number)

        elif number == 15:
            print("--->", number)

        elif number == 10:
            print("--->", number)

        elif number == 5:
            print("--->", number)

    if number == 0:
        time.sleep(1)
        print("Blast off!")
