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

yes_values = ["y", "yes", "sure", "ok", "okay"]
no_values = ["n", "no", "nope", "nah"]

while True:
    roll = input("Roll the dice? ").lower().strip()
    if roll in yes_values:
        print("(" + str(random.randint(1, 6)) + ", " + str(random.randint(1, 6)) + ")")
    elif roll in no_values:
        print("Okay. Good bye!")
        sys.exit()
    else:
        print("\"y\" or \"n\" values only acceptable")