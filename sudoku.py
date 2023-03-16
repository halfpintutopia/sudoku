import copy
from pprint import pprint
import random
from termcolor import colored
from helper_enums import Difficulty, TermcolorSettings


class Sudoku:
    def __init__(self):
        self.current_puzzle = None
        self.puzzle = None
        self.grid = None
        self.create_blank_sudoku()

    def create_blank_sudoku(self):
        self.grid = [[0 for x in range(9)] for y in range(9)]
        return self.grid

    def creat_puzzle_with_difficulty(self, difficulty):
        self.create_puzzle()

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

    def validate_difficulty_input(self, difficulty):
        # print(type(int(difficulty)))
        try:
            if difficulty.isdigit():
                number = int(difficulty)
            else:
                raise ValueError(f"Please enter a number")
            if not 1 <= number <= 3:
                raise ValueError(f"Please enter a number between 1 and 3")
        except ValueError as e:
            print(f"Invalid input: {e}, please try again.\n")
            return False

        return True

    def solve_user_puzzle(self):
        """
        Prompt the user to add 9 rows, to solve a puzzle
        """
        print("Sudoku puzzles are a 9 by 9 grid.")
        print("Each puzzle has 9 rows. There are 9 numbers in each row.")
        print("Please enter each row when prompted.")
        print("Enter 9 numbers separated by a comma.")
        print("Each number must be between 0-9. Please use 0 for a blank.")
        print("e.g. 4,7,0,0,2,6,9,0,0")
        puzzle = []
        for row in range(len(self.grid)):
            while True:
                puzzle_row = input(f"Enter row {row + 1} of your puzzle.\n")
                current_row = []
                if self.create_nums_list(puzzle_row):
                    current_row = self.create_nums_list(puzzle_row)
                if self.check_amount_of_nums(current_row):
                    print("you have entered the correct number")

    def create_nums_list(self, numbers):
        """
        Create list from user's input
        """
        list_of_nums = numbers.replace(" ", "").rstrip(",").split(",")
        if self.check_inputs_are_numbers(list_of_nums):
            return [int(num) for num in list_of_nums]

        return False

    def check_amount_of_nums(self, numbers):
        """
        Validates the string of numbers inputted
        Removes all spaces from the string if the user has entered them
        Splits the string up and creates a list
        """
        try:
            if not len(numbers) == 9:
                raise ValueError(f"You have entered {len(numbers)}. Please enter 9 numbers per row")
        except ValueError as e:
            print(f"Invalid input: {e}, please try again")
            return False

        return True

    def check_inputs_are_numbers(self, numbers):
        """
        Check the list of numbers are all integers
        """
        for num in numbers:
            try:
                if isinstance(num, int):
                    continue
                else:
                    raise ValueError(f"Please enter a number")
            except ValueError as e:
                print(f"Invalid input: {e}, please try again")
                return False

        return True

    def solve_puzzle(self):
        puzzle = [
            [4, 7, 0, 0, 2, 6, 9, 0, 0],
            [0, 0, 5, 0, 0, 0, 0, 0, 0],
            [1, 0, 6, 0, 0, 0, 0, 0, 8],
            [0, 3, 0, 0, 0, 9, 0, 0, 7],
            [0, 8, 0, 5, 0, 0, 0, 0, 4],
            [0, 0, 2, 0, 1, 0, 0, 0, 0],
            [2, 0, 0, 6, 0, 0, 7, 4, 0],
            [8, 4, 0, 0, 5, 2, 0, 0, 1],
            [0, 5, 9, 0, 0, 0, 8, 0, 2]
        ]
        self.create_user_puzzle(puzzle)
        self.find_solution()
        self.add_grid_style()
        # print(f"\x1b[35:0H{self.add_grid_style()}")

    def create_user_puzzle(self, puzzle):
        self.grid = puzzle
        return self.grid

    def add_grid_style(self):
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

    def add_puzzle_style(self):
        """
        Print out the grid with style and headings for columns and rows
        """
        grid_string = "    "
        index = 1
        for letter in range(ord('A'), ord('J')):
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
                    if self.grid[row][column] != 0 and self.grid[row][column] == self.current_puzzle[row][column]:
                        grid_string += "  " + colored(str(self.grid[row][column]), 'yellow', attrs=['bold']) + " "
                    elif self.grid[row][column] == 0 and self.current_puzzle[row][column] != self.grid[row][column] and \
                            self.current_puzzle[row][column] != 0:
                        grid_string += "  " + colored(str(self.current_puzzle[row][column]), 'blue',
                                                      attrs=['bold']) + " "
                    else:
                        grid_string += "  " + colored(str(self.grid[row][column]), attrs=['bold']) + " "
                else:
                    if self.grid[row][column] != 0 and self.grid[row][column] == self.current_puzzle[row][column]:
                        grid_string += "  " + colored(str(self.grid[row][column]), 'yellow', attrs=['bold']) + " "
                    elif self.grid[row][column] == 0 and self.current_puzzle[row][column] != self.grid[row][column] and \
                            self.current_puzzle[row][column] != 0:
                        grid_string += "  " + colored(str(self.current_puzzle[row][column]), 'blue',
                                                      attrs=['bold']) + " "
                    else:
                        grid_string += "  " + colored(str(self.grid[row][column]), attrs=['bold']) + " "
            grid_string += "\n"

            if (row + 1) % 3 == 0 and (row + 1) != 9:
                grid_string += "   " + "-" * 43 + "\n"

        print(grid_string)
        # return grid_string

    def set_difficulty(self, difficulty):
        match difficulty:
            case 1:
                self.create_new_puzzle(Difficulty.EASY.value)
            case 2:
                self.create_new_puzzle(Difficulty.MEDIUM.value)
            case 3:
                self.create_new_puzzle(Difficulty.HARD.value)

    def create_new_puzzle(self, number_of_zeroes):
        self.create_puzzle()
        threes = [(0, 2), (3, 5), (6, 8)]
        for across in threes:
            for down in threes:
                for num in range(0, 5):
                    row = random.randint(across[0], across[1])
                    col = random.randint(down[0], down[1])
                    if self.grid[row][col] != 0:
                        self.grid[row][col] = 0
                        number_of_zeroes -= 1

        while number_of_zeroes > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.grid[row][col] != 0:
                self.grid[row][col] = 0
                number_of_zeroes -= 1

        self.grid = [[5, 3, 0, 0, 0, 4, 6, 0, 2],
                     [0, 1, 0, 0, 3, 2, 0, 5, 0],
                     [0, 2, 0, 0, 0, 0, 0, 0, 3],
                     [8, 0, 2, 9, 0, 0, 0, 0, 6],
                     [0, 0, 0, 0, 0, 1, 0, 0, 9],
                     [3, 0, 0, 0, 5, 0, 0, 2, 8],
                     [7, 0, 0, 0, 0, 0, 0, 4, 0],
                     [0, 0, 0, 0, 0, 0, 0, 6, 0],
                     [1, 0, 3, 2, 0, 7, 9, 0, 5]]

        pprint(self.grid)
        self.current_puzzle = copy.deepcopy(self.grid)
        self.current_puzzle[1][0] = 1
        pprint(self.grid)
        self.add_puzzle_style()

    def compare_current_puzzle_and_grid(self):
        """
        Compare the set grid and current puzzle.
        If number is part of the grid, must not be overwritten
        """
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] != 0 and self.grid[row][col] == self.current_puzzle[row][col]:
                    print('The number cannot be overwritten as part of the puzzle.')
                    # return False

        # return True
