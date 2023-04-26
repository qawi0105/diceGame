import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    print("Welcome to the Dice Game!")
    print("You will roll two dice and try to get the highest score.")
    input("Press Enter to begin...")

    # Roll two dice
    dice1 = roll_dice()
    dice2 = roll_dice()

    # Calculate score
    score = dice1 + dice2

    # Print results
    print(f"You rolled a {dice1} and a {dice2}.")
    print(f"Your score is {score}.")

    if score > 7:
        print("Congratulations, you win!")
    else:
        print("Sorry, you lose.")

# Play the game
play_game()
