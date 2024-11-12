# player.py

from mini_games.tic_tac_toe import play_tic_tac_toe
from mini_games.hangman import play_hangman
from mini_games.wordle import play_wordle
from mini_games.trivia import play_trivia
from mini_games.math_puzzle import play_math_puzzle
from mini_games.number_guessing import play_number_guessing
from mini_games.riddle import play_riddle_game
from mini_games._2048 import play_2048

from utilities import clear_screen, get_key, load_logo
import os
import sys

# Symbols used in the maze
WALL = "▀▁▂▃▄▅▆▇█▉▊▋▌▍▎▏▐▔▕❘❙❚"
SPECIAL_ITEM_2048 = "░"
SPECIAL_ITEM_TICTACTOE = "▒"
SPECIAL_ITEM_WORDLE = "▓"
SPECIAL_ITEM_TRIVIA = "¤"
SPECIAL_ITEM_MATH_PUZZLE = "♦"
SPECIAL_ITEM_HANGMAN = "¶" 
SPECIAL_ITEM_NUMBER_GUESSING = "?"
SPECIAL_ITEM_RIDDLE = "@"

PATH = " "
EXIT = "E"
PLAYER = "P"
logo = load_logo()  # Load the logo from logo.txt

DIRECTIONS = {
    "w": (-1, 0),  # Up
    "s": (1, 0),   # Down
    "a": (0, -1),  # Left
    "d": (0, 1)    # Right
}

def play_maze(maze):
    player_pos = (1, 1)
    exit_pos = locate_exit(maze)

    while True:
        clear_screen()
        from maze import display_maze
        display_maze(maze, player_pos)
        
        if player_pos == exit_pos:
            print("!!Congratulations! You reached the exit!!")
            print("!!NEW LEVEL AVAILABLE!!")
            input("Press ENTER to return to the main menu! Thanks for playing!")
            break

        move = get_key().lower()
        
        # Check for pause key
        if move == 'p':
            pause_menu()  # Call the pause menu function when 'p' is pressed
            continue  # Resume game after pause

        if move in DIRECTIONS:
            dy, dx = DIRECTIONS[move]
            new_y, new_x = player_pos[0] + dy, player_pos[1] + dx

            if (0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze) and 
                maze[new_y][new_x] not in WALL):

                player_pos = handle_special_items(maze, new_y, new_x)
                if player_pos is None:
                    return  # Exits game loop if a mini-game requires


def locate_exit(maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == EXIT:
                return (y, x)
    return None

def handle_special_items(maze, new_y, new_x):
    cell = maze[new_y][new_x]
    
    if cell == SPECIAL_ITEM_2048:
        print("You found a special door! To proceed, you need to create a '64' in a game of 2048.")
        input("Press Enter to start the game of 2048...")
        play_2048()
        maze[new_y][new_x] = PATH  # Clear the item after playing
    elif cell == SPECIAL_ITEM_TICTACTOE:
        print("You found a special door! To proceed, you need to tie in a game of Tic Tac Toe.")
        input("Press Enter to start the game of Tic Tac Toe...")
        play_tic_tac_toe()
        maze[new_y][new_x] = PATH  # Clear the item after playing
    elif cell == SPECIAL_ITEM_WORDLE:
        print("You found a special door! To proceed, you need to complete a game of Wordle.")
        input("Press Enter to start the game of Wordle...")
        play_wordle()
        maze[new_y][new_x] = PATH  # Clear the item after playing
    elif cell == SPECIAL_ITEM_TRIVIA:
        print("You found a special door! To proceed, you need to answer a trivia question correctly.")
        input("Press Enter to start the trivia game...")
        play_trivia()
        maze[new_y][new_x] = PATH  # Clear the item after playing
    elif cell == SPECIAL_ITEM_MATH_PUZZLE:
        print("You found a special door! To proceed, you need to solve a math puzzle.")
        input("Press Enter to start the math puzzle...")
        play_math_puzzle()
        maze[new_y][new_x] = PATH  # Clear the item after playing
    elif cell == SPECIAL_ITEM_HANGMAN:
        print("You found a special door! To proceed, you need to win a game of Hangman.")
        input("Press Enter to start the Hangman game...")
        play_hangman()
        maze[new_y][new_x] = PATH  # Clear the item after playing
    elif cell == SPECIAL_ITEM_NUMBER_GUESSING:
        print("You found a special door! To proceed, you need to win the Number Guessing Game.")
        input("Press Enter to start the Number Guessing Game...")
        play_number_guessing()
        maze[new_y][new_x] = PATH  # Clear the item after playing
    elif cell == SPECIAL_ITEM_RIDDLE:
        print("You found a special item! To proceed, you need to solve a riddle.")
        input("Press Enter to start the riddle game...")
        play_riddle_game()
        maze[new_y][new_x] = PATH  # Clear the item after playing

    return (new_y, new_x)

def pause_menu():
    while True:
        clear_screen()
        terminal_width = os.get_terminal_size().columns
        for line in logo.splitlines():
            print(line.center(terminal_width))
        print("Game paused.")
        options = ["Continue Game", "Quit Game"]
        selected_index = 0

        while True:
            clear_screen()
            for line in logo.splitlines():
                print(line.center(terminal_width))
            for i, option in enumerate(options):
                if i == selected_index:
                    print(f"✿ ❀ ✿ {option} ✿ ❀ ✿".center(terminal_width))
                else:
                    print(option.center(terminal_width))
            key = get_key().lower()
            if key == "w" and selected_index > 0:
                selected_index -= 1
            elif key == "s" and selected_index < len(options) - 1:
                selected_index += 1
            elif key == "\r" or key == "\n":
                if selected_index == 0:
                    return  # Continue game
                elif selected_index == 1:
                    sys.exit()  # Quit game
