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
        if self.__track_not_exist(tracknum):
            return False
        else:
            self._tracks.pop(tracknum)
            return True

    def all(self):
        return self._tracks

    def __track_not_exist(self, tracknum):
        return tracknum >= len(self._tracks)


