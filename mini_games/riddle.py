# mini_games/riddle.py

import random
from utilities import clear_screen

def play_riddle_game():
    riddles = [
        {"riddle": "What has to be broken before you can use it?", "answer": "egg"},
        {"riddle": "I’m tall when I’m young, and I’m short when I’m old. What am I?", "answer": "candle"},
        {"riddle": "What month of the year has 28 days?", "answer": "all"}
    ]

    while True:
        selected_riddle = random.choice(riddles)
        attempts = 3
        feedback = ""  # Variable to store feedback for the player

        while attempts > 0:
            clear_screen()
            # Display the riddle and current attempts
            print(f"Riddle: {selected_riddle['riddle']}")
            print(f"You have {attempts} attempts remaining.\n")
            
            # Show feedback (e.g., "Incorrect answer") below the question, if any
            if feedback:
                print(feedback + "\n")
            
            # Ask for the player's answer
            answer = input("Your answer: ").lower()

            # Check if the answer is correct
            if answer == selected_riddle["answer"]:
                clear_screen()
                print("Correct! You solved the riddle.")
                input("Press Enter to return to the maze...")
                return  # Exit the function when the riddle is solved
            else:
                attempts -= 1
                feedback = "Incorrect answer."  # Update feedback to show incorrect answer message

        # If out of attempts, prompt to try a new riddle
        clear_screen()
        print("Out of attempts! Try another riddle.")
        input("Press Enter to try again...")
