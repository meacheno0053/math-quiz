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
    display = instructions()
print()

def check_rounds():
  while True:
    response = input ("How many rounds? : ")
    
    round_error = "Please type either <Enter>, xxx " \
    "or an integer that is more than 0"
    if response != "":
        try:
            response = int(response)
            
            if response <1:
                print (round_error)
                continue
            
        except ValueError:
            print(round_error)
            continue
    
    return response


first = random.randint(1, 100)
second = random.randint(1, 100)
answer = first + second

question = "{} + {} = ".format(first, second)
print(question)

run = True
while run :
    user_input = int(input("Enter number: "))
    if user_input == answer:
        print("correct!")
        print("Program continues")
        run = False
    elif user_input < answer:
        print("Incorrect! The correct answer is:", answer)
