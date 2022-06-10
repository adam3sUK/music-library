import unittest
from unittest.mock import MagicMock, Mock
from player.track_creator import TrackCreator, Track

class TestTrackCreator(unittest.TestCase):

  def test_creator_calls_eyed3_with_file(self):
    path = '/data/tunes/for-the-poor.mp3'
    eyed3 = Mock()
    track_creator = TrackCreator(path, eyed3)
    track_creator.create()
    eyed3.load.assert_called_with(path)

  def test_creator_create_returns_track_instance(self):
    path = '/data/tunes/for-the-poor.mp3'
    eyed3 = Mock()
    tag = MagicMock(artist='Don Braso', title='For the Poor')
    attrs = {'load.return_value': tag}
    eyed3.configure_mock(**attrs)
    track_creator = TrackCreator(path, eyed3)
    track = track_creator.create()
    self.assertIsInstance(track, Track)