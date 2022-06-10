from cgi import test
import unittest
from ui.interface import Interface
from ui.mocks import PrintLine, InputLine, TestingConsoleIO, MockSubprocess


class TestConsoleRunner(unittest.TestCase):
    OPTIONS = [
        PrintLine("Enter:"),
        PrintLine("  a: to add a track manually"),
        PrintLine("  A: to add a track automatically"),
        PrintLine("  p: to play a track"),
        PrintLine("  d: to delete a track"),
        PrintLine("  l: to list your tracks"),
        PrintLine("  s: to search your tracks"),
        PrintLine("  S: to summarise your top 15 artists"),
        PrintLine("  q: to quit"),
    ]

    INTRO = [PrintLine("Welcome to your music library!"), *OPTIONS]

    SEARCH = [
        InputLine("What do you pick? ", "s"),
        PrintLine("Search by:"),
        PrintLine("  t: title"),
        PrintLine("  a: artist"),
        PrintLine("  f: file"),
        PrintLine("  *: anything"),
    ]

    PLAY = [SEARCH].pop(0)

    QUIT = [*OPTIONS, InputLine("What do you pick? ", "q")]

    def test_adds_tracks(self):
        testing_console_io = TestingConsoleIO(
            *self.INTRO,
            InputLine("What do you pick? ", "a"),
            InputLine("What's the title? ", "Major's Titling Victory"),
            InputLine("What's the artist? ", "The Cribs"),
            InputLine("What's the file? ", "file1.mp3"),
            PrintLine("Added successfully."),
            *self.OPTIONS,
            InputLine("What do you pick? ", "l"),
            PrintLine("1. Major's Titling Victory by The Cribs @ file1.mp3"),
            *self.QUIT,
        )
        interface = Interface(testing_console_io, MockSubprocess())
        interface.run()
        self.assertTrue(testing_console_io.is_done())

    def test_adds_tracks_from_file(self):
        testing_console_io = TestingConsoleIO(
            *self.INTRO,
            InputLine("What do you pick? ", "A"),
            InputLine("What's the file? ", "data/tunes/for-the-poor.mp3"),
            PrintLine("For the Poor by Dan Brasco added!")
            *self.OPTIONS,
            InputLine("What do you pick? ", "l"),
            PrintLine("1. For the Poor by Dan Brasco @ data/tunes/for-the-poor.mp3"),
            *self.QUIT,
        )
        Interface = Interface(testing_console_io, MockSubprocess())
        Interface.run()
        self.assertTrue(testing_console_io.is_done())

    def test_plays_tracks(self):
        testing_console_io = TestingConsoleIO(
            *self.INTRO,
            InputLine("What do you pick? ", "a"),
            InputLine("What's the title? ", "Major's Titling Victory"),
            InputLine("What's the artist? ", "The Cribs"),
            InputLine("What's the file? ", "data/tunes/myfav.wav"),
            PrintLine("Added successfully."),
            *self.OPTIONS,
            InputLine("What do you pick? ", "a"),
            InputLine("What's the title? ", "Hello"),
            InputLine("What's the artist? ", "Adele"),
            InputLine("What's the file? ", "yokal.wav"),
            PrintLine("Added successfully."),
            *self.OPTIONS,
            InputLine("What do you pick? ", "a"),
            InputLine("What's the title? ", "The Milky Way over Ratlinghope"),
            InputLine("What's the artist? ", "Bibio"),
            InputLine("What's the file? ", "data/tunes/myfav2.wav"),
            PrintLine("Added successfully."),
            *self.OPTIONS,
            InputLine("What do you pick? ", "p"),
            PrintLine("Search by:"),
            PrintLine("  t: title"),
            PrintLine("  a: artist"),
            PrintLine("  f: file"),
            PrintLine("  *: anything"),
            InputLine("What do you want to search by? ", "f"),
            InputLine("What do you want to search for? ", "data"),
            PrintLine("1. Major's Titling Victory by The Cribs @ data/tunes/myfav.wav"),
            PrintLine("2. The Milky Way over Ratlinghope by Bibio @ data/tunes/myfav2.wav"),
            InputLine("Which do you want to play? ", "2"),
            PrintLine("Playing The Milky Way over Ratlinghope by Bibio..."),
            PrintLine("Done."),
            *self.QUIT,
        )
        mock_subprocess = MockSubprocess()
        interface = Interface(testing_console_io, mock_subprocess)
        interface.run()
        self.assertEqual(
            mock_subprocess.args,
            ["afplay", "data/tunes/myfav2.wav"],
            "Subprocess wasn't called properly to play the file.",
        )
        self.assertTrue(testing_console_io.is_done())

    def test_artist_summary(self):
        testing_console_io = TestingConsoleIO(
            *self.INTRO,
            InputLine("What do you pick? ", "a"),
            InputLine("What's the title? ", "Major's Titling Victory"),
            InputLine("What's the artist? ", "The Cribs"),
            InputLine("What's the file? ", "file1.mp3"),
            PrintLine("Added successfully."),
            *self.OPTIONS,
            InputLine("What do you pick? ", "a"),
            InputLine("What's the title? ", "The Milky Way over Ratlinghope"),
            InputLine("What's the artist? ", "Bibio"),
            InputLine("What's the file? ", "file2.mp3"),
            PrintLine("Added successfully."),
            *self.OPTIONS,
            InputLine("What do you pick? ", "a"),
            InputLine("What's the title? ", "Men's Needs"),
            InputLine("What's the artist? ", "The Cribs"),
            InputLine("What's the file? ", "file3.mp3"),
            PrintLine("Added successfully."),
            *self.OPTIONS,
            InputLine("What do you pick? ", "S"),
            PrintLine("1. The Cribs: 2 tracks"),
            PrintLine("2. Bibio: 1 tracks"),
            *self.QUIT,
        )
        interface = Interface(testing_console_io, MockSubprocess())
        interface.run()
        self.assertTrue(testing_console_io.is_done())

    def test_searches_tracks(self):
        testing_console_io = TestingConsoleIO(
            *self.INTRO,
            InputLine("What do you pick? ", "a"),
            InputLine("What's the title? ", "Major's Titling Victory"),
            InputLine("What's the artist? ", "The Cribs"),
            InputLine("What's the file? ", "file1.mp3"),
            PrintLine("Added successfully."),
            *self.OPTIONS,
            InputLine("What do you pick? ", "a"),
            InputLine("What's the title? ", "The Milky Way over Ratlinghope"),
            InputLine("What's the artist? ", "Bibio"),
            InputLine("What's the file? ", "file2.mp3"),
            PrintLine("Added successfully."),
            *self.OPTIONS,
            *self.SEARCH,
            InputLine("What do you want to search by? ", "t"),
            InputLine("What do you want to search for? ", "vic"),
            PrintLine("1. Major's Titling Victory by The Cribs @ file1.mp3"),
            *self.OPTIONS,
            *self.SEARCH,
            InputLine("What do you want to search by? ", "a"),
            InputLine("What do you want to search for? ", "ibi"),
            PrintLine("1. The Milky Way over Ratlinghope by Bibio @ file2.mp3"),
            *self.OPTIONS,
            *self.SEARCH,
            InputLine("What do you want to search by? ", "f"),
            InputLine("What do you want to search for? ", "fi"),
            PrintLine("1. Major's Titling Victory by The Cribs @ file1.mp3"),
            PrintLine("2. The Milky Way over Ratlinghope by Bibio @ file2.mp3"),
            *self.OPTIONS,
            *self.SEARCH,
            InputLine("What do you want to search by? ", "*"),
            InputLine("What do you want to search for? ", "r"),
            PrintLine("1. Major's Titling Victory by The Cribs @ file1.mp3"),
            PrintLine("2. The Milky Way over Ratlinghope by Bibio @ file2.mp3"),
            *self.OPTIONS,
            *self.SEARCH,
            InputLine("What do you want to search by? ", "*"),
            InputLine("What do you want to search for? ", "xx"),
            *self.QUIT,
        )
        interface = Interface(testing_console_io, MockSubprocess())
        interface.run()
        self.assertTrue(testing_console_io.is_done())

    def test_deletes_tracks(self):
        testing_console_io = TestingConsoleIO(
            *self.INTRO,
            InputLine("What do you pick? ", "a"),
            InputLine("What's the title? ", "Major's Titling Victory"),
            InputLine("What's the artist? ", "The Cribs"),
            InputLine("What's the file? ", "file1.mp3"),
            PrintLine("Added successfully."),
            *self.OPTIONS,
            InputLine("What do you pick? ", "a"),
            InputLine("What's the title? ", "Be Safe (feat. Lee Ranaldo)"),
            InputLine("What's the artist? ", "The Cribs"),
            InputLine("What's the file? ", "file2.mp3"),
            PrintLine("Added successfully."),
            *self.OPTIONS,
            InputLine("What do you pick? ", "d"),
            PrintLine("1. Major's Titling Victory by The Cribs @ file1.mp3"),
            PrintLine("2. Be Safe (feat. Lee Ranaldo) by The Cribs @ file2.mp3"),
            InputLine("Which do you want to delete? ", "1"),
            PrintLine("Deleted successfully."),
            *self.OPTIONS,
            InputLine("What do you pick? ", "d"),
            PrintLine("1. Be Safe (feat. Lee Ranaldo) by The Cribs @ file2.mp3"),
            InputLine("Which do you want to delete? ", "2"),
            PrintLine("No such track."),
            *self.OPTIONS,
            InputLine("What do you pick? ", "l"),
            PrintLine("1. Be Safe (feat. Lee Ranaldo) by The Cribs @ file2.mp3"),
            *self.QUIT,
        )
        interface = Interface(testing_console_io, MockSubprocess())
        interface.run()
        self.assertTrue(testing_console_io.is_done())

    def test_cycles_on_wrong_choice(self):
        testing_console_io = TestingConsoleIO(
            *self.INTRO,
            InputLine("What do you pick? ", "z"),
            PrintLine("No such command! Try again."),
            *self.QUIT,
        )
        interface = Interface(testing_console_io, MockSubprocess())
        interface.run()
        self.assertTrue(testing_console_io.is_done())
