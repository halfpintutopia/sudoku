from enum import Enum


class Difficulty(Enum):
    EASY = 51
    MEDIUM = 53
    HARD = 56


class MainMenu(Enum):
    PLAY = '1. Play'
    ENTER_OWN = '2. Enter your own puzzle'
    INSTRUCTIONS = '3. Instructions'
    LOADING = 'Just one moment... '
    EXIT = 'X to exit'


class DifficultyPrompt(Enum):
    CHOOSE = 'Please choose difficulty:'
    EASY = '1 for easy'
    MEDIUM = '2 for medium'
    HARD = '3 for hard'


class InputPrompt(Enum):
    PRESS_ENTER = 'Press Enter to return to menu... '
    USERNAME = 'Enter your username: '
    NUMBER = 'Enter a number: '
    INVALID_DIFFICULTY = 'Please enter a number between, 1, 2, 3'
    COORDINATES = 'Enter a number and a letter or exit: '
    INVALID_MAIN_MENU = 'Please choose one of the options. 1, 2, or 3'


class GoogleSheets(Enum):
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]
    CREDS_FILE = 'creds.json'
    SHEET = 'sudoku_games'
    USER_WORKSHEET = 'users'
    GAMES_WORKSHEET = 'saved_games'
