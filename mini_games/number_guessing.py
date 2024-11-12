# mini_games/number_guessing.py

import random
from utilities import clear_screen

def play_number_guessing():
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 7  # Allow 7 attempts
    low, high = 1, 100  # Initialize the range
    
    while attempts > 0:
        clear_screen()
        print("Welcome to the Number Guessing Game!")
        print("You need to guess the number between 1 and 100.")
        print(f"Current range: {low} - {high}")
        print(f"Attempt {8 - attempts}/7")

        try:
            guess = int(input("Enter your guess: "))
            
            if guess == number_to_guess:
                clear_screen()
                print(f"Congratulations! You've guessed the number correctly! It was {number_to_guess}.")
                input("Press Enter to return to the maze...")
                return
            elif guess < number_to_guess:
                low = max(low, guess + 1)  # Update the lower bound of the range
            else:
                high = min(high, guess - 1)  # Update the upper bound of the range
            
            attempts -= 1

        except ValueError:
            print("Please enter a valid number.")

    # If player fails, prompt to try again
    clear_screen()
    print(f"Out of attempts! The correct number was {number_to_guess}.")
    input("Press Enter to try again...")
    play_number_guessing()  # Restart the game if they fail
