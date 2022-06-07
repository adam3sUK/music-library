import unittest

from player.music_library import MusicLibrary, Track


class TestMusicLibrary(unittest.TestCase):
    def setUp(self):
        self.music_library = MusicLibrary()
        self.track_one = Track("As It Was", "Harry Styles", "as-it-way.mp3")
        self.track_two = Track("Go", "Cat Burns", "go.mp3")
        self.track_three = Track("About damn time", "Lizzo", "about-damn-time.mp3")

    def test_track_gets_added(self):
        self.music_library.add(self.track_one)
        self.assertEqual(self.music_library.all(), [self.track_one])

    def test_multiple_tracks_get_added(self):
        self.music_library.add(self.track_one)
        self.music_library.add(self.track_two)
        self.music_library.add(self.track_three)
        self.assertEqual(self.music_library.all(), [self.track_one, self.track_two, self.track_three])

    def test_returns_true_on_track_removal(self):
        self.music_library.add(self.track_one)
        self.music_library.add(self.track_two)
        file_found = self.music_library.remove(1)
        self.assertTrue(file_found)

    def test_returns_false_if_track_number_does_not_exist(self):
        self.music_library.add(self.track_one)
        file_found = self.music_library.remove(1)
        self.assertFalse(file_found)

    def test_remove_track_from_list(self):
        self.music_library.add(self.track_one)
        self.music_library.add(self.track_two)
        self.music_library.add(self.track_three)
        self.music_library.remove(1)
        self.assertEqual(self.music_library.all(), [self.track_one, self.track_three])
