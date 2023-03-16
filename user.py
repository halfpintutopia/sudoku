import gspread
from google.oauth2.service_account import Credentials
import re
from helper_enums import GoogleSheets, InputPrompt, Username
from screen import on, clear_screen_from_pos, write_input, clear


class User:
    def __init__(self):
        self.username = None
        self.pattern = "^[a-z0-9_-]*$"

        self.CREDS = Credentials.from_service_account_file(
            GoogleSheets.CREDS_FILE.value)
        self.SCOPED_CREDS = self.CREDS.with_scopes(GoogleSheets.SCOPE.value)
        self.GSPREAD_CLIENT = gspread.authorize(self.SCOPED_CREDS)
        self.SHEET = self.GSPREAD_CLIENT.open(GoogleSheets.SHEET.value)

        self.saved_games = self.SHEET.worksheet(
            GoogleSheets.GAMES_WORKSHEET.value)

        self.data = self.saved_games.get_all_values()

    def create_username(self):
        """
        Get username from user input
        Save username and game ID to google sheets
        """
        clear_screen_from_pos(10, 1)
        on(10, 1, Username.PROMPT_1.value)
        on(11, 1, Username.PROMPT_2.value)
        on(12, 1, Username.PROMPT_3.value)
        while True:
            username = write_input(14, 1, InputPrompt.USERNAME.value)

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
            clear(15, 1)
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


# def create_username():
#     """
#     Get username from user input
#     Save username and game ID to google sheets
#     """
#     clear_screen_from_pos(10, 1)
#     on(10, 1, Username.PROMPT_1.value)
#     on(11, 1, Username.PROMPT_2.value)
#     on(12, 1, Username.PROMPT_3.value)
#     while True:
#         username = write_input(14, 1, InputPrompt.USERNAME.value)
#
#         if validate_username(username):
#             username = username
#             # self.get_last_entry()
#             game_id = self.get_last_id_entry()
#             print(f"game id = {game_id}")
#             break
#
#     print(f"Hello {username}")
#
#
# def validate_username(username):
#     """
#     Check string inputted by user to meet the conditions:
#     - lowercase
#     - no special characters except underscore and or hyphen
#     - contains no spaces
#     """
#     try:
#         if not bool(re.match(self.pattern, username)):
#             raise ValueError(
#                 f"Name entered contains capital letters or special characters"
#             )
#     except ValueError as e:
#         print(f"Invalid username: {e}, please try again.\n")
#         return False
#
#     return True
