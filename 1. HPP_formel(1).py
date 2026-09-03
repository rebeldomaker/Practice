userInput = input("\nSkriv h for helhed \nSkriv pt for procenttal \nSkriv pd for procentdel \n \nVælg hvad du vil udregne: ")

def helhedFormel():
    try: # ???
        procentDel = float(input("Skriv Procent del: ")) # in python, you read the code backwards, in this case, user inputs, in this case, string. the string is then converted into a float number
        procentTal = float(input("Skriv Procent tal: "))
        print("Helheden er = ", procentDel * 100 / procentTal)
    except ValueError:
        print("Du skal skrive et tal, prøv igen")



def procentTalFormel():
    try:
        procentDel = float(input("Skriv procendel: "))
        helhed = float(input("Skriv helhed: "))
        print("Procenttallet er = ", procentDel / helhed * 100)
    except:
        print("Du skal skrive et tal, prøv igen")

# Udregner hvad procentdelen er. Procentdel er
def procentDelFormel():
    try:
        procentTal = float(input("Skriv procenttallet : "))
        helhed = float(input("Skriv helhed: "))
        print("Procentdelen er = ", procentTal * helhed / 100)
    except:
     print("Du skal skrive et tal, prøv igen")

while True:
    userInput = input("\nSkriv h for helhed\nSkriv pt for procenttal\nSkriv pd for procentdel\nSkriv q for at afslutte\n\nVælg hvad du vil udregne: ").lower()

    if userInput == "h":
        helhedFormel()
    elif userInput == "pt":
        procentTalFormel()
    elif userInput == "pd":
        procentDelFormel()
    elif userInput == "q":
        print("farvel")
        break
    else:
        print("Ugyldift valg, prøv igen.")