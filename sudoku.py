import copy
import random
from helper_enums import Difficulty
from screen import on, clear
from style_puzzle import StylePuzzle
from global_constants import *


class Sudoku:
    def __init__(self):
        self.completed_puzzle = None
        self.original_puzzle = None
        self.current_puzzle = None
        self.puzzle = None
        self.grid = None
        self.grid_sections = [(0, 2), (3, 5), (6, 8)]
        self.missing_num_in_subgrid_range = (0, 5)
        self.row_cell_range = (0, 8)
        self.col_cell_range = (0, 8)
        self.create_blank_sudoku()

    def create_blank_sudoku(self):
        """
        Creates a grid made of a list of lists with 9 zeros in each list
        """
        self.grid = [[0 for x in range(9)] for y in range(9)]
        return self.grid

    def create_puzzle(self):
        """
        Creates the puzzle grid, a completed sudoku puzzle
        All numbers are filled in
        """
        self.create_blank_sudoku()
        self.fill_diagonal_3_by_3([(0, 3), (3, 6), (6, 9)])
        self.create_solutions()
        return self.grid

    def fill_diagonal_3_by_3(self, range_list):
        """
        Initial 3 x 3 by 3 sections filled in
        Fills the grid with the 1/9 5/9 and 9/9 3x3 areas on sudoku grid
        Provides a unique number for each line and row.
        Should save memory from this way of  recursion
        """
        self.completed_puzzle = copy.deepcopy(self.grid)
        for range_values in range_list:
            nums = list(range(1, 10))
            if type(range_values) is tuple:
                for row in range(range_values[0], range_values[1]):
                    for col in range(range_values[0], range_values[1]):
                        rand_num = random.choice(nums)
                        self.completed_puzzle[row][col] = rand_num
                        nums.remove(rand_num)
        return self.completed_puzzle

    def create_solutions(self):
        """
        Copy the grid to find a solution or multiple solutions
        Get missing numbers in the row lists
        """
        for row in range(len(self.completed_puzzle)):
            available_nums = self.get_missing_numbers_in_row(row)
            for col in range(len(self.completed_puzzle[row])):
                if self.completed_puzzle[row][col] == 0:
                    for num in available_nums:
                        if self.check_row_column_3_by_3(num, (row, col)):
                            self.completed_puzzle[row][col] = num

                            # available_nums.remove(num)

                            if self.find_solution():
                                self.create_solutions()
                                return self.completed_puzzle

                            self.completed_puzzle[row][col] = 0

    def find_solution(self):
        """
        Checking cell to fill in
        If possible to fill in then will set a number,
        otherwise will reset the number to 0
        """
        available_cell = self.find_next_zero()

        if not available_cell:
            return True
        else:
            row, col = available_cell

        available_nums = self.get_missing_numbers_in_row(row)

        for num in available_nums:
            if self.check_row_column_3_by_3(num, (row, col)):
                self.completed_puzzle[row][col] = num

                if self.find_solution():
                    return self.completed_puzzle

                self.completed_puzzle[row][col] = 0

        return False

    def find_next_zero(self):
        """
        Use recursion to check the row for zero
        """
        for row in range(len(self.completed_puzzle)):
            for col in range(len(self.completed_puzzle[row])):
                if self.completed_puzzle[row][col] == 0:
                    return row, col

    def get_missing_numbers_in_row(self, row):
        """
        Use recursion to get the missing numbers in the row
        """
        missing_nums = []
        for num in range(1, 10):
            if num not in self.completed_puzzle[row]:
                missing_nums.append(num)

        random.shuffle(missing_nums)

        return missing_nums

    def check_row_column_3_by_3(self, num, cell):
        """
        Check number is not in the row, column or 3 by 3
        """
        if num in self.completed_puzzle[cell[0]]:
            return False

        nums_in_column = [self.completed_puzzle[row][cell[1]] for row in
                          range(len(self.completed_puzzle))]
        if num in nums_in_column:
            return False

        three_by_three = [self.completed_puzzle[row + ((cell[0] // 3) * 3)][
                              column + ((cell[1] // 3) * 3)] for row in
                          range(3) for
                          column in range(3)]
        if num in three_by_three:
            return False

        return True

    def set_difficulty(self, difficulty):
        """
        Set the difficulty of the puzzle
        """
        match difficulty:
            case 1:
                self.create_puzzle_with_difficulty(Difficulty.EASY.value)
            case 2:
                self.create_puzzle_with_difficulty(Difficulty.MEDIUM.value)
            case 3:
                self.create_puzzle_with_difficulty(Difficulty.HARD.value)

    def create_puzzle_with_difficulty(self, num_of_nums_to_remove):
        """
        Copy the completed puzzle and create a puzzle with missing numbers
        Remove amount of numbers dependent on difficulty set.
        """
        self.create_puzzle()

        self.original_puzzle = copy.deepcopy(self.completed_puzzle)

        for across in self.grid_sections:
            for down in self.grid_sections:
                for num in range(self.missing_num_in_subgrid_range[0],
                                 self.missing_num_in_subgrid_range[1]):
                    row = random.randint(across[0], across[1])
                    col = random.randint(down[0], down[1])
                    if self.original_puzzle[row][col] != 0:
                        self.original_puzzle[row][col] = 0
                        num_of_nums_to_remove -= 1

        while num_of_nums_to_remove > 0:
            row = random.randint(self.row_cell_range[0],
                                 self.row_cell_range[1])
            col = random.randint(self.col_cell_range[0],
                                 self.col_cell_range[1])
            if self.original_puzzle[row][col] != 0:
                self.original_puzzle[row][col] = 0
                num_of_nums_to_remove -= 1

        self.current_puzzle = copy.deepcopy(self.original_puzzle)
        style_puzzle = StylePuzzle(
            self.original_puzzle,
            self.current_puzzle
        )
        style_puzzle.add_puzzle_style()

    def compare_current_puzzle_and_grid(self):
        """
        Compare the set grid and current puzzle.
        If number is part of the grid, must not be overwritten
        """
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] != 0 and self.grid[row][col] == \
                        self.current_puzzle[row][col]:
                    # TODO fix this line
                    print(
                        'The number cannot be overwritten as part of the puzzle.')

    def create_nums_list(self, numbers):
        """
        Create list from user's input
        """
        list_of_nums = numbers.replace(" ", "").rstrip(",").split(",")
        return [int(num) for num in list_of_nums]

    def create_user_puzzle(self, puzzle):
        self.grid = puzzle
        return self.grid
