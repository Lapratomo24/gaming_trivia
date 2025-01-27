import sys
import time
import os
import platform
import random
from colorama import init, Fore, Style
from quiz import Quiz, DATA_DIR, FILE_PATH
from quizzes import quizzes

init(autoreset=True)


def ensure_data_dir_exists():
    ''' Ensure data directory exists '''
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def clear_screen():
    ''' Clears the terminal screen '''
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def loading():
    ''' Displays a short loading animation '''
    print("Now loading", end="", flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    clear_screen()
    

def run_trivia_quiz():
    print(Fore.BLUE + "Welcome to Trivia Quiz!" + Style.RESET_ALL)
    
    while True:
        try: 
            num = int(input("How many questions would you like to answer? (10, 15, 20): "))
            if num in [10, 15, 20]:
                break
            else:
                print(Fore.YELLOW + "Choose between 10, 15, or 20" + Style.RESET_ALL)
        except ValueError:
            print(Fore.YELLOW + "Invalid input. Please enter a number" + Style.RESET_ALL)
    
    quiz = Quiz(quizzes)
    quiz.run_quiz(num)
        
    
def mode_validation(input):
    ''' Validates user input for mode selection '''
    if input in ["a", "b", "c"]:
        return True
    else:
        print(Fore.YELLOW + "Invalid input. Try again" + Style.RESET_ALL)
        return False


def display_menu():
    ''' Displays the main menu '''
    print(Fore.BLUE + "\nWelcome to Video Game Trivia!")
    print("Select a mode to run the program:\n" + Style.RESET_ALL)
    print("=====================================")
    print("(a) Trivia Explorer")
    print("(b) Trivia Quiz")
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
                run_trivia_explorer()
            elif select == "b":
                run_trivia_quiz()
                loading()
            else:
                print("Exiting program...")
                sys.exit(1)
    

if __name__ == "__main__":
    main()
