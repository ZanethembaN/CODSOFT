import random
from pyfiglet import Figlet
from colours import *

VALID_CHOICES = ['rock', 'paper', 'scissors']
MOVES = 3


def get_user_choice():
    while True:
        user_choice = input(f"{CYAN}Choose Rock, Paper, or Scissors: {RESET}").lower()
        if user_choice in VALID_CHOICES:
            return user_choice
        else:
            print(f"{RED}{BOLD}Invalid choice. Please choose Rock, Paper, or Scissors.{RESET}")

def get_computer_choice():
    computer_choice_index = random.randint(0, len(VALID_CHOICES)-1)
    computer_choice = VALID_CHOICES[computer_choice_index]
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        result = f"{GREEN}{BOLD}It's a tie!{RESET}"
        winner = 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = f"\n{BG_BRIGHT_GREEN}{BOLD}You win!{RESET}"
        winner = 'user'
    else:
        result = f"\n{BG_BRIGHT_RED}Computer wins!{RESET}"
        winner = 'computer'
    
    return result, winner

def play_game(MOVES):

    # table_label = f"{CYAN}{BOLD}[ROCK/PAPER/SCISSORS]"
    # custom_fig = Figlet(font='')
    # ascii_art = custom_fig.renderText(table_label)
    # ascii_art = f'{CYAN}{BOLD}{ascii_art}{RESET}'
    # print(ascii_art)
    
    user_score = 0
    computer_score = 0

    while MOVES != 0:
        smiley = "\U0001F604"
        print(f"\n{BOLD}Let's play (Rock, Paper, Scissors) YAY!", smiley)
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose {user_choice}.")
        print(f"Computer chose {computer_choice}.")

        result, winner = determine_winner(user_choice, computer_choice)
        print(result)

        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"\n{BOLD}Score - {BOLD}You{RESET}: {user_score}, {BOLD}Computer{RESET}: {computer_score}")

        MOVES -= 1
        play_again()


def play_again():
    while MOVES == 0:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
        else:
            play_game(MOVES)

if __name__ == "__main__":
    play_game(MOVES)
