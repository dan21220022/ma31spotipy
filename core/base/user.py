import os

from core.helpers import constants
from core.helpers.config_reader import read_config
from core.base.artist import *


class User(Artist):
    def __init__(self, username):
        if self.login(username):
            print("hello", username)
        else:
            super().__init__(uuid1(), username)
            with open(read_config(constants.CONFIG_PATH, "DataPaths", "users_path") + username + ".json", 'w+'):
                pass

    def login(self, username):
        users_path = read_config(constants.CONFIG_PATH, "DataPaths", "users_path")
        if os.path.exists(users_path):
            return username in [path for path in os.listdir(users_path)]
        os.mkdir(users_path)
        return False

    def load_data(self):
        # TODO: C part
        pass
