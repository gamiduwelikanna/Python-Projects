print("Welcome to the Quiz Game!")
playing = input("Do you want to play? (yes/no): ")

if playing != "yes":
    quit()

print("Great! Let's start the game.")

answer = input("What is the shorten form for Central Processing Unit? ")
if answer=='CPU':
    print("Your answer is correct!")