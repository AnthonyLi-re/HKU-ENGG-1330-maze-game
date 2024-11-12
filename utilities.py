# utilities.py

import os
import sys
import termios
import tty

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def load_logo(filename="logo.txt"):
    with open(filename, 'r') as file:
        logo = file.read()
    return logo