#!/usr/bin/env python
import unittest
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

if __name__ == "__main__":
    unittest.main()

