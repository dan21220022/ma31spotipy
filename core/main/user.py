from core.main.artist import *
from core.helpers.config_reader import read_config
import os

class User(Artist):
    def __init__(self, username):
        if self.login(username):
            print("hello", username)
        else:
            super().__init__(uuid1(), username)

    def login(self, username):
        users_path = read_config("config.ini", "DataPaths", "users_path")
        if os.path.exists(users_path):
            return username in [path for path in os.listdir(users_path)]
        os.mkdir(users_path)
        return False

    def load_data(self):
        pass
