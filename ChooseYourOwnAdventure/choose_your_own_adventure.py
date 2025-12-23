name = input("Type your name: ")
print("Welcome", name, "to this adventure!")
print("You wake up in a mysterious forest with no memory of how you got here.\n")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()

    if answer == "swim":
        answer = input("You start swimming. The current is strong! Do you fight the current or let it carry you (fight/let)? ").lower()
        
        if answer == "fight":
            print("You fight against the current but get tired and drown. Game over.")
        elif answer == "let":
            answer = input("The current carries you downstream to a waterfall! Do you grab a rock or go over (grab/over)? ").lower()
            
            if answer == "grab":
                print("You grab a rock and pull yourself to shore. You find a treasure chest! You WIN!")
            elif answer == "over":
                print("You go over the waterfall and fall to your doom. Game over.")
            else:
                print('Not a valid option. You lose.')
        else:
            print('Not a valid option. You lose.')
            
    elif answer == "walk":
        answer = input("You walk along the river and find a cave. Do you enter the cave or keep walking (enter/walk)? ").lower()
        
        if answer == "enter":
            answer = input("Inside the cave you see two tunnels: one has light coming from it, one is dark. Which do you choose (light/dark)? ").lower()
            
            if answer == "light":
                print("You follow the light and find an exit leading to a village. The villagers welcome you as a hero! You WIN!")
            elif answer == "dark":
                answer = input("You venture into darkness and hear growling. Do you run back or continue (run/continue)? ").lower()
                
                if answer == "run":
                    print("You run back but trip and fall. A bear catches you. Game over.")
                elif answer == "continue":
                    print("You continue and find a sleeping dragon sitting on a pile of gold. You sneak past and escape with gold! You WIN!")
                else:
                    print('Not a valid option. You lose.')
            else:
                print('Not a valid option. You lose.')
                
        elif answer == "walk":
            print("You walked for many miles, ran out of water and collapsed. Game over.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()

    if answer == "back":
        answer = input("You head back and find a hidden path. Do you take it (yes/no)? ").lower()
        
        if answer == "yes":
            answer = input("The path leads to an old temple. Do you go inside or camp outside (inside/outside)? ").lower()
            
            if answer == "inside":
                print("Inside you find ancient artifacts and a map to treasure! You WIN!")
            elif answer == "outside":
                print("You camp outside but wolves attack you at night. Game over.")
            else:
                print("Not a valid option. You lose.")
        elif answer == "no":
            print("You wander aimlessly and get lost forever. Game over.")
        else:
            print("Not a valid option. You lose.")
            
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()

        if answer == "yes":
            answer = input("The stranger offers you a potion or a map. Which do you take (potion/map)? ").lower()
            
            if answer == "potion":
                answer = input("The stranger asks if you trust them to drink it now (yes/no)? ").lower()
                
                if answer == "yes":
                    print("The potion gives you magical powers! You become a wizard and WIN!")
                elif answer == "no":
                    print("The stranger gets offended and curses you. Game over.")
                else:
                    print("Not a valid option. You lose.")
                    
            elif answer == "map":
                answer = input("The map shows a treasure location. Do you go alone or ask the stranger to join (alone/join)? ").lower()
                
                if answer == "alone":
                    print("You find the treasure but the stranger was a thief and steals it. Game over.")
                elif answer == "join":
                    print("You and the stranger find the treasure and share it! You WIN!")
                else:
                    print("Not a valid option. You lose.")
            else:
                print("Not a valid option. You lose.")
                
        elif answer == "no":
            answer = input("You ignore the stranger. They follow you. Do you run or confront them (run/confront)? ").lower()
            
            if answer == "run":
                print("You run but fall off a cliff. Game over.")
            elif answer == "confront":
                print("You confront them and they reveal they're a king in disguise. They reward your bravery! You WIN!")
            else:
                print("Not a valid option. You lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")

else:
    print('Not a valid option. You lose.')

print("\nThank you for trying", name)
