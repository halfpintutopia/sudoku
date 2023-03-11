import gspread
from google.oauth2.service_account import Credentials
import re


class User:
    def __init__(self):
        self.username = None
        self.pattern = "^[a-z0-9_-]*$"
        self.SCOPE = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]

        self.CREDS = Credentials.from_service_account_file('creds.json')
        self.SCOPED_CREDS = self.CREDS.with_scopes(self.SCOPE)
        self.GSPREAD_CLIENT = gspread.authorize(self.SCOPED_CREDS)
        self.SHEET = self.GSPREAD_CLIENT.open('sudoku_games')

        self.saved_games = self.SHEET.worksheet('saved_games')

        self.data = self.saved_games.get_all_values()

    def create_username(self):
        """
        Get username from user input
        Save username and game ID to google sheets
        """
        while True:
            print("Add your username.")
            print("Username can contain numbers, and be in lowercase.")
            print("Username should not contain spaces")
            print("Username should not contain special characters, except underscore ('_') and hyphen ('-')\n")

            username = input("Enter your username: \n")

            if self.validate_username(username):
                self.username = username
                # self.get_last_entry()
                game_id = self.get_last_id_entry()
                print(f"game id = {game_id}")
                break

        print(f"Hello {self.username}")

    def validate_username(self, username):
        """
        Check string inputted by user to meet the conditions:
        - lowercase
        - no special characters except underscore and or hyphen
        - contains no spaces
        """
        try:
            if not bool(re.match(self.pattern, username)):
                raise ValueError(
                    f"Name entered contains capital letters or special characters"
                )
        except ValueError as e:
            print(f"Invalid username: {e}, please try again.\n")
            return False

        return True

    def get_last_entry(self):
        """
        Get the last entry of the game sheet
        """
        num_of_rows = len(self.saved_games.get_all_values())
        if num_of_rows > 1:
            print(self.saved_games.row_values(num_of_rows))
            return

    def get_last_id_entry(self):
        """
        Get the last entry's id
        """
        game_id = 1
        if len(self.saved_games.get_all_values()) > 1:
            num_of_entries = 1
            id_column = self.saved_games.col_values(2)
            game_id_col = id_column[-num_of_entries:]
            game_id = int(game_id_col[0]) + 1
        return game_id
