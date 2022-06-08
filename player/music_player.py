class MusicPlayer:
  def __init__(self, subprocess):
    self._subprocess = subprocess

  def play(self, path):
    self._subprocess.call(["afplay", path])


# player = MusicPlayer(subprocess)
# player.play('data/tunes/myfav.wav')