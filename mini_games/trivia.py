# mini_games/trivia.py

import random
from utilities import clear_screen

def play_trivia():
    questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
        {"question": "How many continents are there on Earth?", "answer": "7"}
    ]
    question = random.choice(questions)
    attempts = 3
    
    while attempts > 0:
        user_answer = input(f"{question['question']} (Attempts left: {attempts}): ")
        if user_answer.strip().lower() == question['answer'].lower():
            input("Correct! Press Enter to return to the maze...")
            return
        else:
            print("Incorrect. Try again.")
            attempts -= 1
    
    print(f"Out of attempts! The correct answer was: {question['answer']}")
    input("Press Enter to try again...")
    play_trivia()  # Restart if failed
