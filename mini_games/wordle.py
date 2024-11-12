# mini_games/wordle.py

import random
from utilities import clear_screen

def play_wordle():
    # Load words from a text file containing possible words for the Wordle game.
    with open('words_5.txt', 'r') as file:
        words = [line.strip() for line in file.readlines()]

    while True:  # Keep playing until the player successfully completes the game
        random_word = random.choice(words)
        splitted_random_word = list(random_word)
        chances = 0
        max_chances = 5
        true_check = False

        print("****** WORDLE ******")

        while chances < max_chances and not true_check:
            user_input = input("Guess(Enter a 5 letters word in lowercase): ")
            splitted_input = list(user_input)

            if len(splitted_input) != 5:
                print("Enter a word with only 5 letters")
                continue

            true_check_counter = 0
            for i in range(len(splitted_input)):
                if splitted_input[i] == splitted_random_word[i]:
                    print(f"\033[92m{splitted_input[i]}\033[0m", end=" ")  # Green for correct letter in correct position
                    true_check_counter += 1
                elif splitted_input[i] in splitted_random_word:
                    print(f"\033[93m{splitted_input[i]}\033[0m", end=" ")  # Yellow for correct letter in wrong position
                else:
                    print(splitted_input[i], end=" ")  # Normal for incorrect letters
            print()

            if true_check_counter == 5:
                true_check = True
            else:
                chances += 1

        if true_check:
            print("You guessed it correct!")
            input("Press Enter to return to the maze...")
            break  # Exit the loop if the player wins
        else:
            print(f"You couldn't guess the word! It was {random_word}")
            input("Press Enter to try again...")
            clear_screen()  # Clear the screen before restarting
