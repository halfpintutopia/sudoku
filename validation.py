from string_enums import InputPrompt
import re
from screen import on, clear
from global_constants import *


def validate_number_guess(guess):
    try:
        number = int(guess)
        if not 1 <= number <= 9:
            raise ValueError()
    except ValueError:
        on(16, 55, "Number invalid.")
        on(17, 55, "Number must be 1 - 9")
        return False
    return True


def validate_coordinates(row_cell):
    """
    Check row_cell contains 2 characters and contains a letter and a number
    """
    try:
        cell = [coord for coord in row_cell]
        if len(cell) == 2:
            if not cell[0].isdigit() and cell[1].isalpha():
                raise ValueError()
            if not cell[0].isalpha() and cell[1].isdigit():
                raise ValueError()
        else:
            raise ValueError()
    except ValueError:
        on(19, 55, "Only one letter")
        on(20, 55, "and one number")
        on(21, 55, "Must not contain spaces")
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
        on(19, LEFT_MARGIN, InputPrompt.INVALID_DIFFICULTY.value)
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
        if username == '':
            raise ValueError(
                "Username cannot be blank"
            )
        if not bool(re.match(PATTERN, username)):
            raise ValueError(
                "Name entered contains capital letters or special characters"
            )
    except ValueError as e:
        clear(17, LEFT_MARGIN)
        on(17, LEFT_MARGIN, e)
        return False

    return True


def validate_grid_cell(puzzle, row, col):
    """
    Compare the set grid and current puzzle.
    If number is part of the grid, must not be overwritten
    """
    try:
        if puzzle[row][col] != 0:
            raise ValueError()
    except ValueError:
        on(18, 55, "Number is part of puzzle")
        on(19, 55, "Choose another number")
        return False
    return True


def validate_menu_option(option):
    try:
        int(option)
        if not 1 <= int(option) <= 3:
            raise ValueError()
    except ValueError:
        on(16, LEFT_MARGIN, InputPrompt.INVALID_MAIN_MENU.value)
        return False
    return True


def validate_row_for_duplicates(row):
    """
    Validate the row and check whether there are duplicate numbers in
    the row
    """
    try:
        duplicates = {str(x) for x in row if x != 0 and row.count(x)
                      > 1}
        if len(duplicates) > 0:
            raise ValueError(
                f"You have entered {', '.join(duplicates)} multiple "
                f"times in the same row"
            )
    except ValueError as e:
        clear(16, 1, 80)
        on(16, LEFT_MARGIN, e)
        return False
    return True


def validate_row(row):
    """
    Validates the string of numbers inputted
    Removes all spaces from the string if the user has entered them
    Splits the string up and creates a list
    """
    try:
        if len(row) < 9:
            raise ValueError(
                f"You have only entered {len(row)}"
            )
        elif len(row) > 9:
            raise ValueError(
                f"You have entered {len(row)}"
            )

    except ValueError as e:
        clear(20, 1, 60)
        clear(21, 1, 60)
        on(20, LEFT_MARGIN, e)
        on(21, LEFT_MARGIN, 'Please enter exactly 9 numbers')
        return False

    return True


def validate_list_contains_integers(row):
    """
    Validate list from user's input
    """
    try:
        for num in row:
            int(num)
            if not 0 <= int(num) <= 9:
                raise ValueError()
    except ValueError:
        clear(20, 1, 60)
        clear(21, 1, 60)
        on(20, LEFT_MARGIN, 'Only numbers 1 - 9')
        return False

    return True
