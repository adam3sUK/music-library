from player.music_library import Track

class TrackCreator:
    def __init__(self, file, metafinder):
        self._file = file
        self._metafinder = metafinder

    def create(self):
        track = self._metafinder.load(self._file)
        if len(track.tag.title) > 0:
            return Track(title=track.tag.title, artist=track.tag.artist, file=self._file)
        return False