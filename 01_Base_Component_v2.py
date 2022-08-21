import random


# Functions go here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "No"

        else:
            print("Please answer Yes / No")


def instructions():
    print("*** How To Play ***")
    print()
    print("""
***** INSTRUCTIONS *****
    
     -Maths Quiz-

First choose the number of questions you want by typing a number or press <ENTER> for infinate questions (you can always end by typing 'xxx').

These questions are addition only and are ranged from 1-100

Have fun :)
        """)
    print()

    return ""


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
if played_before == "no":
    instructions()
print()


def check_rounds():
    while True:
        response = input("How many rounds? : ")

        round_error = "Please type either <Enter>, xxx " \
        "or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


def intcheck(question, low=None, high=None, exit_code="xxx"):

    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(
                low, high)
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}".format(
                low)
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(
                high)
        else:
            error = "Please enter an integer"

        try:
            response = input(question)

            # check to see if response is the exit code and return it
            if response == exit_code:
                return response

            # change the response into an integer
            else:
                response = int(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue

            else:
                return response

        except ValueError:
            print("Please enter an integer")
            continue


# Main routine goes here...

rounds_played = 0
rounds_lost = 0
rounds_won = 0

# Ask user for # of rounds, <enter> for infinate mode

rounds = intcheck("How many rounds <enter> for infintite: ", 1, exit_code="")

end_game = "no"
while end_game == "no":

    # Start of game play loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Question {}".format(rounds_played + 1)
    else:
        heading = "Question {} of {}".format(rounds_played + 1, rounds)

    print(heading)

    # End game if exit code is typed

    first = random.randint(1, 100)
    second = random.randint(1, 100)
    answer = first + second

    question = "{} + {} = ".format(first, second)
    print(question)

    user_input = intcheck("Your answer: ", 1, exit_code="xxx")

    if user_input == "xxx":
        break
    if user_input == answer:
        print("correct!")
        run = False
    elif user_input < answer:
        print("Incorrect! The correct answer is:", answer)

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

rounds_won = rounds_played -rounds_lost

print()
print('^^^^ End Game Summary ^^^^')
print("Won: {} \t|\t Lost: {} \t|\t Played: {}".format(rounds_won, rounds_lost,
                                                       rounds_played))
print()
print("Thanks For Playing")
