import unittest

from player.music_library import MusicLibrary


class TestMusicLibrary(unittest.TestCase):
    def setUp(self):
        self.music_library = MusicLibrary()

    def test_track_gets_added(self):
        self.music_library.add("Rolling Blackouts by The Go! Team")
        self.assertEqual(self.music_library.all(), ["Rolling Blackouts by The Go! Team"])

    def test_multiple_tracks_get_added(self):
        self.music_library.add("Rolling Blackouts by The Go! Team")
        self.music_library.add("Oh Yeah by Locust")
        self.music_library.add("Sleep on the Wing by Bibio")
        self.assertEqual(self.music_library.all(), ["Rolling Blackouts by The Go! Team", "Oh Yeah by Locust", "Sleep on the Wing by Bibio"])

    def test_returns_true_on_track_removal(self):
        self.music_library.add("Rolling Blackouts by The Go! Team")
        self.music_library.add("Oh Yeah by Locust")
        file_found = self.music_library.remove(1)
        self.assertTrue(file_found)

    def test_returns_false_if_track_number_does_not_exist(self):
        self.music_library.add("Rolling Blackouts by The Go! Team")
        file_found = self.music_library.remove(1)
        self.assertFalse(file_found)

    def test_remove_track_from_list(self):
        self.music_library.add("Rolling Blackouts by The Go! Team")
        self.music_library.add("Oh Yeah by Locust")
        self.music_library.add("Sleep on the Wing by Bibio")
        self.music_library.remove(1)
        self.assertEqual(self.music_library.all(), ["Rolling Blackouts by The Go! Team", "Sleep on the Wing by Bibio"])
