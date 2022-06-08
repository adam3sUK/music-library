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
        self.assertEqual(
            self.music_library.all(), [self.track_one, self.track_two, self.track_three]
        )

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

    def test_can_search_by_title(self):
        self.music_library.add(self.track_one)
        self.music_library.add(self.track_two)
        result = self.music_library.search(
            lambda track: "as" in track.title.lower()
        )
        self.assertEqual(list(result), [self.track_one])

    def test_can_get_multiple_search_results(self):
        self.music_library.add(self.track_one)
        self.music_library.add(self.track_two)
        love_track_two = Track("Love Story", "Taylor Swift", "love-story.mp3")
        love_track_one = Track("Love the way you lie", "Eminem", "love-you-lie.mp3")
        self.music_library.add(love_track_one)
        self.music_library.add(love_track_two)
        result = self.music_library.search(
            lambda track: "love" in track.title.lower()
        )
        self.assertEqual(list(result), [love_track_one, love_track_two])

    def test_can_search_by_artist(self):
        self.music_library.add(self.track_one)
        self.music_library.add(self.track_two)
        result = self.music_library.search(
            lambda track: "harry" in track.artist.lower()
        )
        self.assertEqual(list(result), [self.track_one])

    def test_can_search_by_file(self):
        self.music_library.add(self.track_one)
        self.music_library.add(self.track_two)
        result = self.music_library.search(
            lambda track: "as-it" in track.file.lower()
        )
        self.assertEqual(list(result), [self.track_one])

    def test_can_search_by_anything(self):
        self.music_library.add(self.track_one)
        self.music_library.add(self.track_two)
        result = self.music_library.search(
            lambda track: 
            ("as-it" in track.title.lower())
            or ("as-it" in track.artist.lower())
            or ("as-it" in track.file.lower())
        )
        self.assertEqual(list(result), [self.track_one])