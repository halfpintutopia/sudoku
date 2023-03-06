from pprint import pprint


class Grid:
    def __init__(self):
        self.grid = None
        self.create_empy_board()
        # self.__reset_board()

    def create_empy_board(self):
        """
        Initialises with an empty board
        """
        # self.grid = [[(chr(x), y) for x in range(ord('a'), ord('j') + 1)] for y in range(1, 10)]
        self.grid = [[0 for x in range(ord('a'), ord('j') + 1)] for y in range(1, 10)]

        pprint(self.grid)
