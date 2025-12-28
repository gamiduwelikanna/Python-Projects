import random

def roll():
    min = 1
    max = 6
    roll = random.randint(min,max)

    return roll

value = roll()
print(value)
print("Welcome to the PIG Game!")
print("The objective of the game is to be the first player to reach 50 points.")


while True:
    players = input("Enter the number of players (2-6): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <=6:
            break

        else:
            print("Invalid number of players. Please enter a number between 2 and 6.")
        
    else:
        print("Try Again")

max_scores = 50
player_scores = [0 for i in range(players)]


while max(player_scores) < max_scores:
    for id in range(players):
        print("\nPlayer number", id+1, "- Your total score is", player_scores[id])
        current_score = 0

        while True:
            choice = input("Enter 'r' to roll or 'q' to quit this turn: ")
            if choice.lower() == 'q':
                print("Player", id+1, "has ended their turn.")
                break
            elif choice.lower() != 'r':
                print("Invalid choice. Please enter 'r' or 'q'.")
                continue
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Your turn is over and you lose all points for this turn.")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a", value)
                print("Your current turn score is", current_score)
                
                # Check if player has won
                if player_scores[id] + current_score >= max_scores:
                    print("🎉 You've reached", player_scores[id] + current_score, "points!")
                    break
                
        player_scores[id] += current_score
        print("Your total score is now", player_scores[id])
        
        if player_scores[id] >= max_scores:
            break

max_score = max(player_scores)
winning_id = player_scores.index(max_score)
print("\nPlayer", winning_id+1, "has won the game with a score of", max_score, "!")



