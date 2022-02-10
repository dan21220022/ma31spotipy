import os

from core.base.artist import *
from core.helpers import constants
from core.helpers.config_reader import read_config


class User:
    def __init__(self, username, user_id=None):

        if self.login(username):
            self.user_id = open(read_config(constants.CONFIG_PATH, "DataPaths", "users_path") + username + ".json",
                                'r').read()
        else:
            with open(read_config(constants.CONFIG_PATH, "DataPaths", "users_path") + username + ".json",
                      'w+') as new_user_file:
                if user_id is None:
                    self.user_id = str(uuid1())
                else:
                    self.user_id = user_id
                new_user_file.write(self.user_id)

        self.user_name = username
        self.playlists = []

    def login(self, username):
        users_path = read_config(constants.CONFIG_PATH, "DataPaths", "users_path")
        if os.path.exists(users_path):
            return username in [path for path in os.listdir(users_path)]
        os.mkdir(users_path)
        return False

    def add_playlist(self, playlist: Album):
        playlist_names = [playlist.album_name for playlist in self.playlists]
        if playlist.album_name not in playlist_names:
            self.playlists.append(playlist)

    def add_playlist_track(self, track: Track, playlist_id):
        working_playlist = [playlist for playlist in self.playlists if playlist_id == playlist.album_id][0]
        if working_playlist is None:
            # TODO: throw an exception
            pass
        working_playlist.add_track(track)

    def load_data(self):
        # TODO: C part
        pass
