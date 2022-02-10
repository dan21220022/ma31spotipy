import os

from core.base.artist import *
from core.helpers import constants
from core.helpers.config_reader import read_config


class User:
    def __init__(self, username, user_id=None, user_type=constants.UserTypes.NORMAL):
        if self.login(username):
            file_content = open(read_config(constants.CONFIG_PATH, "DataPaths", "users_path") + username + ".json",
                                'r').readlines()
            self.user_id = file_content[0]
            self.user_type = file_content[1]
        else:
            with open(read_config(constants.CONFIG_PATH, "DataPaths", "users_path") + username + ".json",
                      'w+') as new_user_file:

                self.user_id = str(uuid1()) if user_id is None else user_id
                self.user_type = user_type
                new_user_file.write(self.user_id)
                new_user_file.write('\n')
                new_user_file.write(self.user_type)
                new_user_file.flush()

        self.user_name = username
        self.playlists = []

    def login(self, username):
        users_path = read_config(constants.CONFIG_PATH, "DataPaths", "users_path")
        if os.path.exists(users_path):
            return username in [path for path in os.listdir(users_path)]
        os.mkdir(users_path)
        return False

    def add_playlist(self, playlist: Album):
        if self.user_type == constants.UserTypes.NORMAL and len(
                self.playlists) >= constants.Normal_User_Options.PLAYLISTS_COUNT:
            # TODO: throw exception user cannot add more playlists
            return
        playlist_names = [playlist.album_name for playlist in self.playlists]
        if playlist.album_name not in playlist_names:
            self.playlists.append(playlist)

    def add_playlist_track(self, track: Track, playlist_id):
        working_playlist = [playlist for playlist in self.playlists if playlist_id == playlist.album_id][0]
        if working_playlist is None:
            # TODO: throw an exception
            pass
        if self.user_type == constants.UserTypes.NORMAL and len(
                working_playlist.tracks) >= constants.Normal_User_Options.PLAYLIST_SONGS_COUNT:
            # TODO: throw exception user cannot add more playlists
            return
        working_playlist.add_track(track)

    def load_data(self):
        # TODO: C part
        pass
