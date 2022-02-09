from core.main.track import Track


class Album:
    def __init__(self, album_id, album_name):
        self.album_id = album_id
        self.album_name = album_name
        self.tracks = []

    def add_track(self, new_track: Track):
        if new_track.track_id not in [track.track_id for track in self.tracks]:
            self.tracks.append(new_track)
