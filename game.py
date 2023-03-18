from pyfiglet import Figlet
from termcolor import colored
from sudoku import Sudoku
from screen import on, clear, write, clear_screen, write_input, \
    clear_screen_from_pos, clear_right_side
from helper_enums import Instructions, MainMenu, InputPrompt, \
    DifficultyPrompt, Guess
from user import User
from validation import validate_number_guess, validate_coordinates, \
    validate_difficulty_input, validate_grid_cell
from style_puzzle import StylePuzzle


class Game(Sudoku):
    def __init__(self):
        super().__init__()
        self.user = User()
        self.guess = None
        self.row = None
        self.col = None
        self.grid = None
        self.initiate_game()
        self.lower_unicode_to_one_base = 96
        self.upper_unicode_to_one_base = 64
        self.reset_to_match_index = 1

    def initiate_game(self):
        """
        Start game screen
        """
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
        on(10, 1, MainMenu.PLAY.value)
        on(11, 1, MainMenu.ENTER_OWN.value)
        on(12, 1, MainMenu.SOLVE.value)
        on(13, 1, MainMenu.INSTRUCTIONS.value)

        while True:
            try:
                clear(16, 1)
                option = int(write_input(15, 1, InputPrompt.NUMBER.value))
            except ValueError as e:
                print(InputPrompt.INVALID_MAIN_MENU.value)
                continue
            else:
                self.selected_user_choice(option)
                break

    def selected_user_choice(self, option):
        """
        Take the chosen option and run the function accordingly
        """
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
        """
        Runs when the play option has been chosen
        """
        print(MainMenu.LOADING.value)
        self.user.create_username()

        clear_screen_from_pos(10, 1)
        on(10, 1, 'Hello ' + self.user.get_username())
        self.choose_difficulty()
        self.guess_cell()

    def guess_cell(self):
        """
        Prompt for player to add their guess
        """
        clear_right_side()
        on(10, 55, 'Please enter one row number')
        on(11, 55, 'and one column letter.')
        on(12, 55, 'e.g. 4E or e4')
        on(14, 55, MainMenu.EXIT.value)

        while True:
            clear(17, 55)
            option = write_input(16, 55, 'Enter number and letter:')
            if option == 'x' or option == 'X':
                self.add_initial_options()
            elif validate_coordinates(option):
                self.set_coordinates(option)
                self.guess_number()
                break

    def guess_number(self):
        """
        Prompt for player to choose a number to place in cell
        """
        clear_right_side()
        on(10, 55, 'Please enter a number (1-9)')

        on(12, 55, MainMenu.EXIT.value)

        while True:
            clear(15, 55)
            option = write_input(14, 55, InputPrompt.NUMBER.value)
            if option == 'x' or option == 'X':
                self.add_initial_options()
            elif validate_number_guess(option):
                self.set_guess(option)
                self.set_number_to_coordinates()
                break

    def set_number_to_coordinates(self):
        if validate_grid_cell(self.original_puzzle, self.row, self.col):
            self.current_puzzle[self.row][self.col] = self.guess
            style_puzzle = StylePuzzle(
                self.original_puzzle,
                self.current_puzzle
            )
            style_puzzle.add_puzzle_style()
            self.guess_cell()
        else:
            self.guess_cell()

    def set_guess(self, option):
        self.guess = int(option)

    def set_coordinates(self, cell):
        """
        Set the coordinates to wait for the number input to be put in the cell
        Minus one needs to be taken from the values of inputs
        due to index starting at 0
        """
        letter = ''
        if cell[0].isdigit() and cell[1].isalpha():
            if 0 <= (int(cell[0]) - 1) <= 8:
                self.row = (int(cell[0]) - 1)
            letter = cell[1]
        elif cell[0].isalpha() and cell[1].isdigit():
            letter = cell[0]
            if 0 <= (int(cell[1]) - 1) <= 8:
                self.row = (int(cell[1]) - 1)

        if letter.isupper():
            self.col = ord(letter) - 64 - 1
        else:
            self.col = ord(letter) - 96 - 1

    def choose_difficulty(self):
        """
        Input should allow the user to choose the difficulty of the game
        """
        on(12, 1, DifficultyPrompt.CHOOSE.value)
        on(13, 1, DifficultyPrompt.EASY.value)
        on(14, 1, DifficultyPrompt.MEDIUM.value)
        on(15, 1, DifficultyPrompt.HARD.value)

        while True:
            clear(16, 1)
            clear(17, 1)

            difficulty_level = write_input(16, 1, InputPrompt.NUMBER.value)

            if validate_difficulty_input(difficulty_level):
                clear_screen_from_pos(10, 1)
                self.set_difficulty(int(difficulty_level))
                break

    def show_instructions(self):
        """
        Show the instructions for the game, when option chosen
        """
        clear_screen_from_pos(10, 1)
        self.set_title()
        on(10, 1, Instructions.FIRST_LINE.value)
        on(11, 1, Instructions.SECOND_LINE.value)
        on(12, 1, Instructions.THIRD_LINE.value)
        on(13, 1, Instructions.FOURTH_LINE.value)

        write_input(15, 1, InputPrompt.PRESS_ENTER.value)
        self.add_initial_options()
