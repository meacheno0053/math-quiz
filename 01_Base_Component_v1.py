import random

# Functions go here 
def yes_no (question):
    valid = False
    while not valid:
        response = input(question).lower()

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

# Decoration
def statement_generator(statement, decoration, style):

    sides = decoration * 0

    statement = "{} {} {} ".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    if style == 3:

        print(top_bottom)
        print(statement)
        print(top_bottom)
    else:
        print(statement)

    return ""

# Main routine
statement_generator("^^^ WELCOME TO THE MATH QUIZ ^^^", "^", 3)
print()
played_before = yes_no("?? Have You Played Before ?? ")
print
if played_before ==  "no":
    instructions
print()


# Quick calculations (stats)
rounds_won = rounds_played - rounds_lost

# End of game statements
print()
print('^^^^ End Game Summary ^^^^')
print("Won: {} \t|\t Lost: {} \t|\t" .format(rounds_won, rounds_lost))
print()
print("Thanks For Playing")