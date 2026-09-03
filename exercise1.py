import datetime

def namefunc():
    while True:
        name = input("Your name: ")
        if not name.isalpha():
            print("Error, try again! Your name should only contain letters.")
            continue
        return name

def agefunc():
    while True:
        try:
            age = int(input("Your age: "))
            if age < 0:
                print('Error, please enter a valid age! You cannot be below the age of 0!')
                continue
            current_year = datetime.date.today().year
            birth_year = current_year - age
            calc_future = birth_year + 100  # what year will user become 100 years old
            return birth_year, calc_future, age
        except ValueError:
            print("Error, unexpected input. Please enter a valid age!")

# Main program
name = namefunc()
birth_year, calc_future, age = agefunc()

print(f"Greetings, {name}! \nSo if you are {age} years old, then that must mean you were born in {birth_year}! So you would be 100 years old in {calc_future}.")