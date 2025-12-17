print("Welcome to the Quiz Game!")
playing = input("Do you want to play? (yes/no): ")

if playing != "yes":
    quit()

print("Great! Let's start the game.")

answer = input("What is the shorten form for Central Processing Unit? ")
if answer=='CPU':
    print("Your answer is correct!")
else:
    print("Your answer is incorrect. The correct answer is CPU.")

answer = input("What is the shorten form for Read Only Memory? ")
if answer=='ROM':
    print("Your answer is correct!")
else:
    print("Your answer is incorrect. The correct answer is ROM.")

answer = input("What is the shorten form for Graphics Processing Unit? ")
if answer=='GPU':
    print("Your answer is correct!")
else:
    print("Your answer is incorrect. The correct answer is GPU.")

print("Thanks for playing the Quiz Game!")
