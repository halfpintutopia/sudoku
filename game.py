from grid import Grid
from pyfiglet import Figlet
from termcolor import colored
from sudoku import Sudoku
import time
from screen import on, clear, write, clear_screen, write_input, \
    clear_screen_from_pos
from helper_enums import Instructions, MainMenu, InputPrompt, DifficultyPrompt
from user import User


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
        # self.show_main_menu()
        on(10, 1, '1. Play')
        on(11, 1, '2. Enter your own puzzle')
        on(12, 1, '3. Solve a puzzle')
        on(13, 1, '4. Instructions')

        while True:
            try:
                clear(16, 1)
                option = int(write_input(15, 1, 'Enter a number: '))
            except ValueError as e:
                print(f"Please choose one of the options. 1, 2, 3, or 4")
                continue
            else:
                self.selected_user_choice(option)
                break

    def selected_user_choice(self, option):
        match option:
            case 1:
                for row in range(10, 17):
                    clear(row, 55)

                self.run_play()
            case 2:
                print('You selected 2')
            case 3:
                print('You selected 3')
            case 4:
                self.show_instructions()

    def run_play(self):
        print(f"Just one sec... ")
        User().create_username()

    def choose_difficulty(self):
        """
        Input should allow the user to choose the difficulty of the game
        """
        clear(15, 55)
        clear(16, 55)

        on(10, 55, DifficultyPrompt.CHOOSE.value)
        on(11, 55, DifficultyPrompt.EASY.value)
        on(12, 55, DifficultyPrompt.MEDIUM.value)
        on(13, 55, DifficultyPrompt.HARD.value)

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

        write_input(15, 1, InputPrompt.PRESS_ENTER.value)
        self.add_initial_options()
