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
        print(f"\x1b[1;50H")
        print(colored(custom_fig.renderText('SUDOKU'), 'blue'))

    def add_initial_options(self):
        """
        Show options for the user to enter their choice
        """
        # self.set_title()
        self.on(10, 55, '1. Play')
        self.on(11, 55, '2. Enter your own puzzle')
        self.on(12, 55, '3. Solve a puzzle')
        self.on(13, 55, '4. Instructions')

        choice = 0

        while True:
            try:
                self.clear_line(16, 55)
                print(f"\x1b[15;55H")
                choice = int(input(f"\x1b[15;55HEnter a number: "))
            except ValueError as e:
                print(f"Please choose one of the options. 1, 2, 3, or 4")
                continue
            else:
                break

        match choice:
            case 1:
                print('You selected 1')
            case 2:
                print('You selected 2')
            case 3:
                print('You selected 3')
            case 4:
                print('You selected 4')



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

    def on(self, row, col, string, num_of_blanks=25):
        """
        Combine clear_line and write_line
        """
        self.clear_line(row, col, num_of_blanks)
        self.write_line(row, col, string)

    def clear_line(self, row, col, num_of_blanks=25):
        """
        Before writing a new line, clears the line by over-writing with blank spaces
        This is used for the right side of the screen
        Set number of blank spaces to be more or less dependent on the number of character needed to be overwritten
        """
        print(f"\x1b[{row};{col}H{' ' * num_of_blanks}")

    def write_line(self, row, col, string):
        """
        Add text at a particular row and column of the screen
        """
        print(f"\x1b[{row};{col}H{string}")
