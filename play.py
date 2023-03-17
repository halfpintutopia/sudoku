from screen import on, clear, write_input, clear_screen_from_pos, set_title, \
    clear_right_side
from helper_enums import InputPrompt, Username, DifficultyPrompt, \
    Instructions, Guess, MainMenu
import re
from user import User
from validation import validate_username, validate_menu_option, \
    validate_difficulty_input, validate_coordinates, validate_number_guess
from sudoku import Sudoku


class Play:
    def __init__(self):
        self.username = None
        self.row = None
        self.col = None
        self.guess = None
        self.menu_item_play = '1. Play'
        self.menu_item_enter_own = '2. Enter your own puzzle'
        self.menu_item_solve = '3. Solve a puzzle'
        self.menu_item_instructions = '4. Instructions'
        self.menu_item_loading = 'Just one moment... '
        self.menu_item_exit = 'X to exit'
        self.user = User(self.username)
        self.sudoku = Sudoku()

    def initiate_game(self):
        """
        Start game screen
        """
        set_title()
        self.add_initial_options()

    def add_initial_options(self):
        """
        Show options for the user to enter their choice
        """
        clear_screen_from_pos(10, 1)
        on(10, 1, self.menu_item_play)
        on(11, 1, self.menu_item_enter_own)
        on(12, 1, self.menu_item_solve)
        on(13, 1, self.menu_item_instructions)
        while True:
            clear(16, 1)
            option = write_input(15, 1, InputPrompt.NUMBER.value)
            if validate_menu_option(option):
                self.selected_user_choice(int(option))
                break

    def selected_user_choice(self, option):
        """
        Take the chosen option and run the function accordingly
        """

        match option:
            case 1:
                clear_screen_from_pos(10, 1)
                self.run_play()
            case 2:
                print('You selected 2')
            case 3:
                print('You selected 3')
            case 4:
                self.show_instructions()

    def get_username(self):
        """
        Get username from user input
        """
        clear_screen_from_pos(10, 1)
        on(10, 1, Username.PROMPT_1.value)
        on(11, 1, Username.PROMPT_2.value)
        on(12, 1, Username.PROMPT_3.value)

        while True:
            username = write_input(14, 1, InputPrompt.USERNAME.value)

            if validate_username(username):
                self.username = username
                # self.get_last_entry()
                # game_id = self.get_last_id_entry()
                # print(f"game id = {game_id}")
                break

        print(self.username)
        return self.username
        # print(f"Hello {self.username}")

    def run_play(self):
        """
        Runs when the play option has been chosen
        """
        print(self.menu_item_loading)
        self.get_username()
        clear_screen_from_pos(10, 1)
        on(10, 1, 'Hello ' + self.username)
        self.choose_difficulty()
        self.guess_cell()

    def choose_difficulty(self):
        """
        Input should allow the user to choose the difficulty of the game
        """
        on(12, 1, DifficultyPrompt.CHOOSE.value)
        on(13, 1, DifficultyPrompt.EASY.value)
        on(14, 1, DifficultyPrompt.MEDIUM.value)
        on(15, 1, DifficultyPrompt.HARD.value)

        while True:
            clear(16, 1)
            clear(17, 1)

            difficulty_level = write_input(16, 1, InputPrompt.NUMBER.value)

            if validate_difficulty_input(difficulty_level):
                clear_screen_from_pos(10, 1)
                self.sudoku.set_difficulty(int(difficulty_level))
                break

    def show_instructions(self):
        """
        Show the instructions for the game, when option chosen
        """
        clear_screen_from_pos(10, 1)
        on(10, 1, Instructions.FIRST_LINE.value)
        on(11, 1, Instructions.SECOND_LINE.value)
        on(12, 1, Instructions.THIRD_LINE.value)
        on(13, 1, Instructions.FOURTH_LINE.value)

        write_input(15, 1, InputPrompt.PRESS_ENTER.value)
        self.add_initial_options()

    def guess_cell(self):
        """
        Prompt for player to add their guess
        """
        clear_right_side()
        on(10, 55, 'Please enter one row number')
        on(11, 55, 'and one column letter.')
        on(12, 55, 'e.g. 4E or e4')
        on(14, 55, MainMenu.EXIT.value)

        while True:
            clear(17, 55)
            option = write_input(16, 55, 'Enter number and letter:')
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
        on(10, 55, 'Please enter a number (1-9)')

        on(12, 55, MainMenu.EXIT.value)

        while True:
            clear(15, 55)
            option = write_input(14, 55, InputPrompt.NUMBER.value)
            if option == 'x' or option == 'X':
                self.add_initial_options()
            elif validate_number_guess(option):
                self.set_guess(option)
                self.set_number_to_coordinates()
                break

    def set_number_to_coordinates(self):
        if self.sudoku.validate_grid_cell(self.row, self.col):
            self.sudoku.current_puzzle[self.row][self.col] = self.guess
            self.sudoku.add_puzzle_style()
            self.guess_cell()
        else:
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
