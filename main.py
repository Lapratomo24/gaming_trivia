import sys
import time
import os
import platform
import csv
from datetime import datetime
from colorama import init, Fore, Style
from quiz import Quiz, DATA_DIR, FILE_PATH
from quizzes import quizzes

init(autoreset=True)


def ensure_data_dir_exists():
    """Ensure data directory exists"""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def clear_screen():
    """Clears the terminal screen"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def loading():
    """Displays a short loading animation"""
    print("Now loading", end="", flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    clear_screen()


def save_to_csv(username, score, num_questions):
    fieldnames = ["Username", "Score", "#Questions", "Date"]
    with open(FILE_PATH, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(
            {
                "Username": username,
                "Score": score,
                "#Questions": num_questions,
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            }
        )


def run_trivia_quiz():
    """Displays trivia quiz to user"""
    print(Fore.BLUE + "Welcome to Gaming Quiz! \n" + Style.RESET_ALL)
    username = input("Tell us your name: ")
    loading()

    while True:
        try:
            num = int(
                input(
                    f"Hi, {username}! How many questions would you like to answer? (10, 15, 20): "
                )
            )
            if num in [10, 15, 20]:
                break
            else:
                print(Fore.YELLOW + "Choose between 10, 15, or 20" + Style.RESET_ALL)
        except ValueError:
            print(
                Fore.YELLOW + "Invalid input. Please enter a number" + Style.RESET_ALL
            )

    quiz = Quiz(quizzes)
    score = quiz.run_quiz(num)
    # time_taken = datetime.now().strftime("%Y-%m-%d %H:%M")
    save_to_csv(username, score, num)


def run_trivia_history():
    """Displays trivia history to user"""
    print(Fore.BLUE + "Welcome to Timelines of Gaming History! \n" + Style.RESET_ALL)
    print("=== Select Platform ===")
    print("(a) PlayStation")
    print("(b) Xbox")
    print("(c) Nintendo")
    
    while True:
        try:
            choice = input("You pick: ")
            if mode_validation(choice):
                display_timeline()
            else:
                print(Fore.YELLOW + "Select between (a), (b), or (c)." + Style.RESET_ALL)
        except ValueError:
            print(Fore.YELLOW + "Invalid input. Select between (a), (b), or (c)." + Style.RESET_ALL)
            
    
def mode_validation(input):
    """Validates user input for mode selection"""
    if input in ["a", "b", "c"]:
        return True
    else:
        print(Fore.YELLOW + "Invalid input. Try again" + Style.RESET_ALL)
        return False


def display_menu():
    """Displays the main menu"""
    print(Fore.BLUE + "\nWelcome to Video Game Trivia!")
    print("Select a mode to run the program:\n" + Style.RESET_ALL)
    print("=====================================")
    print("(a) Trivia: Timelines of Gaming History")
    print("(b) Trivia: Gaming Quiz")
    print("(c) Exit")
    print("=====================================")


def main():
    """Runs all functions"""
    ensure_data_dir_exists()

    while True:
        display_menu()
        select = input("\nSelect (a) or (b) to run the program: ").strip().lower()
        if mode_validation(select):
            loading()

            if select == "a":
                run_trivia_history()
            elif select == "b":
                run_trivia_quiz()
            else:
                print("Exiting program...")
                sys.exit(1)


if __name__ == "__main__":
    main()
