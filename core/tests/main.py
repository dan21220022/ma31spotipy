from uuid import uuid1

from core.base.album import Album
from core.base.spotipy_search_engine import get_all_artists, get_artist_popular_songs, \
    get_song_from_album
from core.base.user import User
from core.helpers import json_reader


def print_all_artists(data):
    print(json_reader.get_field_val(data, "track", "popularity"))
    print(len(get_all_artists()))
    for artist in get_all_artists():
        print(artist.artist_id, artist.artist_name + ":")
        for album in artist.albums:
            print("\t" + album.album_name, str(album.album_id) + ":")
            for song in album.tracks:
                print("\t\t" + song.track_name)


def user_test(data):
    my_user = User("daniel")
    print(my_user)
    my_user.add_playlist(Album(uuid1(), "my_album"))
    my_user.add_playlist_track(json_reader.get_song(data), my_user.playlists[0].album_id)
    print(my_user.playlists[0].tracks[0].track_name)


def main():
    data = json_reader.load_json("./../../data/songs/song_086myS9r57YsLbJpU0TgK9.json")
    print_all_artists(data)
    user_test(data)

    songs = get_song_from_album("34GQP3dILpyCN018y2k61L")
    for song in songs:
        print(song.track_name, song.popularity)
    print("artist popular songs:", get_artist_popular_songs("7Ln80lUS6He07XvHI8qqHH"))


if __name__ == '__main__':
    main()
