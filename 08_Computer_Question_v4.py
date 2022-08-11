import random
    
    
def intcheck(question, low=None, high=None, exit_code = "xxx"):

    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}".format(low)
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(high)
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

# Ask user for # of rounds, <enter> for infinate mode

rounds = intcheck("How many rounds <enter> for infintite: ", 1, exit_code = "")

end_game = "no"
while end_game =="no":

    # Start of game play loop
    
    
    # Rounds Heading
    print()
    if rounds =="":
        heading = "Continuous Mode: Question {}".format(rounds_played +1)
    else:
        heading = "Question {} of {}".format(rounds_played + 1, rounds)    
    
    print(heading)

    # End game if exit code is typed

    first = random.randint(1, 100)
    second = random.randint(1, 100)
    answer = first + second

    question = "{} + {} = ".format(first, second)
    print(question)
    

    user_input = intcheck("Your answer: ", 1, exit_code = "xxx")

    if user_input == "xxx":
        break
    if user_input == answer:
        print("correct!")
        run = False
    elif user_input < answer:
        print("Incorrect! The correct answer is:", answer)
        if user_input < answer:
            break
    
    rounds_played += 1
    
    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break


# Put end game content here
print()
print("Thank you for playing")