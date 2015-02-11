import unittest
import lichess_downloader

class LichessDownloaderTest(unittest.TestCase):
    def testInstantiate(self):
        ld = lichess_downloader.LichessDownloader()
        self.assertIsNotNone(ld)
