#!/bin/env python
import json
import time
import requests
import sys

max_games = 19
sleep_time = 30
max_time = 1 * 10
max_list_requests = 1
list_requests = 0
imported_games = {}
start_time = time.time()
stop = False

def get_game_request():
    url = "http://en.lichess.org/api/game?rated=1&nb=200"
    req = requests.get(url)
    # data = json.loads(req.json())
    # list_requests = list_requests + 1
    # json_data = open('lichess.json')
    # data = json.load(json_data)
    # print json.dumps(data, indent=4)
    return req.json()


def get_game_info_from_request():
    data = get_game_request()

    for game in data["list"]:
        
        if game["id"] in imported_games:
            sys.stderr.write("Already imported game: %s\n" % game["id"])
            imported_games[game["id"]] = imported_games[game["id"]] + 1
        else:
            sys.stderr.write("New game found: %s\n" % game["id"])
            download_game(game["id"])
            imported_games[game["id"]] = 1

        sys.stderr.write("Game list has %i games\n" % len(imported_games.keys()))

def download_game(game_id):
    url = "http://en.lichess.org/%s/pgn" % game_id

    sys.stderr.write("Downloading game:  %s\n" % url)
    req = requests.get(url)

    if req.status_code == 200:
        sys.stderr.write("Request successful:  %s\n" % url)
        print req.content + "\n\n"
    else:
        print req.content
        stop = True

def begin_import():
    while keep_importing():
        get_game_info_from_request()

def keep_importing():
    program_run_time = time.time() - start_time
    games_imported = len(imported_games.keys())
    return stop == False and program_run_time < max_time and games_imported < max_games and list_requests < max_list_requests

begin_import()
