import unittest
import pgn_module
import re

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

    json2 = """
        {
                    "clock": {
                        "increment": 2,
                        "initial": 180,
                        "totalTime": 240
                    },
                    "id": "IGwZ8ld7",
                    "perf": "blitz",
                    "players": {
                        "black": {
                            "analysis": {
                                "blunder": 0,
                                "inaccuracy": 3,
                                "mistake": 2
                            },
                            "rating": 2452,
                            "ratingDiff": -9,
                            "userId": "zuckertort"
                        },
                        "white": {
                            "analysis": {
                                "blunder": 1,
                                "inaccuracy": 0,
                                "mistake": 3
                            },
                            "rating": 2160,
                            "ratingDiff": 7,
                            "userId": "luis_alfredop"
                        }
                    },
                    "rated": true,
                    "speed": "blitz",
                    "status": "draw",
                    "timestamp": 1422121854198,
                    "turns": 63,
                    "url": "http://lichess.org/IGwZ8ld7/black",
                    "variant": "standard"
                }
       """



    def testParseGoodJson(self):
        self.assertTrue(pgn_module.parse_lichess_json(self.json1))

    def testParseBadJson(self):
        self.assertEqual(None, pgn_module.parse_lichess_json("JUNK"))

    def testAnnotator(self):
        ""
        pgn_module.parse_lichess_json(self.json1)
        self.assertEqual("lichess.org", pgn_module.annotator())

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

    def testMoves(self):
        json1 = '{"moves": "g3 e6 Bg2 Nf6 Bxb7"}'
        pgn_module.parse_lichess_json(json1)
        
        self.assertEqual(3, len(pgn_module.moves()))
        self.assertEqual("g3", pgn_module.moves()[0][0])
        self.assertEqual("e6", pgn_module.moves()[0][1])
        self.assertEqual("Bg2", pgn_module.moves()[1][0])
        self.assertEqual("Nf6", pgn_module.moves()[1][1])
        self.assertEqual("Bxb7", pgn_module.moves()[2][0])

    def testPgnMoves(self):
        json1 = '{"moves": "g3 e6 Bg2 Nf6 Bxb7"}'
        pgn_module.parse_lichess_json(json1)

        self.assertTrue(re.search("1. g3 e6 2. Bg2 Nf6", pgn_module.pgnString()))
        self.assertIsNone(re.search("4.", pgn_module.pgnString()))

    def testPlyCount(self):
        
        pgn_module.parse_lichess_json('{"moves": "g3 e6 Bg2 Nf6"}')
        self.assertEqual(4, pgn_module.plyCount())

        pgn_module.parse_lichess_json(self.json1)
        self.assertEqual(7, pgn_module.plyCount())

    def testPgnFull(self):
        pgn_module.parse_lichess_json(self.json1)
        self.assertTrue(re.search('\[Date "2015.02.07"]' , pgn_module.pgnString()))
        self.assertTrue(re.search('\[White "white1"]' , pgn_module.pgnString()))
        self.assertTrue(re.search('\[Black "black1"]' , pgn_module.pgnString()))
        self.assertTrue(re.search('\[Result "1-0"]' , pgn_module.pgnString()))
        self.assertTrue(re.search('\[WhiteElo "1489"]' , pgn_module.pgnString()))
        self.assertTrue(re.search('\[BlackElo "1447"]' , pgn_module.pgnString()))
        self.assertTrue(re.search('\[ECO "A00"]' , pgn_module.pgnString()))
        self.assertTrue(re.search('\[Opening "Hungarian Opening, General"]' , pgn_module.pgnString()))
        self.assertTrue(re.search('\[Annotator "lichess.org"]' , pgn_module.pgnString()))

    def testECO(self):
        ""
        eco_json = """{
            "opening": {
                "code": "A00",
                "name": "Hungarian Opening, General"
            }}"""

        pgn_module.parse_lichess_json(eco_json)
        self.assertEqual("A00", pgn_module.eco())

    def testElo(self):
        pgn_module.parse_lichess_json(self.json1)
        self.assertEqual(1489, pgn_module.whiteElo())
        self.assertEqual(1447, pgn_module.blackElo())

    def testOpening(self):
        pgn_module.parse_lichess_json(self.json1)
        self.assertEqual("Hungarian Opening, General", pgn_module.opening())

    def testResult(self):
        result_json = '{"winner": "white"}'
        pgn_module.parse_lichess_json(result_json)
        self.assertEqual("1-0", pgn_module.result())

        result_json = '{"winner": "black"}'
        pgn_module.parse_lichess_json(result_json)
        self.assertEqual("0-1", pgn_module.result())

        pgn_module.parse_lichess_json(self.json2)
        self.assertEqual("1/2-1/2", pgn_module.result())

if __name__ == "__main__":
    unittest.main()
