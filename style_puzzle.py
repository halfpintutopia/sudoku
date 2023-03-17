from termcolor import colored
from screen import on


class StylePuzzle:
    def __init__(
            self,
            original_puzzle: [list[int]],
            current_puzzle: [list[int]]
    ):
        self.original_puzzle = original_puzzle
        self.current_puzzle = current_puzzle
        self.grid_string = None
        self.original_num_colour = 'yellow'
        self.guess_num_colour = 'blue'
        self.num_style_bold = 'bold'
        self.double_space = '  '
        self.single_space = ' '

    def add_column_headings(self):
        """
        Add letters A through J for each column heading
        """
        self.grid_string = "    "
        index = 1
        for letter in range(ord('A'), ord('J')):
            self.grid_string += "  " + chr(letter) + " "
            if index % 3 == 0 and index != 9:
                self.grid_string += "   "
            index += 1

        self.grid_string += "\n   " + "-" * 43 + "\n"
        return self.grid_string

    def add_subgrid_row_lines(self, row: int):
        """
        Add style for every three rows
        """
        if (row + 1) % 3 == 0 and (row + 1) != 9:
            self.grid_string += "   " + "-" * 43 + "\n"

        return self.grid_string

    def add_subgrid_col_lines(self, col: int):
        """
        Add style for every three columns
        """
        if col % 3 == 0 and col != 0:
            self.grid_string += " | "

        return self.grid_string

    def add_row_heading_lines(self, row: int):
        """
        Add style for row headings
        """
        self.grid_string += str(row + 1) + " | "
        return self.grid_string

    def color_original_numbers(self, row: int, col: int):
        """
        When number is part of the original puzzle,
        then change color of number on grid to yellow
        """
        self.grid_string += self.double_space + colored(
            str(self.current_puzzle[row][col]),
            self.original_num_colour,
            attrs=[self.num_style_bold]
        ) + self.single_space
        return self.grid_string

    def color_guesses(self, row: int, col: int):
        """
        When the number in the grid is a user's guess,
        the number is a different color to the original puzzle numbers
        """
        self.grid_string += self.double_space + colored(
            str(self.current_puzzle[row][col]),
            self.guess_num_colour,
            attrs=[self.num_style_bold]
        ) + self.single_space
        return self.grid_string

    def set_zero_num_to_white(self, row: int, col: int):
        """
        Default color for cells in the grid that have no number in them
        """
        self.grid_string += self.double_space + colored(
            str(self.current_puzzle[row][col]),
            attrs=[self.num_style_bold]) + self.single_space
        return self.grid_string

    def add_puzzle_style(self):
        """
        Print out the grid with style and headings for columns and rows
        """
        self.add_column_headings()

        for row in range(9):
            self.add_row_heading_lines(row)
            for col in range(9):
                self.add_subgrid_col_lines(col)
                if self.original_puzzle[row][col] != 0:
                    self.color_original_numbers(row, col)
                elif self.current_puzzle[row][col] != 0:
                    self.color_guesses(row, col)
                else:
                    self.set_zero_num_to_white(row, col)

            self.grid_string += "\n"

            self.add_subgrid_row_lines(row)
        on(10, 1, self.grid_string)
