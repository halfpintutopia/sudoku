from enum import Enum


class Difficulty(Enum):
    EASY = 51
    MEDIUM = 53
    HARD = 56


class TermcolorSettings(Enum):
    RED = 'red'
    YELLOW = 'yellow'
    BLUE = 'blue'
    BOLD = 'bold'
    DARK = 'dark'


class Instructions(Enum):
    FIRST_LINE = 'A Sudoku puzzle is created with a 9 by 9 square (9 rows ' \
                 'and 9 columns).'
    SECOND_LINE = 'The 9 by 9 square is also divided into 3 by 3 areas (a ' \
                  'total of 9 x 3 by 3 areas).'
    THIRD_LINE = 'Each row, column and 3 by 3 area must contain numbers ' \
                 '1 - 9 (inclusive).'
    FOURTH_LINE = 'Numbers cannot be repeated in the row, column nor 3 ' \
                  'by 3 area.'


class MainMenu(Enum):
    PLAY = '1. Play'
    ENTER_OWN = '2. Enter your own puzzle'
    INSTRUCTIONS = '3. Instructions'
    LOADING = 'Just one moment... '
    EXIT = 'X to exit'


class DifficultyPrompt(Enum):
    CHOOSE = 'Please choose difficulty'
    EASY = '1 for easy'
    MEDIUM = '2 for medium'
    HARD = '3 for hard'


class InputPrompt(Enum):
    PRESS_ENTER = 'Press Enter to return to menu... '
    USERNAME = 'Enter your username: '
    NUMBER = 'Enter a number: '
    INVALID_DIFFICULTY = 'Invalid input: Please enter a number between, ' \
                         '1, 2, or 3 please try again.'
    COORDINATES = 'Enter a number and a letter or exit: '
    INVALID_MAIN_MENU = 'Please choose one of the options. 1, 2, 3, or 4'


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


class Username(Enum):
    PROMPT_1 = 'Add your username. Username should be lowercase.'
    PROMPT_2 = 'Username must only contain letters a-z and can contain a ' \
               'hyphen (-) or underscore (_).'
    PROMPT_3 = 'Username should not contain spaces.'


class Guess(Enum):
    PROMPT_1 = 'Please enter a row number and a column letter. e.g. 4E'
    PROMPT_2 = 'Please enter a number (1-9) you want to put in the cell'
