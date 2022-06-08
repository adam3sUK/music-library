import unittest
from unittest.mock import Mock
from player.music_player import MusicPlayer

class TestMusicPlay(unittest.TestCase):

  def test_music_plays(self):
    path = '/data/tunes/myfav.wav'
    subprocess = Mock()
    player = MusicPlayer(subprocess)
    player.play(path)
    subprocess.call.assert_called_with(['afplay', path])
