class ArtistTracks:
  def __init__(self):
    self._artist_tracks = {}

  def add(self, tracks):
    for track in tracks:
      if track.artist in self._artist_tracks:
        self._artist_tracks[track.artist] += 1
      else:
        self._artist_tracks[track.artist] = 1

  def all(self):
    return self._artist_tracks