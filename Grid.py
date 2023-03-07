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
        self.grid = [[0 for x in range(9)] for y in range(9)]
        return self.grid

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
                        sudoku_numbers.remove(random_num)

        self.fill_in_zeroes()

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
        """
        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                if self.grid[row][column] == 0:
                    random_number = random.randint(1, 9)
                    cell = self.find_zeroes()
                    # print(self.find_zeroes()[0])
                    if self.check_cell(random_number, cell):
                        self.grid[cell[0]][cell[1]] = random_number

        # print(type(self.grid[row]))
        # print(self.grid[row].index(random_number))
        # if random_number in self.grid[row]:
        #     print(f"random number is already in {self.grid[row]}, {random_number}")
        # elif random_number in self.grid[column]:
        #     # return False
        #     print(f"random number is already in {self.grid[column]}, {random_number}")
        # else:
        #     # self.grid[row][column] = random_number
        #     print(f"random number is not in {self.grid[column]} or {self.grid[row]}, {random_number}")

        # try:
        #     self.grid[row].index(random_number)
        #     return True
        # except ValueError as e:
        #     print(f"random: {random_number}")

        # pprint(f"column: {self.grid[row]} {self.grid[column]}")

    def check_cell(self, number, cell):
        """
        Checks if the cell contains a zero and is not already in the row or column
        cell is a tuple, first in tuple is row, second in tuple is column
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
        # print(f"three by three: {three_by_three}")
