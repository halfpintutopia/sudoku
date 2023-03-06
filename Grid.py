# from Label import *
from pprint import pprint


class Grid:
    def __init__(self):
        self.grid = None
        self.create_empy_board()
        # self.__reset_board()

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
        # self.grid = [[(chr(x), y) for x in range(ord('a'), ord('j') + 1)] for y in range(1, 10)]
        self.grid = [[0 for x in range(ord('a'), ord('j') + 1)] for y in range(1, 10)]
        return self.grid



