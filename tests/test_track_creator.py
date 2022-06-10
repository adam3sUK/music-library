import unittest
from unittest.mock import Mock
from player.music_library import Track
from player.track_creator import TrackCreator

class TestTrackCreator(unittest.TestCase):

  def test_creator_calls_eyed3_with_file(self):
    path = '/data/tunes/for-the-poor.mp3'
    eyed3 = Mock()
    track_creator = TrackCreator(path, eyed3)
    track_creator.create()
    eyed3.load.assert_called_with(path)

  def test_creator_create_returns_track(self):
    path = '/data/tunes/for-the-poor.mp3'
    eyed3 = Mock()
    attrs = {'load.return_value': {'tag': {'artist': 'Bon Braso', 'title': 'For the Poor'}}}
    eyed3.configure_mock(**attrs)
    track_creator = TrackCreator(path, eyed3)
    track = track_creator.create()
    self.assertIsInstance(track, Track)