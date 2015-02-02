#!/bin/env python
import json
data = [ ]
json_data = open('lichess.json')
data = json.load(json_data)
# print json.dumps(data, indent=4)

imported_games = {}

def get_game_info_from_request():
    for game in data["list"]:
        
        if game["id"] in imported_games:
            print "Yep, game ", game["id"], " exists, and it's ", imported_games[game["id"]]
            imported_games[game["id"]] = imported_games[game["id"]] + 1
        else:
            print "Nope, game ", game["id"], " doesn't exist"
            imported_games[game["id"]] = 1

        print "----------------------------------------------------------------------"


get_game_info_from_request()
