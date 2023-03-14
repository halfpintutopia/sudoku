from grid import Grid
from pyfiglet import Figlet
from termcolor import colored
from sudoku import Sudoku
import time
from screen import on, clear, write


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
        # self.set_title()
        on(10, 55, '1. Play')
        on(11, 55, '2. Enter your own puzzle')
        on(12, 55, '3. Solve a puzzle')
        on(13, 55, '4. Instructions')

        choice = 0

        while True:
            try:
                clear(16, 55)
                choice = int(input(f"\x1b[15;55HEnter a number: \x1b[16;55H"))
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
                print('You selected 4')

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
            # else:
        # sudoku = Sudoku()
        # self.original_puzzle = sudoku.

        # print(f"\x1b[15;55H")
        # choice = input(f"\x1b[15;55HEnter a number: ")

        # print(f"\x1b[2J")  # Erase entire screen
        # print(f"\x1b[H")  # Puts cursor back to home position
        # print(f"\x1b[15;50H{choice}", end="\r")
        # print("1. Play")
        # print("2. Enter your own puzzle")
        # print("3. Solve a puzzle")
        # print("4. Instructions\n")

        # difficulty_level = input("Enter number: \n")
        # # self.validate_difficulty_input(difficulty_level)
        # # break
        # if self.validate_difficulty_input(difficulty_level):
        #     print(int(difficulty_level))
        #     break


