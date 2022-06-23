# Math Quiz scoring system

# Rounds won will be calculated (total - lost)
rounds_played = 0 
rounds_lost = 0

# Results for testing purposes
test_results = ["won", "won", "lost", "lost", "lost"]

# Play game
for item in test_results:
    rounds_played += 1 

    #generate computer choice

    result = item

    if result == "Lost":
        result = "You lost"
        rounds_lost += 1 

# Quick calculations (stats)
rounds_won = rounds_played - rounds_lost

# End of game statements
print()
print('^^^^ End Game Summary ^^^^')
print("Won: {} \t|\t Lost: {} \t|\t" .format(rounds_won, rounds_lost))
print()
print("Thanks For Playing")