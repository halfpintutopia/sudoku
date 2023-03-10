from pprint import pprint
import random


class Sudoku:
    def __init__(self):
        self.grid = None
        self.create_blank_sudoku()

    def create_blank_sudoku(self):
        self.grid = [[0 for x in range(9)] for y in range(9)]
        return self.grid

    def create_puzzle(self):
        self.fill_diagonal_3_by_3([(0, 3), (3, 6), (6, 9)])
        self.create_solutions()
        return self.grid

    def fill_diagonal_3_by_3(self, range_list):
        """
        Initial 3 x 3 by 3 sections filled in
        Fills the grid with the 1/9 5/9 and 9/9 3x3 areas on sudoku grid
        Provides a unique number for each line and row and makes recursion a bit easier
        Once the numbers are filled in for the 3 sections the rest of the numbers can be added
        """
        for range_values in range_list:
            nums = list(range(1, 10))
            if type(range_values) is tuple:
                for row in range(range_values[0], range_values[1]):
                    for col in range(range_values[0], range_values[1]):
                        rand_num = random.choice(nums)
                        self.grid[row][col] = rand_num
                        nums.remove(rand_num)

        return self.grid

    def create_solutions(self):
        """
        Copy the grid to find a solution or multiple solutions
        Get missing numbers in the row lists
        """
        cell = self.find_next_zero()
        print(f"cell: {cell}")

        return True

    def find_next_zero(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 0:
                    return row, col

        return True
