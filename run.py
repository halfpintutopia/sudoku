from Grid import *
from pprint import pprint
from pprint import pprint
from Grid import *
from Sudoku import *
from User import *
import time
import curses
from curses import wrapper
from Game import *
from termcolor import colored
from pyfiglet import Figlet

def esc(code):
    return f'\033[{code}m'


# def set_up(standard_output_screen):
#     pass


def main():
    # wrapper(set_up)
    # grid = Grid()
    # # for x in range(10):
    # #     print(x, end='\r')
    # # print()
    # print(grid, end='\r')
    # pprint(grid.create_completed_game())
    # grid.create_empy_board()
    # pprint(grid.create_styled_board())
    # board = Board()
    #
    # question_board_code = board.generate_question_board_code(1)  # generates a medium level sudoku
    #
    # pprint(board.board)

    # print(esc('34;1;4') + 'really' + esc(0) + ' important')

    # x = int(input('Enter value of x : '))
    # y = int(input('Enter value of y : '))
    # ch = input('Enter the Character : ')
    #
    # print('\n' * y + ' ' * x + ch)
    # print('\n\n\n\n')  # just for sparing some lines after the output
    game = Game()

    # print(esc('34;1;4') + game + esc(0))
    sudoku = Sudoku()
    # sudoku.choose_difficulty()
    sudoku.solve_puzzle()
    # pprint(sudoku.create_puzzle())
    # user = User()
    # user.create_username()


if __name__ == '__main__':
    main()
