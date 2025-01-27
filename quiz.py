import csv
import os
import random
from quizzes import quizzes
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

# Constants
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
FILE_PATH = os.path.join(DATA_DIR, "score.csv")


class Quiz:
    """Stores questions and answers"""

    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question_data):
        print(question_data["question"])
        for i, option in enumerate(question_data["options"], start=1):
            print(f"{i}. {option}")

    def get_answer(self):
        while True:
            try:
                choice = int(input("\nSelect a number between 1 and 3: "))
                if 1 <= choice <= 3:
                    return choice
                else:
                    print("Please select a number between 1 and 3")
            except ValueError:
                print("Invalid input. Please enter a number")

    def check_answer(self, question_data, user_input):
        correct_answer = question_data["options"].index(question_data["answer"]) + 1
        if user_input == correct_answer:
            print(Fore.GREEN + "\nCorrect answer!\n" + Style.RESET_ALL)
            self.score += 1
        else:
            print(
                Fore.RED
                + f"\nWrong answer. The correct answer is {question_data["answer"]}.\n"
                + Style.RESET_ALL
            )

    def run_quiz(self):
        print("Welcome to the Video Game Trivia Quiz!\n")
        for question in self.questions:
            self.display_question(question)
            user_choice = self.get_answer()
            self.check_answer(question, user_choice)
        print(f"Quiz over! Your final score is {self.score} / {len(self.questions)}")


quiz = Quiz(quizzes)
quiz.run_quiz()
