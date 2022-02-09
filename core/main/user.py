from core.main.artist import *


class User(Artist):
    def __init__(self, username):
        if self.login(username):
            # TODO: load all user data
            pass
        else:
            super().__init__(uuid1(), username)

    def login(self, username):
        # TODO: check in the config file path of users file and if user exists
        return False

    def load_data(self):
        pass