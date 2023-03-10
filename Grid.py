# from Label import *
from pprint import pprint
import random

TEST = 'test string'


class Grid:
    def __init__(self):
        self.grid = None
        self.create_empy_board()

    # def __str__(self):
    #     """
    #     Print out the grid with style and headings for columns and rows
    #     """
    #     grid_string = "    "
    #     index = 1
    #     for letter in range(ord('a'), ord('j')):
    #         grid_string += "  " + chr(letter) + " "
    #         if index % 3 == 0 and index != 9:
    #             grid_string += "   "
    #         index += 1
    #
    #     grid_string += "\n   " + "-" * 43 + "\n"
    #
    #     for row in range(9):
    #         grid_string += str(row + 1) + " | "
    #         for column in range(9):
    #             if column % 3 == 0 and column != 0:
    #                 grid_string += " | "
    #             if column == 8:
    #                 grid_string += "  " + str(self.grid[row][column]) + " "
    #             else:
    #                 grid_string += "  " + str(self.grid[row][column]) + " "
    #         grid_string += "\n"
    #
    #         if (row + 1) % 3 == 0 and (row + 1) != 9:
    #             grid_string += "   " + "-" * 43 + "\n"
    #
    #     return grid_string

    def create_empy_board(self):
        """
        Initialises with an empty board
        """
        self.grid = [[0 for x in range(9)] for y in range(9)]
        # return self.grid

    def create_completed_game(self):
        """
        Main function to create a filled in grid
        """
        self.create_empy_board()
        self.fill_diagonal_sections([(0, 3), (3, 6), (6, 9)])
        self.fill_in_zeroes()
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
                        sudoku_numbers.remove(random_num)

    def find_zeroes(self):
        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                if self.grid[row][column] == 0:
                    return row, column

        return False

    def fill_in_zeroes(self):
        """
        Fills in the grid.
        Replaces the cells that contain 0 with a random number
        - create a list of numbers missing from the row
        - randomly choose a number from the list and then check the cell
        - if the cell row, column 3x3 has the number choose another
        - loop until the number can be put into the cell
        """

        for row in range(len(self.grid)):
            missing_numbers = self.get_missing_numbers_in_row(row)
            for column in range(len(self.grid[row])):
                if len(missing_numbers) > 1:
                    if self.grid[row][column] == 0:
                        number = self.check_number_is_unique(missing_numbers, (row, column))
                        self.grid[row][column] = number
                        missing_numbers.remove(number)
                else:
                    self.grid[row][column] = missing_numbers[0]

    def check_number_is_unique(self, missing_numbers, cell):
        numbers_to_check = missing_numbers.copy()
        while True:
            random_number = random.choice(numbers_to_check)
            if self.check_cell(random_number, (cell[0], cell[1])):
                break
            else:
                numbers_to_check.remove(random_number)

        return random_number

    def get_missing_numbers_in_row(self, row):
        missing_numbers = []
        for num in range(1, 10):
            if num not in self.grid[row]:
                missing_numbers.append(num)

        return missing_numbers

    def check_cell(self, number, cell):
        """
        Checks if the cell contains a zero and is not already in the row or column
        cell is a tuple, first in tuple is row, second in tuple is column
        First checks row, the column and then 3x3 area
        """
        if number in self.grid[cell[0]]:
            return False

        numbers_in_column = [self.grid[row][cell[1]] for row in range(len(self.grid))]
        if number in numbers_in_column:
            return False

        three_by_three = [self.grid[row + ((cell[0] // 3) * 3)][column + ((cell[1] // 3) * 3)] for row in range(3) for
                          column in range(3)]

        if number in three_by_three:
            return False

        return True
