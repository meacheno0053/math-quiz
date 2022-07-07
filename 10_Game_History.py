game_summary = []

rounds_lost = 0
rounds_won = 0
rounds_played =5

for item in range (0,5):
    result = input("choose result: ")

    outcome = "Rounds {}: {}".format(item, result)

    if result == "Lost":
        rounds_lost += 1
    elif result == "Won":
        rounds_won += 1

    game_summary.append(outcome)

rounds_won = rounds_played - rounds_lost


percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100

print()
print("**** Game History ****")
for game in game_summary:
    print(game)

print()



print("Win: {}, ({:.0f}%) \nLoss: {}"
     "({:.0f}%)".format (rounds_won,
                         rounds_won,
                         rounds_lost,
                        rounds_lost.
                        Rounds_won))