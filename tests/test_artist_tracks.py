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

  def test_no_more_than_15_artists_shown(self):
    self.artist_tracks.add([self.track_one, self.track_two, self.track_three])
    self.artist_tracks.add([self.track_four])
    self.artist_tracks.add([
      Track("First class", "Jack Harlow", "life-times.mp3"),
      Track("IFTK", "Tion Wayne", "iftk.mp3"),
      Track("Running up that Hill", "Kate Bush", "ruth.mp3"),
      Track("Afraid to feel", "LF SYSTEM", "afraid.mp3"),
      Track("wait for u", "future", "wait.mp3"),
      Track("crazy what love can do", "david guetta", "crazy.mp3"),
      Track("green green grass", "george ezra", "grass.mp3"),
      Track("spaceman", "sam ryder", "spaceman.mp3"),
      Track("last last", "burna boy", "last.mp3"),
      Track("where did you go?", "Jax jones", "where.mp3"),
      Track("baby", "aitch", "baby.mp3"),
      Track("all i wanna be", "tate mcrae", "all.mp3"),
      Track("peru", "fireboy", "peru.mp3"),
      Track("starlight", "dave", "starlight.mp3"),
    ])
    self.assertEqual(len(self.artist_tracks.most_tracks()), 15)