from helper_enums import InputPrompt
import re
from screen import on, clear

pattern = "^[a-z0-9_-]*$"


def validate_number_guess(guess):
    try:
        number = int(guess)
    except ValueError:
        print("Please enter a number")
        return False
    return True


def validate_coordinates(row_cell):
    """
    Check row_cell contains 2 characters and contains a letter and a number
    """
    cell = [coord for coord in row_cell]
    try:
        if len(cell) == 2:
            (
                    cell[0].isdigit() and cell[1].isalpha()
            ) or (
                    cell[0].isalpha() and cell[1].isdigit()
            )
    except ValueError:
        return False
    return True


def validate_difficulty_input(difficulty):
    """
    Checks the input for difficulty entered is a number
    """
    try:
        isinstance(int(difficulty), int)
        if not 1 <= int(difficulty) <= 3:
            raise ValueError
    except ValueError:
        print(InputPrompt.INVALID_DIFFICULTY.value)
        return False

    return True


def validate_username(username):
    """
    Check string inputted by user to meet the conditions:
    - lowercase
    - no special characters except underscore and or hyphen
    - contains no spaces
    """
    try:
        if not bool(re.match(pattern, username)):
            raise ValueError()
    except ValueError:
        clear(15, 1)
        on(15, 1,
           'Name entered contains capital letters or special characters')
        return False

    return True
