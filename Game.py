from Grid import *
from pyfiglet import Figlet
from termcolor import colored


class Game:
    def __init__(self):
        self.grid = None
        self.initiate_game()

    def initiate_game(self):
        custom_fig = Figlet(font='block')
        print(colored(custom_fig.renderText('SUDOKU'), 'red'))

