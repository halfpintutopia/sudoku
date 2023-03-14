def on(row, col, string, num_of_blanks=25):
    """
    Combine clear_line and write_line
    """
    clear(row, col, num_of_blanks)
    write(row, col, string)


def clear(row, col, num_of_blanks=25):
    """
    Before writing a new line, clears the line by over-writing with blank spaces
    This is used for the right side of the screen
    Set number of blank spaces to be more or less dependent on the number of character needed to be overwritten
    """
    print(f"\x1b[{row};{col}H{' ' * num_of_blanks}")


def write(row, col, string):
    """
    Add text at a particular row and column of the screen
    """
    print(f"\x1b[{row};{col}H{string}")
