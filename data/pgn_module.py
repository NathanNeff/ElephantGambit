import json
import datetime
import itertools

pgn = {}

def pgnString():
    pgn_string = ""
    for idx, val in enumerate(pgn['Moves']):
        pgn_string = pgn_string + str(idx+1) + ". " + val[0] + " " + val[1] + " "
    return pgn_string

def moves():
    return pgn['Moves']


def white():
    return pgn.get('White', "")

def black():
    return pgn.get('Black', "")

def site():
    return pgn.get('Site', "")

def date():
    return pgn.get('Date', "")

def fill_pgn(pgn_json):
    pgn['White'] = pgn_json['players']['white']['userId']
    pgn['Black'] = pgn_json['players']['black']['userId']
    pgn['Site'] = pgn_json['url']
    pgn['Date'] = datetime.date.fromtimestamp(int(pgn_json['timestamp']) / 1000).strftime("%Y.%m.%d")
    l = pgn_json['moves'].split()
    moves_iter  = itertools.izip_longest(fillvalue="", *[iter(l)] * 2)
    moves_list = []
    for move in moves_iter:
        moves_list.append(move)
    pgn['Moves'] = moves_list


def parse_lichess_json(json_text):
    try:
        pgn_json = json.loads(json_text)

    except ValueError as e:
        return None

    fill_pgn(pgn_json)
    return True


