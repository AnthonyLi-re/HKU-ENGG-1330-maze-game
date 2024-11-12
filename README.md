# Maze Game

Welcome to Maze Game! This project is a text-based maze adventure where players navigate through a maze filled with various mini-games. Each mini-game presents a unique challenge that must be completed to proceed.

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [File Structure](#file-structure)
- [How to Play](#how-to-play)
- [Mini-Games Included](#mini-games-included)
- [Credits](#credits)

## About the Project

Maze Game is built with a modular structure, allowing each mini-game to operate independently. The main maze navigation experience is enhanced with mini-games, providing a mix of puzzles, number games, and word challenges to engage players.

## Features

- **Modular Design**: Each mini-game is contained in a separate file for easy management.
- **Dynamic Interaction**: Games like Hangman and Number Guessing dynamically adjust their display with clear screen updates.
- **Reusable Utilities**: Core utility functions ensure consistency across the project.
- **Classic Games**: Popular games like 2048, Tic Tac Toe, and Hangman are included for varied gameplay.

## File Structure

Here is a complete breakdown of the file structure based on the provided directory layout:

```plaintext
├── main.py                   # Main entry point to launch the game
├── maze.py                   # Maze map file management and handling
├── player.py                 # Handles maze navigation and player interactions
├── utilities.py              # Common helper functions (e.g., screen clearing)
├── logo.txt                  # ASCII art logo displayed on the main and pause screens
├── words_5.txt               # Word list for Wordle game
├── words_10.txt              # Word list for Hangman and Riddle games
├── maps/                     # Contains maze map files
├── mini_games/               # Directory containing individual mini-games
│   ├── _2048.py              # 2048 game logic
│   ├── hangman.py            # Hangman game logic
│   ├── math_puzzle.py        # Math puzzle game logic
│   ├── number_guessing.py    # Number Guessing game logic
│   ├── riddle.py             # Riddle game logic
│   ├── tic_tac_toe.py        # Tic Tac Toe game logic
│   ├── trivia.py             # Trivia game logic
│   └── wordle.py             # Wordle game logic
└── README.md                 # Project documentation
```

## How to Play

1. Launch the game by running `python main.py` in a new terminal.
2. Use the main menu to start navigating the maze.
3. Move with **WASD** keys:
   - **W**: Up
   - **A**: Left
   - **S**: Down
   - **D**: Right
4. When encountering a special door in the maze, complete the mini-game to proceed.

## Mini-Games Included

The following mini-games are included in Maze Game:

- **2048** (`mini_games/_2048.py`): Combine numbers to reach the "64" tile in this modified 2048 game.
- **Hangman** (`mini_games/hangman.py`): Guess the word letter-by-letter before the hangman drawing is complete.
- **Math Puzzle** (`mini_games/math_puzzle.py`): Solve various math puzzles to proceed.
- **Number Guessing** (`mini_games/number_guessing.py`): Guess the correct number within a dynamic range based on your guesses.
- **Riddle Game** (`mini_games/riddle.py`): Solve a riddle within a limited number of attempts.
- **Tic Tac Toe** (`mini_games/tic_tac_toe.py`): Attempt to tie the game against the computer.
- **Trivia** (`mini_games/trivia.py`): Answer general knowledge questions to progress.
- **Wordle** (`mini_games/wordle.py`): Guess the 5-letter word within six attempts, similar to the classic Wordle game.

## File Descriptions

### `main.py`
The main script that launches the game and displays the main menu. It initiates the game loop and handles player input for menu selection.

### `maze.py`
Manages maze map loading and interactions, supporting different maze layouts based on level difficulty.

### `player.py`
Handles the core maze navigation and player interactions. This file checks for special items in the maze and calls mini-game functions when an item is encountered.

### `utilities.py`
Contains common helper functions used throughout the project:
- `clear_screen`: Clears the terminal screen.
- `get_key`: Captures single-character input without needing Enter.

### `logo.txt`
ASCII art logo displayed in the main and pause screens. This file allows you to change the logo independently without modifying code.

### `words_5.txt` and `words_10.txt`
- `words_5.txt`: A list of 5-letter words used in the Wordle game.
- `words_10.txt`: Contains a list of 10-letter words used in the Hangman. 
Each word is on a separate line, making it easy to add or remove words.

### `maps/`
Stores maze map files for each level, providing different challenges as players progress.

### `mini_games/`
This directory contains individual files for each mini-game:
- `_2048.py`: Implements a modified 2048 game, where players must create a tile with the value "64" to proceed.
- `hangman.py`: Classic Hangman game, where players guess letters in a word before running out of attempts.
- `math_puzzle.py`: Math-based puzzle challenges that players must solve to advance.
- `number_guessing.py`: A number guessing game that narrows the range based on player guesses.
- `riddle.py`: Presents a random riddle, with players given a limited number of attempts to solve it.
- `tic_tac_toe.py`: Tic Tac Toe game, where players must try to tie with the computer.
- `trivia.py`: Presents a trivia question to the player, who must answer correctly to advance.
- `wordle.py`: A simplified Wordle game where players guess a 5-letter word within a fixed number of attempts.

## Credits

Developed by Li Tsun Wai, Liu Kwan Ho, Li Yitong, Tong Ka Kit, Leung Tsz Yuet

