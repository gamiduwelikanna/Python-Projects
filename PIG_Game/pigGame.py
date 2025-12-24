import random

def roll():
    min = 1
    max = 6
    roll = random.randint(min,max)

    return roll

value = roll()
print(value)


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

print(players)