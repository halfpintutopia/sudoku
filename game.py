from grid import Grid
from pyfiglet import Figlet
from termcolor import colored
from sudoku import Sudoku
import time
from screen import on, clear, write, clear_screen
import keyboard
from helper_enums import Instructions, MainMenu, InputPrompt


class Game:
    def __init__(self):
        self.grid = None
        self.initiate_game()

    def initiate_game(self):
        """
        Start game screen
        """
        self.set_title()
        Sudoku().add_grid_style()
        self.add_initial_options()

    def set_title(self):
        """
        Create title for the start screen
        """
        custom_fig = Figlet(font='block')
        print(f"\x1b[1;50H")
        print(colored(custom_fig.renderText('SUDOKU'), 'yellow'))

    def add_initial_options(self):
        """
        Show options for the user to enter their choice
        """
        clear_screen()
        self.set_title()
        on(10, 1, '1. Play')
        on(11, 1, '2. Enter your own puzzle')
        on(12, 1, '3. Solve a puzzle')
        on(13, 1, '4. Instructions')

        choice = 0

        while True:
            try:
                clear(16, 1)
                choice = int(
                    self.add_input_at_position(15, 1, 'Enter a number: '))
            except ValueError as e:
                print(f"Please choose one of the options. 1, 2, 3, or 4")
                continue
            else:
                break

        match choice:
            case 1:
                for row in range(10, 17):
                    clear(row, 55)

                self.create_username()
                # self.choose_difficulty()
            case 2:
                print('You selected 2')
            case 3:
                print('You selected 3')
            case 4:
                self.show_instructions()

    def create_username(self):
        username = int(input(f"\x1b[10;55HEnter a username: \x1b[11;55H"))

    def choose_difficulty(self):
        """
        Input should allow the user to choose the difficulty of the game
        """
        clear(15, 55)
        clear(16, 55)

        on(10, 55, 'Please choose difficulty')
        on(11, 55, '1 for easy')
        on(12, 55, '2 for medium')
        on(13, 55, '3 for hard')

        while True:
            try:
                difficulty_level = int(input(f"\x1b[15;55HEnter a number: "))
                # self.validate_difficulty_input(difficulty_level)
                # break
            except ValueError as e:
                print(f"Please choose one of the options. 1, 2, 3, or 4")
                continue

        # difficulty_level = input("Enter number: \n")
        # # self.validate_difficulty_input(difficulty_level)
        # # break
        # if self.validate_difficulty_input(difficulty_level):
        #     print(int(difficulty_level))
        #     break

    def show_main_menu(self, row, col):
        """
        Create the main menu
        Placement dependent on where it should be positioned at row and col
        """
        clear_screen()
        self.set_title()
        on({row}, {col}, MainMenu.PLAY.value)
        on({row}, {col}, MainMenu.ENTER_OWN.value)
        on({row}, {col}, MainMenu.SOLVE.value)
        on({row}, {col}, MainMenu.INSTRUCTIONS.value)

    def show_instructions(self):
        """
        Show the instructions for the game, when option chosen
        """
        clear_screen()
        self.set_title()
        on(10, 1, Instructions.FIRST_LINE.value)
        on(11, 1, Instructions.SECOND_LINE.value)
        on(12, 1, Instructions.THIRD_LINE.value)
        on(13, 1, Instructions.FOURTH_LINE.value)

        self.add_input_at_position(15, 1, InputPrompt.PRESS_ENTER.value)
        self.add_initial_options()

    def add_input_at_position(self, row, col, string):
        """
        Show the input
        A helper function to return an input at a set row and column
        """
        return input(f"\x1b[{row};{col}H{string}\x1b[{row + 1};{col}H")
