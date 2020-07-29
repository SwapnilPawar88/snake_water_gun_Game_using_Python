# Sanke-Water-Gun Game By Swapnil Pawar
import random

chance = 10
computer_points = 0
user_points = 0
draw = 0

# list initialise with name lst
lst = ["Sanke", "Water", "Gun"]

# Enter Input
print("enter S for Sanke")
print("enter W for Water")
print("enter G for Gun")

# loop iterate until chance is equal to 10
while chance >= 1:
    if chance == 5:
        print(f"Warning You have {chance} Chance Left")

    computer = random.choice(lst)
    user = input().capitalize()
    if user == 'S':
        chance -= 1
        # print("You Have Chance remain ", chance)
        if computer == "Sanke":
            print("this is Draw...")
            draw += 1
            chance += 1
            print("You Have Chance remain", chance)
            continue
        elif computer == "Water":
            print("You Win !")
            user_points += 1
            continue
        else:
            print("Computer Win !")
            computer_points += 1
            continue
    elif user == 'W':
        chance -= 1
        # print("You Have Chance remain ", chance)
        if computer == "Sanke":
            print("Computer win ")
            computer_points += 1
            continue
        elif computer == "Water":
            print("This is Draw !")
            draw += 1
            chance += 1
            print("You Have Chance remain", chance)
            continue
        else:
            print("You Win !")
            user_points += 1
            continue
    elif user == 'G':
        chance -= 1
        # print("You Have Chance remain ", chance)
        if computer == "Sanke":
            print("You win !")
            user_points += 1
            continue
        elif computer == "Water":
            print("Computer Win")
            computer_points += 1
            continue
        else:
            print("This is Draw")
            draw += 1
            chance += 1
            print("You Have Chance remain",chance)
            continue
    else:
        chance -= 1
        print("Wrong Input Select S or W or G ")
        if chance == 10:
            pass
        else:
            chance += 1
            print("Chance remain ", chance)

# Game End Here prints points
print("Game End !")
print("Your Points are ", user_points)
print("Computer Points ", computer_points)
print("Draw Points Are ", draw)
if user_points > computer_points:
    print("You Win !")
elif computer_points > user_points:
    print("Computer Win !")
else:
    print("Game is Draw ! ")
