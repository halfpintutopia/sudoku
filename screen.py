from pyfiglet import Figlet
from termcolor import colored

game_title = 'SUDOKU'
font_name = 'block'
title_color = 'yellow'


def clear_screen():
    """
    Helper function to clear the entire 24 row / 80 col screen
    """
    print(f"\x1b[2J")


def clear_screen_from_pos(row: int, col: int):
    """
    Helper function to clear the screen from the position of row and column
    """
    print(f"\x1b[{row};{col}H\x1b[0J")


def on(row, col, string, num_of_blanks=25):
    """
    Clears the line at row and column by using a number of blanks
    Overwrites line with blanks
    Write on the same line at the row and column
    """
    clear(row, col, num_of_blanks)
    write(row, col, string)


def clear(row, col, num_of_blanks=25):
    """
    Clears the line by over-writing with blank spaces
    This is used for the right side of the screen
    Set number of blank spaces to be more or less
    Dependent on the number of character needed to be overwritten
    """
    print(f"\x1b[{row};{col}H{' ' * num_of_blanks}")


def write(row, col, string):
    """
    Add text at a particular row and column of the screen
    """
    print(f"\x1b[{row};{col}H{string}")


def write_input(row, col, string):
    """
    Show the input at the position of row and col
    """
    return input(f"\x1b[{row};{col}H{string}\x1b[{row + 1};{col}H\x1b[5m")


def set_cursor(row, col):
    print(f"\x1b[{row}:{col}H")


def set_title():
    """
    Create title for the start screen
    """
    clear_screen()
    custom_fig = Figlet(font=font_name, justify="center")
    print("\x1b[1;1H" + colored(custom_fig.renderText(game_title),
                                title_color))


def clear_right_side():
    for num in range(10, 25):
        clear(num, 55)
