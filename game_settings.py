import copy
import random
from style_puzzle import StylePuzzle


class GameSettings:
    def __init__(self, completed_puzzle: [list[int]]):
        self.completed_puzzle = completed_puzzle
        self.original_puzzle = [list[int]]
        self.current_puzzle = [list[int]]
        self.grid_sections = [(0, 2), (3, 5), (6, 8)]
        self.missing_num_in_subgrid_range = (0, 5)
        self.row_cell_range = (0, 8)
        self.col_cell_range = (0, 8)
        self.easy = 51
        self.medium = 53
        self.hard = 56
        self.style_puzzle = StylePuzzle(
            self.original_puzzle,
            self.current_puzzle
        )

    def create_puzzle_with_difficulty(self, num_of_nums_removed: int):
        """
        Copy the completed puzzle and create a puzzle with missing numbers
        Remove amount of numbers dependent on difficulty set.
        """
        self.original_puzzle = copy.deepcopy(self.completed_puzzle)

        for across in self.grid_sections:
            for down in self.grid_sections:
                for num in range(self.missing_num_in_subgrid_range[0],
                                 self.missing_num_in_subgrid_range[1]):
                    row = random.randint(across[0], across[1])
                    col = random.randint(down[0], down[1])
                    if self.original_puzzle[row][col] != 0:
                        self.original_puzzle[row][col] = 0
                        num_of_nums_removed -= 1

        while num_of_nums_removed > 0:
            row = random.randint(self.row_cell_range[0],
                                 self.row_cell_range[1])
            col = random.randint(self.col_cell_range[0],
                                 self.col_cell_range[1])
            if self.original_puzzle[row][col] != 0:
                self.original_puzzle[row][col] = 0
                num_of_nums_removed -= 1

        self.current_puzzle = copy.deepcopy(self.original_puzzle)
        self.style_puzzle.add_puzzle_style()

    def set_difficulty(self, difficulty: int):
        """
        Pass the difficulty to create_puzzle_with_difficulty()
        with correct number of missing numbers
        """
        match difficulty:
            case 1:
                self.create_puzzle_with_difficulty(self.easy)
            case 2:
                self.create_puzzle_with_difficulty(self.medium)
            case 3:
                self.create_puzzle_with_difficulty(self.hard)
