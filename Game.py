from Grid import *
from pyfiglet import Figlet
from termcolor import colored


class Game:
    def __init__(self):
        self.grid = None
        self.initiate_game()

    def initiate_game(self):
        """
        Start game screen
        """
        self.set_title()
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
        print(f"\x1b[30;0H1. Play")
        print(f"\x1b[31;0H2. Enter your own puzzle")
        print(f"\x1b[32;0H3. Solve a puzzle")
        print(f"\x1b[33;0H4. Instructions")

        choice = input(f"\x1b[35:0HEnter a number:\n")
        print(f"\x1b[35:0H{choice}")
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
