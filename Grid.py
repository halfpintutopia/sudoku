# from Label import *
from pprint import pprint
import random


class Grid:
    def __init__(self):
        self.grid = None
        self.create_empy_board()

    def __str__(self):
        """
        Print out the grid with style and headings for columns and rows
        """
        grid_string = "    "
        index = 1
        for letter in range(ord('a'), ord('j')):
            grid_string += "  " + chr(letter) + " "
            if index % 3 == 0 and index != 9:
                grid_string += "   "
            index += 1

        grid_string += "\n   " + "-" * 43 + "\n"

        for row in range(9):
            grid_string += str(row + 1) + " | "
            for column in range(9):
                if column % 3 == 0 and column != 0:
                    grid_string += " | "
                if column == 8:
                    grid_string += "  " + str(self.grid[row][column]) + " "
                else:
                    grid_string += "  " + str(self.grid[row][column]) + " "
            grid_string += "\n"

            if (row + 1) % 3 == 0 and (row + 1) != 9:
                grid_string += "   " + "-" * 43 + "\n"

        return grid_string

    def create_empy_board(self):
        """
        Initialises with an empty board
        """
        self.grid = [[0 for x in range(ord('a'), ord('j') + 1)] for y in range(1, 10)]
        # return self.grid

    def create_completed_game(self):
        """
        Main function to create a filled in grid
        """
        self.create_empy_board()
        self.fill_diagonal_sections([(0, 3), (3, 6), (6, 9)])
        return self.grid

    def fill_diagonal_sections(self, range_array):
        """
        Initial 3 sections filled in
        Fills the grid with the 1/9 5/9 and 9/9 3x3 areas on sudoku grid
        Provides a unique number for each line and row
        Once the numbers are filled in for the 3 sections the rest of the numbers can be added
        """
        for range_values in range_array:
            sudoku_numbers = list(range(1, 10))
            if type(range_values) is tuple:
                for row in range(range_values[0], range_values[1]):
                    for column in range(range_values[0], range_values[1]):
                        random_num = random.choice(sudoku_numbers)
                        self.grid[row][column] = random_num
                        print(self.grid)
                        sudoku_numbers.remove(random_num)
