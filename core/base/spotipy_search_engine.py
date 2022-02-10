import os
from typing import List

from core.base.album import Album
from core.base.artist import Artist
from core.base.track import Track
from core.helpers import json_reader, config_reader, constants
from core.helpers.json_reader import run_over_path


@run_over_path
def get_all_artists(data, artists=[]) -> List[Artist]:
    extracted_artists = json_reader.get_artists(data)
    for new_artist in extracted_artists:
        new_album = json_reader.get_album(data)
        if new_artist.artist_id not in [artist.artist_id for artist in artists]:
            new_artist.add_album(new_album)
            new_artist.add_track(json_reader.get_song(data), new_album.album_id)
            artists.append(new_artist)
        else:
            artist = [artist for artist in artists if artist.artist_id == new_artist.artist_id][0]
            artist.add_album(new_album)
            artist.add_track(json_reader.get_song(data), new_album.album_id)
    return artists


def get_artist_popular_songs(artist_id: str) -> List[Track]:
    pass


def get_song_from_album(album_id: str) -> List[Track]:
    pass
