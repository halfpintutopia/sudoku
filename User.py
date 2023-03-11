import gspread
from google.oauth2.service_account import Credentials


class User:
    def __init__(self):
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
            print("Username should not contain spaces.")
            print("Username should not contain special characters, except underscore ('_') and hyphen ('-')\n")

            username = input("Enter your username: \n")
            break

        print(f"Hello {username}")
