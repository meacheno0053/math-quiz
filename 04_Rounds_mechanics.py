# Round numbers for each individual equation


def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <Enter> " \
                    "or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response <1:
                    print(round_error)
                    continue
           
            except ValueError:
                print(round_error)
                continue

        return response

        
rounds_played = 0
choose_instruction = "Please answer the question"

# Ask user for number of rounds, or <enter> for infinate
rounds = check_rounds()

end_game = "no"
while end_game == "no":

#rounds heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played +1)
    print(heading) 
    choose = input("{} or 'xxx' to end:".format(choose_instruction))
    if choose == 'xxx':
       break
    else:
        heading = "round {} of {}".format(rounds_played + 1, rounds)
        print(heading)
        choose = input(choose_instruction)
        if rounds_played == rounds - 1:
            end_game = "yes"

print("You chose {}".format(choose))

rounds_played +=1