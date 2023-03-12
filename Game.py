from Grid import *
from pyfiglet import Figlet
from termcolor import colored
from Sudoku import *
import time


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
        colored_text = colored(custom_fig.renderText('SUDOKU'), 'blue')
        print(f"\x1b[1;20H{colored_text}")

    def add_initial_options(self):
        """
        Show options for the user to enter their choice
        """
        # self.set_title()
        print(f"\x1b[10;55H1. Play")
        print(f"\x1b[11;55H2. Enter your own puzzle")
        print(f"\x1b[12;55H3. Solve a puzzle")
        print(f"\x1b[13;55H4. Instructions")

        print(f"\x1b[10;55H{' ' * 25}")
        print(f"\x1b[10;55H1. Test-1")

        print(f"\x1b[11;55H{' ' * 25}")
        print(f"\x1b[11;55H2. Test-2")

        print(f"\x1b[12;55H{' ' * 25}")
        print(f"\x1b[12;55H3. Test-3")

        print(f"\x1b[13;55H{' ' * 25}")
        print(f"\x1b[13;55H4. Test-4")

        print(f"\x1b[15;55H")
        choice = input(f"\x1b[15;55HEnter a number please: ")
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
