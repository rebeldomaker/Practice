import time

def countdown():
    try:
        mins = input("How many minutes? ")
        mins = int(mins)
        
        if mins <= 0:
            print("Please enter a valid number of minutes")
            return
            
        for i in range(mins, 0, -1):
            print(f"{i} minutes remaining")
            time.sleep(60)
        print("Time's up!")
        
    except ValueError:
        print("Please enter a valid number")

countdown()