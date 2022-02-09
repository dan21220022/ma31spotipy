from track import Track


class Album:
    def __init__(self, album_id, album_name):
        self.album_id = album_id
        self.album_name = album_name
        self.tracks = []

    def add_track(self, new_track: Track):
        self.tracks.append(new_track)
        self.tracks = sorted(self.tracks, key=lambda track: track.name)
