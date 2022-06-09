import unittest
from player.artist_tracks import ArtistTracks
from player.music_library import Track

class TestArtistTracks(unittest.TestCase):
  def setUp(self):
    self.artist_tracks = ArtistTracks()
    self.track_one = Track("As It Was", "Harry Styles", "as-it-way.mp3")
    self.track_two = Track("Go", "Cat Burns", "go.mp3")
    self.track_three = Track("Sign of the Times", "Harry Styles", "sign-of-the-times.mp3")
    self.track_four = Track("About damn time", "Lizzo", "about-damn-time.mp3")

  def test_track_gets_added(self):
    self.artist_tracks.add([self.track_one])
    self.assertEqual(self.artist_tracks.most_tracks(), [(self.track_one.artist, 1)])

  def test_chosen_track_gets_added(self):
    self.artist_tracks.add([self.track_two])
    self.assertEqual(self.artist_tracks.most_tracks(), [(self.track_two.artist, 1)])

  def test_multiple_tracks_get_added(self):
    self.artist_tracks.add([self.track_one])
    self.artist_tracks.add([self.track_two])
    self.assertEqual(self.artist_tracks.most_tracks(), [(self.track_one.artist, 1), (self.track_two.artist, 1)])

  def test_tracks_by_same_artist_get_grouped(self):
    self.artist_tracks.add([self.track_one])
    self.artist_tracks.add([self.track_two])
    self.artist_tracks.add([self.track_three])
    self.assertEqual(self.artist_tracks.most_tracks(), [(self.track_one.artist, 2), (self.track_two.artist, 1)])

  def test_multiple_tracks_can_be_added_together(self):
    self.artist_tracks.add([self.track_one, self.track_two, self.track_three])
    self.assertEqual(self.artist_tracks.most_tracks(), [(self.track_one.artist, 2), (self.track_two.artist, 1)])