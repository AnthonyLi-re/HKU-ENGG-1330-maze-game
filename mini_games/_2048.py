# mini_games/2048.py

import random
from utilities import clear_screen, get_key

def init_board():
    return [[0] * 4 for _ in range(4)]

def add_new_tile(board):
    empty_tiles = [(r, c) for r in range(4) for c in range(4) if board[r][c] == 0]
    if empty_tiles:
        r, c = random.choice(empty_tiles)
        board[r][c] = 4 if random.random() > 0.9 else 2

def slide(row):
    new_row = [i for i in row if i != 0]
    while len(new_row) < 4:
        new_row.append(0)
    return new_row

def combine(row):
    for i in range(3):
        if row[i] == row[i + 1] and row[i] != 0:
            row[i] *= 2
            row[i + 1] = 0
    return row

def move_left(board):
    new_board = []
    for row in board:
        new_board.append(slide(combine(slide(row))))
    return new_board

def rotate_board(board):
    return [list(row) for row in zip(*board[::-1])]

def check_64_created(board):
    for row in board:
        if 64 in row:
            return True
    return False

def play_2048():
    board = init_board()
    add_new_tile(board)
    add_new_tile(board)
    
    while True:
        clear_screen()
        for row in board:
            print("    ".join([str(num).rjust(4) if num != 0 else "    " for num in row]))
        print("Use WASD keys to move. Press 'p' to pause the game.")

        move = get_key().lower()
        
        if move == 'p':
            input("Game paused. Press Enter to continue.")
        
        elif move in 'wasd':
            if move == 'w':
                board = rotate_board(board)
                board = rotate_board(board)
                board = rotate_board(board)
                board = move_left(board)
                board = rotate_board(board)
            elif move == 's':
                board = rotate_board(board)
                board = move_left(board)
                board = rotate_board(board)
                board = rotate_board(board)
                board = rotate_board(board)
            elif move == 'a':
                board = move_left(board)
            elif move == 'd':
                board = rotate_board(board)
                board = rotate_board(board)
                board = move_left(board)
                board = rotate_board(board)
                board = rotate_board(board)

            add_new_tile(board)

            if check_64_created(board):
                clear_screen()
                for row in board:
                    print("    ".join([str(num).rjust(4) if num != 0 else "    " for num in row]))
                print("Congratulations! You have successfully created a '64'.")
                input("Press Enter to return to the maze...")
                return
            elif all(board[r][c] != 0 for r in range(4) for c in range(4)):
                print("Game over! You did not create a '64'. You must try again.")
                input("Press Enter to restart the 2048 game...")
                board = init_board()
                add_new_tile(board)
                add_new_tile(board)
