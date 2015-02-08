import unittest
import pgn_module

class ParseJson(unittest.TestCase):
    json1 = """
        {
            "clock": {
                "increment": 1,
                "initial": 0,
                "totalTime": 30
            },
            "id": "game1",
            "moves": "g3 e6 Bg2 Nf6 Bxb7 Be7 Bxa8",
            "opening": {
                "code": "A00",
                "name": "Hungarian Opening, General"
            },
            "perf": "bullet",
            "players": {
                "black": {
                    "rating": 1447,
                    "ratingDiff": -10,
                    "userId": "black1"
                },
                "white": {
                    "rating": 1489,
                    "ratingDiff": 10,
                    "userId": "white1"
                }
            },
            "rated": true,
            "speed": "bullet",
            "status": "resign",
            "timestamp": 1423358208502,
            "turns": 7,
            "url": "http://lichess.org/viICO7M5/white",
            "variant": "standard",
            "winner": "white"
        }"""

    def testParseGoodJson(self):
        self.assertTrue(pgn_module.parse_lichess_json(self.json1))


    def testParseBadJson(self):
        self.assertEqual(None, pgn_module.parse_lichess_json("JUNK"))

    def testSite(self):
        ""
        pgn_module.parse_lichess_json(self.json1)
        self.assertEqual("http://lichess.org/viICO7M5/white", pgn_module.site())

    def testWhite(self):
        ""
        pgn_module.parse_lichess_json(self.json1)
        self.assertEqual("white1", pgn_module.white())

    def testBlack(self):
        ""
        pgn_module.parse_lichess_json(self.json1)
        self.assertEqual("black1", pgn_module.black())

    def testDate(self):
        ""
        pgn_module.parse_lichess_json(self.json1)
        self.assertEqual("2015.02.07", pgn_module.date())

if __name__ == "__main__":
    unittest.main()
