# mini_games/math_puzzle.py

import random
from utilities import clear_screen

def play_math_puzzle():
    print("Solve 3 different math puzzles to proceed.")

    def generate_complex_arithmetic():
        # Generate a more complex arithmetic question with two operations
        num1 = random.randint(10, 50)
        num2 = random.randint(10, 50)
        num3 = random.randint(1, 20)
        operations = ["+", "-"]
        op1, op2 = random.sample(operations, 2)
        
        if op1 == "+":
            part1 = num1 + num2
        elif op1 == "-":
            part1 = num1 - num2

        if op2 == "+":
            answer = part1 + num3
            question = f"({num1} {op1} {num2}) {op2} {num3}"
        elif op2 == "-":
            answer = part1 - num3
            question = f"({num1} {op1} {num2}) {op2} {num3}"
        
        return question, answer

    def generate_arithmetic_sequence():
        # Generate an arithmetic sequence question
        start = random.randint(1, 10)
        diff = random.randint(2, 5)
        terms = [start + i * diff for i in range(5)]
        answer = terms[-1] + diff  # Next term in the sequence
        question = f"Find the next number in the sequence: {', '.join(map(str, terms))}, ..."
        return question, answer

    def generate_simple_algebra():
        # Generate a simple algebra problem of the form ax + b = c
        a = random.randint(1, 10)
        x = random.randint(1, 10)
        b = random.randint(1, 10)
        c = a * x + b
        question = f"Solve for x: {a}x + {b} = {c}"
        answer = x
        return question, answer

    def generate_percentage_problem():
        # Generate a percentage problem
        total = random.randint(100, 500)
        percent = random.choice([10, 15, 20, 25, 30, 50])
        answer = (total * percent) / 100
        question = f"What is {percent}% of {total}?"
        return question, answer

    # List of question generators
    question_generators = [
        generate_complex_arithmetic,
        generate_arithmetic_sequence,
        generate_simple_algebra,
        generate_percentage_problem,
    ]

    # Player must solve 3 questions to proceed
    questions_to_solve = 3
    for i in range(questions_to_solve):
        question, answer = random.choice(question_generators)()
        attempts = 3  # Allow 3 attempts per question

        while attempts > 0:
            try:
                user_answer = int(input(f"Puzzle {i + 1}: {question} = "))
                if user_answer == answer:
                    print("Correct!")
                    break
                else:
                    attempts -= 1
                    print(f"Incorrect. You have {attempts} attempts left.")
            except ValueError:
                print("Please enter a valid number.")
                attempts -= 1

        # If the player fails any of the 3 questions, they must restart the puzzle
        if attempts == 0:
            print("You ran out of attempts on one of the puzzles.")
            input("Press Enter to retry the entire math puzzle...")
            return play_math_puzzle()  # Restart the entire math puzzle if failed

    # If all questions are solved correctly, allow the player to proceed
    input("Congratulations! You solved all puzzles. Press Enter to return to the maze...")
