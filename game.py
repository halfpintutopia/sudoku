from grid import Grid
from pyfiglet import Figlet
from termcolor import colored
from sudoku import Sudoku
import time
from screen import on, clear, write, clear_screen
import keyboard

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
                choice = int(self.add_input_at_position(15, 1, 'Enter a number: '))
                # choice = int(input(f"\x1b[15;1HEnter a number: \x1b[16;1H"))
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

    def add_input_at_position(self, row, col, string):
        """
        A helper function to return an input at a set row and column
        """
        return input(f"\x1b[{row};{col}H{string}\x1b[16;1H")

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

    def show_instructions(self):
        """
        Show the instructions for the game, when option chosen
        """
        clear_screen()
        self.set_title()
        on(10, 1, 'A Sudoku puzzle is created with a 9 by 9 square (9 rows and 9 columns).')
        on(11, 1, 'The 9 by 9 square is also divided into 3 by 3 areas (a total of 9 x 3 by 3 areas).')
        on(12, 1, 'Each row, column and 3 by 3 area must contain numbers 1 - 9 (inclusive).')
        on(13, 1, 'Numbers cannot be repeated in the row, column nor 3 by 3 area.')

        self.add_return_input()
        self.add_initial_options()



    def add_return_input(self):
        """
        Show the prompt to press enter to continue
        """
        return input(f"\x1b[15;1HPress Enter to return to menu... \x1b[16;1H")
