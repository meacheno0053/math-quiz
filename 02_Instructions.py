def yes_no (question): 
    valid = False
    while not valid: 
        response = input(question).lower()

    if response == "yes" or response == "y": 
        print("You have chose yes")
        return "yes"

    elif response == "no" or response == "n":
        return "no"

    else:
        print("Please answer yes or no")

def instructions ():
    print("*** How To Play ***")
    print()
    print("instructions go here")
    print()
    return""

played_before = yes_no ("Have you played before")

if played_before == "no":
    print()

print("program continues")