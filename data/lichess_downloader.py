import time
class LichessDownloader():
    def __init__(self, maxTime=0):
        ""
        self.maxTime = maxTime
        self.startTime = time.time()
        self.stopTime = self.startTime + self.maxTime

    def stopTimeTriggered(self):
        return time.time() > self.stopTime
