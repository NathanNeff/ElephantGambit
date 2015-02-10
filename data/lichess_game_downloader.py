#!/bin/env python
import json
import time
import requests
import sys
import pgn_module

max_games = 10000
sleep_time = 60
max_time = 600 * 30
max_list_requests = 100
list_requests = 0
imported_games = {}
start_time = time.time()
stop = False

class LichessDownloader():

    def __init__(self, maxTime=60, maxRequests=0):
        ""
        self.games = {}
        self.start_time = time.time()
        self.maxTime = time.time() + maxTime
        self.maxRequests = maxRequests
        self.num_requests = 0
        
    # Allow easy mocking of this method for testing
    def getNow(self):
        return time.time()

    def getRunningTime(self):
        return self.getNow() - self.start_time
        
    def gameCount(self):
        return len(self.games)

    def addGame(self, gameId):
        if not self.games.get(gameId):
            self.games[gameId] = 1

    def get_game_request():
        # API docs:  https://github.com/ornicar/lila#http-api
        url = "http://en.lichess.org/api/game?rated=1&nb=200&with_moves=1&with_opening=1"
        req = requests.get(url)
        global list_requests
        list_requests = list_requests + 1
        # json_data = open('lichess.json')
        # data = json.load(json_data)
        # print json.dumps(data, indent=4)
        # return req.json()
        # sys.stderr.write("Game:  " + req.json())
        return req.json()


    def get_game_info_from_request():
        data = get_game_request()

        for game in data["list"]:
            
            if game["id"] in imported_games:
                sys.stderr.write("Already imported game: %s\n" % game["id"])
                imported_games[game["id"]] = imported_games[game["id"]] + 1
            else:
                sys.stderr.write("New game found: %s\n" % game["id"])
                pgn_module.parse_lichess_json(game)
                print pgn_module.pgnString(), "\n"
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

    def maxTimeTriggered(self):
        return self.getNow() > self.maxTime

    def begin_import():
        while keep_importing():
            get_game_info_from_request()
            for i in range(sleep_time):
                sys.stderr.write("Sleeping %d\n" % i)
                time.sleep(1)

    def keep_importing(self):
        global games_imported
        games_imported = len(imported_games.keys())
        return stop == False and program_run_time < max_time and games_imported < max_games and list_requests < max_list_requests

    def numRequests(self):
        return self.num_requests
        
    def maxRequestsTriggered(self):
        return self.numRequests() >= self.maxRequests

    def getNumGamesImported(self):
        return self.gamesImported

if __name__ == "__main__":
    begin_import()
