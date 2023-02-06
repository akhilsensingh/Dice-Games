import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    print("Welcome to the Dice Game!")
    player1_score = 0
    player2_score = 0

    while True:
        print("Player 1, it's your turn. Roll the dice? (yes/no)")
        roll = input()

        if roll == "yes":
            player1_roll = roll_dice()
            print("You rolled a", player1_roll)
            player1_score += player1_roll
        elif roll == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

        print("Player 2, it's your turn. Roll the dice? (yes/no)")
        roll = input()

        if roll == "yes":
            player2_roll = roll_dice()
            print("You rolled a", player2_roll)
            player2_score += player2_roll
        elif roll == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    
    if player1_score > player2_score:
        print("Player 1 wins! Congratulations.")
    elif player1_score == player2_score:
        print("It's a tie.")
    else:
        print("Player 2 wins! Congratulations.")

play_game()