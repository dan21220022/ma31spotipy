from operator import attrgetter
from typing import List

from core.base.artist import Artist
from core.base.track import Track
from core.helpers import json_reader, constants
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


@run_over_path
def get_artist_albums(data, albums: list, artist_id: str):
    if albums is None:
        albums = []

    artist_id = artist_id[0]
    if artist_id not in str(data):
        return albums

    new_album = json_reader.get_album(data).album_name
    if new_album not in albums:
        albums.append(new_album)
    return albums


@run_over_path
def get_artist_popular_songs(data, songs: list, artist_id: str) -> List[Track]:
    if songs is None:
        songs = []

    artist_id = artist_id[0]
    if artist_id not in str(data):
        return songs

    new_song = json_reader.get_song(data)
    if new_song.track_id not in songs:
        songs.append(new_song)
    return sorted(songs, key=attrgetter(constants.SongsFileFields.POPULARITY), reverse=True)[:10]


@run_over_path
def get_song_from_album(data, songs: list, album_id: str) -> List[Track]:
    if songs is None:
        songs = []

    artist_id = album_id[0]
    if artist_id not in str(data):
        return songs

    new_song = json_reader.get_song(data)
    if new_song.track_id not in songs:
        songs.append(new_song)
    return songs
