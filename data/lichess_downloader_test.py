import unittest
import lichess_downloader

class LichessDownloaderTest(unittest.TestCase):
    def testInstantiate(self):
        ld = lichess_downloader.LichessDownloader()
        self.assertIsNotNone(ld)
        
    def testMaxTimeDefault(self):
        ld = lichess_downloader.LichessDownloader(maxTime=10)
        self.assertEquals(10, ld.maxTime)

        ld = lichess_downloader.LichessDownloader()
        self.assertEquals(0, ld.maxTime)

    def testStopTimeTriggered(self):
        c = lichess_downloader.LichessDownloader(maxTime=0.00001)
        sleep(0.001)
        self.assertTrue(c.stopTimeTriggered())

        c = lichess_downloader.LichessDownloader(maxTime=100)
        self.assertFalse(c.stopTimemeTriggered())
