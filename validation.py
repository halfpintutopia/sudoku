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
                f"You have entered the {', '.join(duplicates)} multiple "
                f"times in the same row"
            )
    except ValueError as e:
        clear(16, 1, 80)
        on(16, left_margin, e)
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
        clear(16, 1, 60)
        clear(17, 1, 60)
        on(16, left_margin, e)
        on(17, left_margin, 'Please enter exactly 9 numbers')
        return False

    return True


def validate_list_contains_integers(row):
    """
    Validate list from user's input
    """
    try:
        for num in row:
            int(num)
    except ValueError:
        clear(16, 1, 60)
        clear(17, 1, 60)
        on(16, left_margin, 'You have entered letters.')
        on(17, left_margin, 'Please enter only numbers.')
        return False

    return True
