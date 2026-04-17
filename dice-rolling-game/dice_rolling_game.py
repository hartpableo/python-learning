# Roll the dice?
# if "y"
    # return 2 random numbers (1 - 6 each)
    # prompt question again
# else if "n"
    # "Good bye"
    # terminate
# else
    # "y or n only"
    # prompt question again
    
import sys, random

num_of_dice = 2

# Set the number of dice
while True:
    set_num_of_dice = input("How many dice do you want to roll? ")
    if set_num_of_dice.isdigit() == False or int(set_num_of_dice) <= 0:
        print("That is not a valid number of dice. Try again!")
    else:
        num_of_dice = int(set_num_of_dice)
        break

# Roll the dice
yes_values = ["y", "yes", "sure", "ok", "okay"]
no_values = ["n", "no", "nope", "nah"]

while True:
    roll = input("Roll the dice? ").lower().strip()
    if roll in yes_values:
        print("(" + str(random.randint(1, 6)) + ", " + str(random.randint(1, 6)) + ")")
    elif roll in no_values:
        print("Okay. Good bye!")
        break;
    else:
        print("That is not a valid answer.")