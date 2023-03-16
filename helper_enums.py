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
    SOLVE = '3. Solve a puzzle'
    INSTRUCTIONS = '4. Instructions'


class DifficultyPrompt(Enum):
    CHOOSE = 'Please choose difficulty'
    EASY = '1 for easy'
    MEDIUM = '2 for medium'
    HARD = '3 for hard'


class InputPrompt(Enum):
    PRESS_ENTER = 'Press Enter to return to menu... '

