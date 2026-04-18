import random

choices = ["ROCK", "PAPER", "SCISSORS"]
winning_choices_map = {
    "ROCK": "SCISSORS",
    "PAPER": "ROCK",
    "SCISSORS": "PAPER"
}

human_score = 0
machine_score = 0
    
while True:    
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
        human_score += 1
    else:
        print("You Lose!")
        machine_score += 1
        
    print("Scores: You: " + str(human_score) + "  |  " + "Me: " + str(machine_score))
    print("")