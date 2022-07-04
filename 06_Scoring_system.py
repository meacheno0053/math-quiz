# Math Quiz scoring system

# Rounds won will be calculated (total - lost)
rounds_played = 0 
rounds_lost = 0
rounds_won = 0

# Results for testing purposes
test_results = ["won", "won", "lost", "lost", "lost"]

# Play game
for item in test_results:
    rounds_played += 1 

    #generate computer choice

    result = item

    if result == "lost":
        result = "You lost"
        rounds_lost += 1 

# Quick calculations (stats)
rounds_won = rounds_played - rounds_lost

# End of game statements
print()
print('^^^^ End Game Summary ^^^^')
print("Won: {} \t|\t Lost: {} \t|\t Played: {}" .format(rounds_won, rounds_lost, rounds_played))
print()
print("Thanks For Playing")