#!/usr/bin/env python
import unittest
import mock
import datetime
import time
import lichess_game_downloader

class TestSomething(unittest.TestCase):
    def testSomething(self):
        c = lichess_game_downloader.LichessDownloader()
        self.assertIsNotNone(c)

    def testAddGame(self):
        c = lichess_game_downloader.LichessDownloader()

        c.addGame("1")
        self.assertEquals(1, c.gameCount())

        # Duplicate games don't add to total
        c.addGame("1")
        self.assertEquals(1, c.gameCount())

        c.addGame("2")
        self.assertEquals(2, c.gameCount())

    def testTimeElapsed(self):
        # An exercise in mocking!
        # http://stackoverflow.com/questions/23988853/how-to-mock-set-system-date-in-pytest
        elapsed_seconds = 10
        with mock.patch('lichess_game_downloader.LichessDownloader.getNow', return_value=time.time() - elapsed_seconds):
            ""
            c = lichess_game_downloader.LichessDownloader(maxTime=10)
            self.assertTrue(c.time_elapsed())


if __name__ == "__main__":
    unittest.main()

