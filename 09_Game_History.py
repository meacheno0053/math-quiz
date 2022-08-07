game_summary = []

rounds_lost = 0
rounds_played =0

for item in range (1,9):
    result = input("choose result: ")

    outcome = "Rounds {}: {}".format(item, result)

    if result == "Lost":
        rounds_lost += 1

    game_summary.append(outcome)

rounds_won = rounds_played - rounds_lost


percent_win = rounds_won / rounds_played * 100
percent_lost = rounds_lost / rounds_played * 100

print()
print("**** Game History ****")
for game in game_summary:
    print(game)

print()

# displays game stats with % values to the nearest whole number
print("**** GAME STATISTICS ****")
print("Win: {}, ({:.0f}%) \nLoss: {}"
     "({:.0f}%)".format (rounds_won,
                         percent_win,
                         rounds_lost,
                         percent_lost))