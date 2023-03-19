import gspread
from google.oauth2.service_account import Credentials
from helper_enums import GoogleSheets, InputPrompt
from screen import on, clear_screen_from_pos, write_input
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
        self.left_margin = 5

    def get_username(self):
        """
        Returns the user's username
        """
        return self.username

    def create_username(self):
        """
        Get username from user input
        Save username and game ID to google sheets
        """
        clear_screen_from_pos(10, 1)
        on(10, self.left_margin, 'Add your username.')
        on(11, self.left_margin, 'Username should be lowercase.')
        on(12, self.left_margin, 'Username must only contain letters a-z')
        on(13, self.left_margin, 'and can contain a hyphen or underscore')
        while True:
            username = write_input(15, self.left_margin,
                                   InputPrompt.USERNAME.value)

            if validate_username(username):
                self.username = username
                break

        return self.username

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
