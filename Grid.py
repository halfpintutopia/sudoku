# from Label import *
from pprint import pprint


class Grid:
    def __init__(self):
        self.grid = None
        self.create_empy_board()
        # self.__reset_board()

    def __str__(self):
        grid_string = "    "
        index = 1
        for letter in range(ord('a'), ord('j')):
            grid_string += "  " + chr(letter) + " "
            if index % 3 == 0 and index != 9:
                grid_string += "   "
            index += 1

        grid_string += "\n   " + "-" * 43 + "\n"

        for i in range(9):
            grid_string += str(i + 1) + " | "

            if i % 3 == 0 and i != 0:
                print("-" * 30)

            for j in range(9):
                if j % 3 == 0 and j != 0:
                    grid_string += " | "
                if j == 8:
                    grid_string += "  " + str(self.grid[i][j]) + " "
                else:
                    grid_string += "  " + str(self.grid[i][j]) + " "
            grid_string += "\n"

            if (i + 1) % 3 == 0 and (i + 1) != 9:
                "--------------------------------------------"
                grid_string += "   " + "-" * 43 + "\n"
        return f"{grid_string}"

    def create_empy_board(self):
        """
        Initialises with an empty board
        """
        # self.grid = [[(chr(x), y) for x in range(ord('a'), ord('j') + 1)] for y in range(1, 10)]
        self.grid = [[0 for x in range(ord('a'), ord('j') + 1)] for y in range(1, 10)]
        return self.grid



