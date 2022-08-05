import random

def check_rounds():
    while True:
        response = input ("How many rounds? : ")
        
        round_error = "Please type either <Enter>, xxx " \
        "or an integer more than 0"
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


# Main routine goes here...

rounds_played = 0 

# Ask user for # of rounds, <enter> for infinate mode

rounds = check_rounds()

print("got to end of function", rounds)

end_game = "no"
while end_game =="no":

  # Start of game play loop

  
  # Rounds Heading
  print()
  if rounds =="":
    heading = "Continuous Mode: Round {}".format(rounds_played +1)
  else:
    heading = "Round {} of {}".format(rounds_played + 1, rounds)    

  # **** rest of loop / game ****

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
        print("Program continues")
        run = False
    elif user_input < answer:
        print("Incorrect! The correct answer is:", answer)

        rounds_played += 1

  # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

    if user_input == "xxx":
        break

# Put end game content here
print()
print("Thank you for playing")