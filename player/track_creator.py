from music_library import Track
import eyed3

class TrackCreator:
    def __init__(self, file, metafinder):
        self._file = file
        self._metafinder = metafinder

    def create(self):
        track = self._metafinder.load(self._file)
        print(track.tag)
        return Track(title=track.tag.title, artist=track.tag.artist, file=self._file)



poor_track = TrackCreator('data/tunes/for-the-poor.mp3', eyed3)
poor_track.create()