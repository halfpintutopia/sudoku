from sudoku import Sudoku
from screen import on, clear, clear_screen, write_input, \
    clear_screen_from_pos, clear_right_side, set_title
from helper_enums import MainMenu, InputPrompt, \
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
        on(10, left_margin, 'Hello ' + self.user.get_username())
        self.choose_difficulty()
        self.guess_cell()

    def guess_cell(self):
        """
        Prompt for player to add their guess
        """
        clear_right_side()
        on(10, 55, 'Enter row number')
        on(11, 55, 'and one column letter.')
        on(12, 55, 'e.g. 4E or e4')
        on(14, 55, MainMenu.EXIT.value)

        while True:
            clear(17, 55)
            option = write_input(16, 55, 'Enter number and letter:')  # near
            # perfect character length
            if option == 'x' or option == 'X':
                self.add_initial_options()
            elif validate_coordinates(option):
                self.set_coordinates(option)
                self.guess_number()
                break

    def guess_number(self):
        """
        Prompt for player to choose a number to place in cell
        """
        clear_right_side()
        on(10, 55, 'Enter number 1 - 9')

        on(12, 55, MainMenu.EXIT.value)

        while True:
            clear(15, 55)
            option = write_input(14, 55, 'Add number:')
            if option == 'x' or option == 'X':
                self.add_initial_options()
            elif validate_number_guess(option):
                self.set_guess(option)
                self.set_number_to_coordinates()
                break

    def set_number_to_coordinates(self):
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
        self.guess = int(option)

    def set_coordinates(self, cell):
        """
        Set the coordinates to wait for the number input to be put in the cell
        Minus one needs to be taken from the values of inputs
        due to index starting at 0
        """
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
        on(12, left_margin, DifficultyPrompt.CHOOSE.value)
        on(13, left_margin, DifficultyPrompt.EASY.value)
        on(14, left_margin, DifficultyPrompt.MEDIUM.value)
        on(15, left_margin, DifficultyPrompt.HARD.value)

        while True:
            clear(17, left_margin)
            clear(18, left_margin)

            difficulty_level = write_input(17, left_margin,
                                           InputPrompt.NUMBER.value)

            if validate_difficulty_input(difficulty_level):
                self.set_difficulty(int(difficulty_level))
                break

    def show_instructions(self):
        """
        Show the instructions for the game, when option chosen
        """
        clear_screen_from_pos(10, left_margin)
        on(10, left_margin, 'A Sudoku puzzle is created with a 9 by 9 square')
        on(11, left_margin, '(9 rows and 9 columns).')
        on(12, left_margin, 'The 9 x 9 square is divided into 3 by 3 areas')
        on(13, left_margin, 'a total of 9 x 3 by 3 areas.')
        on(14, left_margin, 'Each row, column and 3 x 3 area')
        on(15, left_margin, 'must contain numbers 1 - 9.')
        on(16, left_margin, 'Numbers cannot be repeated in the row')
        on(17, left_margin, 'column nor 3 by 3 area.')

        write_input(19, left_margin, InputPrompt.PRESS_ENTER.value)
        self.add_initial_options()

    def solve_user_puzzle(self):
        """
        Prompt the user to add 9 rows, to solve a puzzle
        """
        clear_screen_from_pos(10, left_margin)
        on(10, left_margin, 'Every row must contain 9 numbers,')
        on(11, left_margin, 'each number must be  separated by a comma.')
        on(12, left_margin, 'Each number must be 1 to 9.')
        on(13, left_margin, 'Use 0 for a blank.')
        on(14, left_margin, 'e.g. 4,7,0,0,2,6,9,0,0')
        self.original_puzzle = []
        for row in range(9):
            clear_screen_from_pos(14, 1)
            while True:
                clear(15, left_margin, 80)
                puzzle_row = write_input(16, left_margin, 'Enter row ' +
                                         str(row + 1))
                list_of_nums = puzzle_row.replace(" ", "").rstrip(",").split(
                    ",")
                if validate_list_contains_integers(list_of_nums):
                    if validate_row(list_of_nums):
                        current_row = self.create_nums_list(puzzle_row)
                        if validate_row_for_duplicates(current_row):
                            self.original_puzzle.append(current_row)
                            break
        self.completed_puzzle = copy.deepcopy(self.original_puzzle)
        on(20, left_margin, 'Just one moment, generating solution')
        self.solve_puzzle()

    def solve_puzzle(self):
        self.completed_puzzle = copy.deepcopy(self.original_puzzle)
        self.create_solutions()
        style_puzzle = StylePuzzle(
            self.original_puzzle,
            self.completed_puzzle
        )
        clear_screen()
        set_title()
        style_puzzle.add_puzzle_style()
        on(10, 55, 'X to exit to main menu')
        write_input(10, 55, InputPrompt.PRESS_ENTER.value)
        self.add_initial_options()
