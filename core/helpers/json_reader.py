import json
import os
from typing import List

from core.base.album import Album
from core.base.artist import Artist
from core.base.track import Track
from core.helpers import constants, config_reader


def load_json(json_path):
    with open(json_path) as json_file:
        data = json.load(json_file)
        return data


def get_field_val(data: json, *args):
    json_data = data
    for arg in args:
        json_data = json_data[arg]
    return json_data


def get_artists(data) -> List[Artist]:
    artists = []
    artists_json = get_field_val(data, constants.SongsFileFields.TRACK, constants.SongsFileFields.ARTISTS)
    for artist in artists_json:
        artist_id = get_field_val(artist, constants.SongsFileFields.ID)
        artist_name = get_field_val(artist, constants.SongsFileFields.NAME)
        artists.append(Artist(artist_id, artist_name))
    return artists


def get_album(data) -> Album:
    album_json = get_field_val(data, constants.SongsFileFields.TRACK, constants.SongsFileFields.ALBUM)
    return Album(get_field_val(album_json, constants.SongsFileFields.ID),
                 get_field_val(album_json, constants.SongsFileFields.NAME))


def get_song(data) -> Track:
    track_json = get_field_val(data, constants.SongsFileFields.TRACK)
    return Track(get_field_val(track_json, constants.SongsFileFields.ID),
                 get_field_val(track_json, constants.SongsFileFields.NAME),
                 get_field_val(track_json, constants.SongsFileFields.POPULARITY))


def run_over_path(func):
    def path_runner():
        obj_list = []
        songs_dir = config_reader.read_config(constants.CONFIG_PATH, "DataPaths", "songs_path")
        for path in os.listdir(songs_dir):
            data = load_json(songs_dir + path)
            obj_list = func(data, obj_list)
        return obj_list
    return path_runner
