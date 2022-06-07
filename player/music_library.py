class MusicLibrary:
    def __init__(self):
        self._tracks = []

    def add(self, track):
        self._tracks.append(track)

    def remove(self, tracknum):
        if tracknum > len(self._tracks) - 1:
            return False
        else:
            self._tracks.pop(tracknum)
            return True

    def all(self):
        return self._tracks
