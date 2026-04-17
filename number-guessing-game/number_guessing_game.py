# Ask for a number range
# Save a number between the range in memory
# Loop: While still not correct answer is given
    # if correct answer is given, print success message and prompt to play again
    # if play again, restart
    # if wrong answer given, print "wrong" message and continue with guess
    
import random

# TODO: "Play again" functionality must start from the very start: setting range

# Minimum number in the range
while True:
    range_min = input("Set the minimum number in the range: ")
    if range_min.isdigit():
        range_min = int(range_min)
        break
    print("That is not a valid value. Try again!")
    
# Maximum number in the range
while True:
    range_max = input("Set the maximum number in the range: ")
    if range_max.isdigit() == False:
        print("That is not a valid value. Try again!")
    range_max = int(range_max)
    if range_max < range_min:
        print("Maximum number must be GREATER THAN the minimum number")
    else:
        break
        
# Select a hidden number from the range and save to memory
hidden_num = random.randint(range_min, range_max)

# Let's play
playing = True
while playing:
    answer = input("Guess the number: ")
    if answer.isdigit() == False:
        print("That is not a valid value. Try again!")
        continue
    answer = int(answer)
    if answer < range_min or answer > range_max:
        print("That number is out of the set range!")
        print("Minimum: " + str(range_min))
        print("Maximum: " + str(range_max))
    elif answer < hidden_num:
        print("Go higher")
    elif answer > hidden_num:
        print("Go lower")
    else:
        print("Congratulations! You got the correct answer: " + str(hidden_num))
        
        # Prompt to play again
        while True:
            yes_values = ["y", "yes", "sure", "ok", "okay", "go"]
            no_values = ["n", "no", "nope", "nah"]
            play_again = input("Do you want to play again? (y/n) ").lower().strip()
            if play_again in ["y", "yes", "sure", "ok", "okay", "go"]:
                break
            elif play_again in ["n", "no", "nope", "nah"]:
                print("Thanks for playing!")
                playing = False
                break
            else:
                print("That is not a valid answer. Try again!")