from uuid import uuid1

from core.base.album import Album
from core.base.track import Track


class Artist:
    def __init__(self, artist_id, artist_name):
        self.artist_id = artist_id
        self.artist_name = artist_name
        self.albums = []
        self.default_album_uuid = uuid1()
        self.default_album_name = "none"
        self.albums.append(Album(self.default_album_uuid, self.default_album_name))

    def add_album(self, new_album: Album):
        album_names = [album.album_name for album in self.albums]
        print("album names", album_names)
        if new_album.album_name not in album_names:
            self.albums.append(new_album)

    def add_track(self, track: Track, album_id):
        working_album = [album for album in self.albums if album_id == album.album_id][0]
        if working_album is None:
            working_album = [album for album in self.albums if album.album_id == self.default_album_uuid][0]
        working_album.add_track(track)
