import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    print("Welcome to the Dice Game!")
    player_score = 0
    computer_score = 0

    while True:
        print("Your turn. Roll the dice? (yes/no)")
        roll = input()

        if roll == "yes":
            player_roll = roll_dice()
            print("You rolled a", player_roll)
            player_score += player_roll

            computer_roll = roll_dice()
            print("Computer rolled a", computer_roll)
            computer_score += computer_roll

            print("Your score:", player_score)
            print("Computer score:", computer_score)
        elif roll == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    
    if player_score > computer_score:
        print("You win! Congratulations.")
    elif player_score == computer_score:
        print("It's a tie.")
    else:
        print("You lose. Better luck next time.")

play_game()