import gspread
from google.oauth2.service_account import Credentials
import re
from helper_enums import GoogleSheets, InputPrompt, Username
from screen import on, clear_screen_from_pos, write_input, clear
from validation import validate_username


class User:
    def __init__(self, username=None):
        self.username = username
        self.pattern = "^[a-z0-9_-]*$"

        self.CREDS = Credentials.from_service_account_file(
            GoogleSheets.CREDS_FILE.value)
        self.SCOPED_CREDS = self.CREDS.with_scopes(GoogleSheets.SCOPE.value)
        self.GSPREAD_CLIENT = gspread.authorize(self.SCOPED_CREDS)
        self.SHEET = self.GSPREAD_CLIENT.open(GoogleSheets.SHEET.value)

        self.users = self.SHEET.worksheet(GoogleSheets.USER_WORKSHEET.value)
        self.saved_games = self.SHEET.worksheet(
            GoogleSheets.GAMES_WORKSHEET.value)

        self.users_data = self.users.get_all_values()
        self.saved_games_data = self.saved_games.get_all_values()
        self.user_id = None

    def get_username(self):
        return self.username

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

            if validate_username(username):
                self.username = username
                # self.save_username()
                # self.get_last_entry()
                # game_id = self.get_last_id_entry()
                # print(f"game id = {game_id}")
                break

        return self.username

    # def save_username(self):
    #     cell_list = self.saved_games.findall('siri')
    #     for cell in cell_list:
    #
    #     print(cell_list)

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
