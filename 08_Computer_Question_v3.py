import random
    
    
def check_rounds():
  while True:
    response = input ("How many Questions? : ")
    
    round_error = "Please type either <Enter>, xxx " \
    "or an integer that is more than 0"
    if response != "":
        try:
            response = int(response)
            
            if response <1:
                print (round_error)
                continue
                
                if response >20:
                    print(round_error)
                    continue

        except ValueError:
            print(round_error)
            continue
    
    return response


# Main routine goes here...

rounds_played = 0 

# Ask user for # of rounds, <enter> for infinate mode

rounds = check_rounds(exit_code = 'xxx')

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
    
    run = True
    while run :
        user_input = int(input("Your answer: "))
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
    
    if user_input == "xxx":
        break

# Put end game content here
print()
print("Thank you for playing")