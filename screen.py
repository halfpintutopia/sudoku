def clear_screen():
    """
    Helper function to clear the entire 24 row / 80 col screen
    """
    print(f"\x1b[2J")


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
    Show the input
    A helper function to return an input at a set row and column
    """
    return input(f"\x1b[{row};{col}H{string}\x1b[{row + 1};{col}H")


def esc(code):
    return f'\033[{code}m'
