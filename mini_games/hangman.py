# mini_games/hangman.py

import random
from utilities import clear_screen

HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

# Load words from words_5.txt file
with open('words_10.txt', 'r') as file:
    words = [line.strip() for line in file.readlines()]

def get_random_word(word_list):
    """Selects a random word from the given list of words."""
    return random.choice(word_list)

def display_board(missed_letters, correct_letters, secret_word):
    """Displays the current game board with missed and correctly guessed letters."""
    print(HANGMAN_PICS[len(missed_letters)])
    print()
    print(f"Missed letters: {' '.join(missed_letters)}")
    blanks = ['_' if letter not in correct_letters else letter for letter in secret_word]
    print(" ".join(blanks))
    print()  # Add a blank line for spacing

def get_guess(already_guessed):
    """Prompts the player to guess a letter and validates the input."""
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Choose again.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a LETTER.")
        else:
            return guess

def play_hangman():
    """Main function to play the Hangman game."""
    print("H A N G M A N")
    missed_letters = ""
    correct_letters = ""
    secret_word = get_random_word(words)
    game_is_done = False

    while True:
        clear_screen()  # Clear the screen each time to update in place
        display_board(missed_letters, correct_letters, secret_word)
        
        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters += guess

            # Check if the player has guessed all letters
            if all(letter in correct_letters for letter in secret_word):
                clear_screen()
                display_board(missed_letters, correct_letters, secret_word)
                print(f'Yes! The secret word is "{secret_word}"! You have won!')
                game_is_done = True
        else:
            missed_letters += guess

            # Check if the player has run out of guesses
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                clear_screen()
                display_board(missed_letters, correct_letters, secret_word)
                print(f'You have run out of guesses! The word was "{secret_word}".')
                input("Press Enter to try again...")
                return play_hangman()  # Restart the Hangman game if failed

        # Exit the game if completed
        if game_is_done:
            input("Congratulations! Press Enter to return to the maze...")
            break
