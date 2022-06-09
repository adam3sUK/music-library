class ArtistTracks:
  def __init__(self):
    self._artist_tracks = {}

  def add(self, tracks):
    for track in tracks:
      if track.artist in self._artist_tracks:
        self._artist_tracks[track.artist] += 1
      else:
        self._artist_tracks[track.artist] = 1

  def most_tracks(self):
    all = self._sort_list()
    return all[:15]

  def _sort_list(self):
    return sorted(self._artist_tracks.items(), key=lambda value: value[1], reverse=True)