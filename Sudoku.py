import copy
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
        pprint(self.grid)
        return self.grid

    def create_solutions(self):
        """
        Copy the grid to find a solution or multiple solutions
        Get missing numbers in the row lists
        """
        # new_sudoku = copy.deepcopy(self.grid)
        # for row in range(len(new_sudoku)):
        #     available_nums = self.get_missing_numbers_in_row(row)
        #     for col in range(len(new_sudoku[row])):
        #         if new_sudoku[row][col] == 0:
        #             for num in available_nums:
        #                 if self.check_row_column_3_by_3(num, (row, col)):
        #                     new_sudoku[row][col] = num
        #                     # available_nums.remove(num)
        #
        #                     # if self.find_solution():
        #
        #                 prev_col = self.remove_last_filled_in_zero((row, col))
        #                 new_sudoku[row][prev_col] = 0
        # new_sudoku = copy.deepcopy(self.grid)
        for row in range(len(self.grid)):
            available_nums = self.get_missing_numbers_in_row(row)
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 0:
                    for num in available_nums:
                        if self.check_row_column_3_by_3(num, (row, col)):
                            self.grid[row][col] = num

                            # available_nums.remove(num)

                            if self.find_solution():
                                self.create_solutions()
                                return self.grid

                            self.grid[row][col] = 0

                        # prev_col = self.remove_last_filled_in_zero((row, col))
                        # self.grid[row][prev_col] = 0
                # else:
                #     if self.remove_last_filled_in_zero((row, col)):
                #         col_num = self.remove_last_filled_in_zero((row, col))
                #         new_sudoku[row][col_num] = 0
                # not_poss_num = available_nums[0]
                # available_nums.pop(0)
                # available_nums.append(not_poss_num)
                # for num in available_nums:
                #     if self.check_row_column_3_by_3(num, (row, col_num)):
                #         new_sudoku[row][col_num] = num
                #         print(f"first num = {num}")
                # available_nums.remove(num)
                # if self.check_row_column_3_by_3(num, (row, col)):
                #     new_sudoku[row][col] = num
                #     print(f"second num = {num}")
                # available_nums.remove(num)

        #     print(available_nums)
        # pprint(self.grid)

    def find_solution(self):
        """
        Checking cell to fill in
        If possible to fill in then will set a number otherwise will reset the number to 0
        """
        available_cell = self.find_next_zero()

        if not available_cell:
            return True
        else:
            row, col = available_cell

        available_nums = self.get_missing_numbers_in_row(row)

        for num in available_nums:
            if self.check_row_column_3_by_3(num, (row, col)):
                self.grid[row][col] = num

                if self.find_solution():
                    return self.grid

                self.grid[row][col] = 0

        return False

    def remove_last_filled_in_zero(self, cell):
        """
        Use recursion to find the previous column in the row that was a 0 in the original grid
        """
        if cell[1] != 0:
            for i in range(cell[1] - 1, -1, -1):
                if self.grid[cell[0]][i] == 0:
                    print(f"i = column:  {cell[0]}, {i}")
                    return i

        print(f"return original: {cell[0]}, {cell[1]}")
        return False

    def find_next_zero(self):
        """
        Use recursion to check the row for zero
        """
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 0:
                    return row, col

    def get_missing_numbers_in_row(self, row):
        """
        Use recursion to get the missing numbers in the row
        """
        missing_nums = []
        for num in range(1, 10):
            if num not in self.grid[row]:
                missing_nums.append(num)

        random.shuffle(missing_nums)

        return missing_nums

    def check_row_column_3_by_3(self, num, cell):
        """
        Check number is not in the row, column or 3 by 3
        """
        if num in self.grid[cell[0]]:
            return False

        nums_in_column = [self.grid[row][cell[1]] for row in range(len(self.grid))]
        # print(nums_in_column)
        if num in nums_in_column:
            return False

        three_by_three = [self.grid[row + ((cell[0] // 3) * 3)][column + ((cell[1] // 3) * 3)] for row in range(3) for
                          column in range(3)]
        # print(three_by_three)
        if num in three_by_three:
            return False

        return True
