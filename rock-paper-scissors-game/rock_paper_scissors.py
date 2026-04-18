import random

winning_choices_map = {
    "ROCK": "SCISSORS",
    "PAPER": "ROCK",
    "SCISSORS": "PAPER"
}

while True:
    choices = ["ROCK", "PAPER", "SCISSORS"]
    machine_choice = random.choice(choices)
    human_choice = input("Rock, paper, or scissors? (rock/paper/scissors/exit) ").upper().strip()

    if human_choice == "EXIT":
        print("Thanks for playing!")
        break
    if human_choice not in choices:
        print("That is not a valid value. Try again!")
        continue
    
    print("")
    print("You: " + human_choice + "  |  " + "Me: " + machine_choice)
    print("")
    
    if human_choice == machine_choice:
        print("It's a tie!")
    elif winning_choices_map.get(human_choice) == machine_choice:
        print("You win!")
    else:
        print("You Lose!")