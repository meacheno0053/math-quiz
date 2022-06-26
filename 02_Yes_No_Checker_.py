# Ask the user if they have played before
def yes_no (question):
    valid = False
    while not valid:
        response = input("Have you played before?").lower()

        if response == "Yes"or response == "y":
            return "Yes"
        elif response == "No" or response =="n":
            return "No"

        else: 
            print("Please answer Yes / No")

def instructions ():
    print("*** How To Play ***")
    print()
    print("instructions go here")
    print()
    
    return""
