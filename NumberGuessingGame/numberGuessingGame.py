import random

top_of_range = input("Type a number: ")

if(top_of_range.isdigit()):
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(1,top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please enter a number next time.")
        continue

    print("Number of guesses so far ", guesses)
    if user_guess ==random_number:
        
        print("The number you guessed is correct!")
        break
    elif user_guess > random_number:
        print("You were above the random number. Enter another number.")
    else:
        print("You were below the random number. Enter another number.")

print("You guessed the number in ", guesses, " guesses")