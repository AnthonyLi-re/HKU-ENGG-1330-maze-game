# mini_games/tic_tac_toe.py

from random import choice
from utilities import clear_screen, get_key
from time import sleep

empty_board = [" " for _ in range(9)]

class Player:
    def __init__(self, name, is_computer=False):
        self.name = name
        self.letter = "None"
        self.is_computer = is_computer

def play_tic_tac_toe():
    board = list(empty_board)
    p1 = Player("P1")
    p2 = Player("Computer", is_computer=True)

    letters = ["X", "O"]
    p1.letter = choice(letters)
    letters.remove(p1.letter)
    p2.letter = letters[0]

    active_player = p1

    while True:
        clear_screen()
        print("Tic Tac Toe")
        print(" " * 10 + f" {board[6]} | {board[7]} | {board[8]} ")
        print(" " * 10 + "---+---+---")
        print(" " * 10 + f" {board[3]} | {board[4]} | {board[5]} ")
        print(" " * 10 + "---+---+---")
        print(" " * 10 + f" {board[0]} | {board[1]} | {board[2]} ")
        print(f"PlayerOne: {p1.letter}         PlayerTwo: {p2.letter}")

        if active_player.is_computer:
            move = computer_move(board)
        else:
            move = make_move(active_player, board)
        board[move - 1] = active_player.letter

        if check_win(active_player, board) or " " not in board:
            clear_screen()
            print("Tic Tac Toe - Final Board")
            print(" " * 10 + f" {board[6]} | {board[7]} | {board[8]} ")
            print(" " * 10 + "---+---+---")
            print(" " * 10 + f" {board[3]} | {board[4]} | {board[5]} ")
            print(" " * 10 + "---+---+---")
            print(" " * 10 + f" {board[0]} | {board[1]} | {board[2]} ")
            break

        if " " not in board:
            break

        active_player = p2 if active_player == p1 else p1

    input("Congratulations! Press Enter to return to the maze...")

def computer_move(board):
    available_moves = [i + 1 for i in range(9) if board[i] == " "]
    return choice(available_moves)

def make_move(player, board):
    previous_moves = set()
    while True:
        move = input(f"{player.name} Move (1-9): ")
        try:
            move = int(move)
            if move in previous_moves:
                print("Illegal Move, you cannot input the same number more than once.")
                sleep(1.5)
                continue
            if move < 1 or move > 9 or board[move - 1] != " ":
                print("Illegal Move, try again.")
                sleep(1.5)
                continue
            previous_moves.add(move)
            return move
        except ValueError:
            print("Invalid input, please enter a number between 1 and 9.")
            sleep(1.5)

def check_win(player, board):
    letter = player.letter
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == letter for i in condition):
            return True
    return False
