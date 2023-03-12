from Grid import *
from pyfiglet import Figlet
from termcolor import colored
from Sudoku import *


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
        print(colored(custom_fig.renderText('SUDOKU'), 'red'))

    def add_initial_options(self):
        """
        Show options for the user to enter their choice
        """
        # self.set_title()
        print(f"\x1b[10;50H1. Play")
        print(f"\x1b[11;50H2. Enter your own puzzle")
        print(f"\x1b[12;50H3. Solve a puzzle")
        print(f"\x1b[13;50H4. Instructions")

        choice = input(f"\x1b[15:50HEnter a number:\n")
        print(f"\x1b[2J")  # Erase entire screen
        print(f"\x1b[H")  # Puts cursor back to home position
        print(f"\x1b[15:50H{choice}", end="\r")
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
