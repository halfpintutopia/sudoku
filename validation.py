from helper_enums import InputPrompt
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
        on(18, 55, "Only one letter")
        on(19, 55, "and one number")
        on(20, 55, "Must not contain spaces")
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
        on(19, left_margin, InputPrompt.INVALID_DIFFICULTY.value)
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
        clear(15, left_margin)
        on(15, left_margin,
           'Name entered contains capital letters or special characters')
        return False

    return True


# def validate_menu_option(menu_choice):
#     """
#     Check the menu option chosen is a valid number,
#     a number from 1 to 4 inclusive
#     """
#     try:
#         int(menu_choice)
#         if 1 < int(menu_choice) > 4:
#             raise ValueError()
#     except ValueError:
#         on(16, left_margin, InputPrompt.INVALID_MAIN_MENU.value)
#         return False
#
#     return True


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
        on(16, left_margin, InputPrompt.INVALID_MAIN_MENU.value)
        return False
    return True
