#!/bin/env python
import json

imported_games = {}

def get_game_request():
    json_data = open('lichess.json')
    data = json.load(json_data)
    return data
    # print json.dumps(data, indent=4)


def get_game_info_from_request():
    data = get_game_request()

    for game in data["list"]:
        
        if game["id"] in imported_games:
            print "Yep, game ", game["id"], " exists, and it's ", imported_games[game["id"]]
            imported_games[game["id"]] = imported_games[game["id"]] + 1
        else:
            print "Nope, game ", game["id"], " doesn't exist"
            imported_games[game["id"]] = 1

        print "----------------------------------------------------------------------"
        print "game list has ", len(imported_games.keys()), "things in it"


get_game_info_from_request()
