from dataclasses import dataclass


@dataclass
class Track:
    title: str
    artist: str
    file: str

    def __str__(self):
        return f"{self.title} by {self.artist}"


class MusicLibrary:
    def __init__(self):
        self._tracks = []

    def add(self, track):
        self._tracks.append(track)

    def remove(self, tracknum):
        if self.__track_exist(tracknum):
            self._tracks.pop(tracknum)
            return True
        return False

    def search(self, condition):
        return [track for track in self._tracks if condition(track)]

    def all(self):
        return self._tracks

    def __track_exist(self, tracknum):
        return tracknum < len(self._tracks)


