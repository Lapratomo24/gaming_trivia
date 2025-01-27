import sys
import csv
import time
import os
import platform
import random
from colorama import init, Fore, Style
from quiz import Quiz

init(autoreset=True)

# Constants
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
FILE_PATH = os.path.join(DATA_DIR, "trivia.csv")

