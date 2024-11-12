# main.py

from maze import load_maze, display_maze
from player import play_maze
from utilities import clear_screen, get_key, load_logo
import os

def main_menu():
    logo = load_logo()  # Load the logo from logo.txt
    selected_index = 0
    options = ["Play Game", "Quit"]
    level_options = ["LEVEL 1 (10x10)", "LEVEL 2 (15x15)", "LEVEL 3 (20x20)", "LEVEL 4 (25x25)"]

    while True:
        clear_screen()
        terminal_width = os.get_terminal_size().columns
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
                # Level selection screen
                level_selected = 0
                while True:
                    clear_screen()
                    print("Select a Level:")
                    for i, level in enumerate(level_options):
                        if i == level_selected:
                            print(f"> {level} <")
                        else:
                            print(level)
                    level_key = get_key().lower()
                    if level_key == "w" and level_selected > 0:
                        level_selected -= 1
                    elif level_key == "s" and level_selected < len(level_options) - 1:
                        level_selected += 1
                    elif level_key == "\r" or level_key == "\n":
                        break
                map_files = ["maps/10x20.txt", "maps/15x30.txt", "maps/20x40.txt", "maps/25x50.txt"]
                maze = load_maze(map_files[level_selected])
                max_width = max(len(row) for row in maze)
                maze = [row + [' '] * (max_width - len(row)) for row in maze]
                play_maze(maze)
            elif selected_index == 1:
                print("Goodbye!")
                break

if __name__ == "__main__":
    main_menu()
