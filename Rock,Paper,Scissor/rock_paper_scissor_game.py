import random

user_wins = 0
computer_wins = 0

print("------------------------------\n")
print("Welcome to Rock, Paper, Scissor Game!")
print("To select Rock select 'r', for Paper select 'p', and for Scissor select 's'.")
print("Enter 'q' to quit thr game\n\n")


options = ['r', 'p', 's']
#a list of the choices that can be made

while True:
    user_input= input("Enter a letter (r/p/s) or 'q' to quit: ").lower()

    if user_input == 'q':
        print("Thank you for playing!\n")
        break

    if user_input not in options:
        print("Invalid input. Please try again.\n")
        continue

    random_number = random.randint(0,2)
    # 0 for rock, 1 for paper, 2 for scissor

    computer_pick = options[random_number]
    print("Computer picked: " + computer_pick + ".\n")

    if user_input == 'r' and computer_pick == 's':
        print("You win!\n")
        user_wins += 1

    elif user_input == 'p' and computer_pick == 'r':
        print("You win!\n")
        user_wins += 1

    elif user_input == 's' and computer_pick == 'p':
        print("You win!\n")
        user_wins += 1
        
    elif user_input == computer_pick:
        print("It's a tie!\n")

    else:
        print("Computer wins!\n")
        computer_wins += 1
    
    print("Your wins: " , user_wins)
    print("Computer wins: " , computer_wins , "\n")
    print("Let's play again!\n")

print("------------------------------\n")
print("Final Scores:"
      "\nYour wins: " ,user_wins ,
      "\nComputer wins: " ,computer_wins ,
      "\n\n------------------------------")
    
