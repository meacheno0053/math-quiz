# Ask the user if they have played before
def yes_no (question):
    valid = False
    while not valid:
        response = input("Have you played before?").lower()

        if response == "yes"or response == "y":
            return "yes"
        elif response == "no" or response =="n":
            return "no"

        else: 
            print("Please answer Yes / No")

def instructions ():
    print("*** How To Play ***")
    print()
    print("instructions go here")
    print()
    
    return""


for item in range(0,6):
    ask = yes_no("Do you want instructions?")
    print("You chose", ask)