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

    def testMaxTimeTriggered(self):
        c = lichess_game_downloader.LichessDownloader(maxTime=0.000001)
        self.assertTrue(c.maxTimeTriggered())

        c = lichess_game_downloader.LichessDownloader(maxTime=100)
        self.assertFalse(c.maxTimeTriggered())

    def testGetNumRequests(self):
        c = lichess_game_downloader.LichessDownloader()
        self.assertEquals(0, c.numRequests())

        c.num_requests=1
        self.assertEquals(1, c.numRequests())

    def testMaxRequestsTriggered(self):
        # An exercise in mocking!
        # http://stackoverflow.com/questions/23988853/how-to-mock-set-system-date-in-pytest
        with mock.patch('lichess_game_downloader.LichessDownloader.numRequests', return_value=2) as blerk:
            ""
            c = lichess_game_downloader.LichessDownloader(maxRequests=1)
            self.assertTrue(c.maxRequestsTriggered(), "Max requests is 2 and I've requested 1")

            c = lichess_game_downloader.LichessDownloader(maxRequests=2)
            self.assertTrue(c.maxRequestsTriggered(), "Max requests is 2 and I've requested 2")

            c = lichess_game_downloader.LichessDownloader(maxRequests=3)
            self.assertFalse(c.maxRequestsTriggered(), "Max requests is 2 and I've requested 3")

if __name__ == "__main__":
    unittest.main()

