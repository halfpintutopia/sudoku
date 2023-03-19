from sudoku import Sudoku
from screen import on, clear, clear_screen, write_input, \
    clear_screen_from_pos, set_title
from string_enums import MainMenu, InputPrompt, \
    DifficultyPrompt
from user import User
from validation import validate_number_guess, validate_coordinates, \
    validate_difficulty_input, validate_grid_cell, validate_menu_option, \
    validate_row_for_duplicates, validate_row, validate_list_contains_integers
from style_puzzle import StylePuzzle
import copy
from global_constants import *


class Game(Sudoku):
    def __init__(self):
        super().__init__()
        self.cell = None
        self.user = User()
        self.guess = None
        self.row = None
        self.col = None
        self.grid = None
        self.initiate_game()
        self.lower_unicode_to_one_base = 96
        self.upper_unicode_to_one_base = 64
        self.reset_to_match_index = 1

    def initiate_game(self):
        """
        Start game screen
        """
        self.add_initial_options()

    def add_initial_options(self):
        """
        Show options for the user to enter their choice
        """
        set_title()
        on(10, 5, MainMenu.PLAY.value)
        on(11, 5, MainMenu.ENTER_OWN.value)
        on(12, 5, MainMenu.INSTRUCTIONS.value)

        while True:
            clear(15, 5)
            option = write_input(14, 5, InputPrompt.NUMBER.value)
            if validate_menu_option(option):
                self.selected_user_choice(int(option))
                break

    def selected_user_choice(self, option):
        """
        Take the chosen option and run the function accordingly
        """
        match option:
            case 1:
                for row in range(10, 17):
                    clear(row, 55)

                self.run_play()
            case 2:
                for row in range(10, 17):
                    clear(row, 55)

                self.solve_user_puzzle()
            case 3:
                for row in range(10, 17):
                    clear(row, 55)

                self.show_instructions()

    def run_play(self):
        """
        Runs when the play option has been chosen
        """
        print(MainMenu.LOADING.value)
        self.user.create_username()

        clear_screen()
        set_title()
        on(10, LEFT_MARGIN, 'Hello ' + self.user.get_username())
        self.choose_difficulty()
        self.guess_cell()

    def guess_cell(self):
        """
        Prompt for player to add their guess
        """
        on(10, 55, 'Enter row number')
        on(11, 55, 'and one column letter.')
        on(12, 55, 'e.g. 4E or e4')

        on(14, 55, 'XS for solution')
        on(15, 55, 'X to exit')

        while True:
            clear(18, 55)
            option = write_input(17, 55, 'Enter number and letter:')
            if option.lower() == 'x':
                self.add_initial_options()
            elif option.lower() == 'xs':
                self.solve_puzzle()
            elif validate_coordinates(option):
                self.set_coordinates(option)
                self.guess_number()
                break

    def guess_number(self):
        """
        Prompt for player to choose a number to place in cell
        """
        on(10, 55, 'Enter number 1 - 9')

        on(12, 55, MainMenu.EXIT.value)

        while True:
            clear(15, 55)
            clear(16, 55)
            clear(17, 55)
            clear(18, 55)
            clear(19, 55)
            clear(20, 55)
            clear(21, 55)
            option = write_input(14, 55, f"Add number to {self.cell}:")
            if option == 'x' or option == 'X':
                self.add_initial_options()
            elif validate_number_guess(option):
                self.set_guess(option)
                self.set_number_to_coordinates()
                break

    def set_number_to_coordinates(self):
        """
        Add the number to the cell chosen by the user
        Update the puzzle and then style the grid
        """
        if validate_grid_cell(self.original_puzzle, self.row, self.col):
            self.current_puzzle[self.row][self.col] = self.guess
            style_puzzle = StylePuzzle(
                self.original_puzzle,
                self.current_puzzle
            )
            clear_screen()
            set_title()
            style_puzzle.add_puzzle_style()
            self.guess_cell()
        else:
            write_input(20, 55, "Enter to continue..")
            self.guess_cell()

    def set_guess(self, option):
        """
        Set the guess to the instance
        """
        self.guess = int(option)

    def set_coordinates(self, cell):
        """
        Set the coordinates to wait for the number input to be put in the cell
        Minus one needs to be taken from the values of inputs
        due to index starting at 0
        """
        self.cell = cell.upper()
        letter = ''
        if cell[0].isdigit() and cell[1].isalpha():
            if 0 <= (int(cell[0]) - 1) <= 8:
                self.row = (int(cell[0]) - 1)
            letter = cell[1]
        elif cell[0].isalpha() and cell[1].isdigit():
            letter = cell[0]
            if 0 <= (int(cell[1]) - 1) <= 8:
                self.row = (int(cell[1]) - 1)

        if letter.isupper():
            self.col = ord(letter) - 64 - 1
        else:
            self.col = ord(letter) - 96 - 1

    def choose_difficulty(self):
        """
        Input should allow the user to choose the difficulty of the game
        """
        on(12, LEFT_MARGIN, DifficultyPrompt.CHOOSE.value)
        on(13, LEFT_MARGIN, DifficultyPrompt.EASY.value)
        on(14, LEFT_MARGIN, DifficultyPrompt.MEDIUM.value)
        on(15, LEFT_MARGIN, DifficultyPrompt.HARD.value)

        while True:
            clear(17, LEFT_MARGIN)
            clear(18, LEFT_MARGIN)

            difficulty_level = write_input(17, LEFT_MARGIN,
                                           InputPrompt.NUMBER.value)

            if validate_difficulty_input(difficulty_level):
                self.set_difficulty(int(difficulty_level))
                break

    def show_instructions(self):
        """
        Show the instructions for the game, when option chosen
        """
        clear_screen_from_pos(10, LEFT_MARGIN)
        on(10, LEFT_MARGIN, 'A Sudoku puzzle is created with a 9 by 9 square')
        on(11, LEFT_MARGIN, '(9 rows and 9 columns).')
        on(12, LEFT_MARGIN, 'The 9 x 9 square is divided into 3 by 3 areas')
        on(13, LEFT_MARGIN, 'a total of 9 x 3 by 3 areas.')
        on(14, LEFT_MARGIN, 'Each row, column and 3 x 3 area')
        on(15, LEFT_MARGIN, 'must contain numbers 1 - 9.')
        on(16, LEFT_MARGIN, 'Numbers cannot be repeated in the row')
        on(17, LEFT_MARGIN, 'column nor 3 by 3 area.')

        write_input(19, LEFT_MARGIN, InputPrompt.PRESS_ENTER.value)
        self.add_initial_options()

    def solve_user_puzzle(self):
        """
        Prompt the user to add 9 rows, to solve a puzzle
        """
        clear_screen_from_pos(10, LEFT_MARGIN)
        on(10, LEFT_MARGIN, 'Every row must contain 9 numbers,')
        on(11, LEFT_MARGIN, 'each number must be  separated by a comma.')
        on(12, LEFT_MARGIN, 'Each number must be 1 to 9.')
        on(13, LEFT_MARGIN, 'Use 0 for a blank.')
        on(14, LEFT_MARGIN, 'e.g. 4,7,0,0,2,6,9,0,0')
        on(16, LEFT_MARGIN, 'X to exit')
        self.original_puzzle = []
        for row in range(9):
            # clear_screen_from_pos(14, 1)
            while True:
                clear(19, LEFT_MARGIN, 80)
                puzzle_row = write_input(18, LEFT_MARGIN, 'Enter row ' +
                                         str(row + 1))
                if puzzle_row.lower() == 'x':
                    self.add_initial_options()
                list_of_nums = puzzle_row.replace(" ", "").rstrip(",").split(
                    ",")
                if validate_list_contains_integers(list_of_nums):
                    if validate_row(list_of_nums):
                        current_row = self.create_nums_list(puzzle_row)
                        if validate_row_for_duplicates(current_row):
                            self.original_puzzle.append(current_row)
                            break
        self.completed_puzzle = copy.deepcopy(self.original_puzzle)
        on(20, LEFT_MARGIN, 'Just one moment, generating solution')
        self.solve_puzzle()

    def solve_puzzle(self):
        """
        Provides the solution and then styles the grid
        """
        if self.completed_puzzle is None:
            self.completed_puzzle = copy.deepcopy(self.original_puzzle)
        self.create_solutions()
        style_puzzle = StylePuzzle(
            self.original_puzzle,
            self.completed_puzzle
        )
        clear_screen()
        set_title()
        style_puzzle.add_puzzle_style()
        if self.original_puzzle == self.completed_puzzle:
            on(10, 55, "Unsolvable")
            on(11, 55, "Error in the puzzle")
            on(12, 55, "Check the numbers in rows")
            write_input(14, 55, "Press Enter to exit")
        else:
            write_input(10, 55, "Press Enter to exit")
        self.add_initial_options()
