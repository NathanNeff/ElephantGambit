import json
import datetime
import itertools
import sys

pgn = {}

def pgnString():
    pgn_string = ""
    for k in ['Event', 'Site', 'Date', 'White', 'Black', 'Result', 'WhiteElo', 'BlackElo', 
              'TimeControl', 'ECO', 'Opening', 'Annotator']:
        try:
            pgn_string = pgn_string + "[%s \"%s\"]\n" % (k, str(pgn.get(k, '')))
        except UnicodeEncodeError as e:
            sys.stderr.write("Error with this:  " + pgn.get(k, ''))
            return ''


    for idx, val in enumerate(pgn['Moves']):
        pgn_string = pgn_string + str(idx+1) + ". " + val[0] + " " + val[1] + " "

    if result() != '':
        pgn_string = pgn_string + result()

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

def eco():
    return pgn.get('ECO', "")

def result():
    return pgn.get('Result', "")

def plyCount():
    return pgn.get('PlyCount', "")

def timeControl():
    return pgn.get('TimeControl', "")

def fill_pgn(pgn_json):
    pgn['White'] = pgn_json.get('players', {}).get('white', {}).get('userId', '')
    pgn['Black'] = pgn_json.get('players', {}).get('black', {}).get('userId', '')
    pgn['Site'] = pgn_json.get('url', '')
    pgn['ECO'] = pgn_json.get('opening', {}).get('code', '')
    pgn['Opening'] = pgn_json.get('opening', {}).get('name', '')
    pgn['Date'] = pgn_json.get('timestamp', '')
    if pgn['Date'] != '':
        pgn['Date'] = datetime.date.fromtimestamp(int(pgn['Date']) / 1000).strftime("%Y.%m.%d")

    l = pgn_json.get('moves', '').split()
    moves_iter  = itertools.izip_longest(fillvalue="", *[iter(l)] * 2)
    moves_list = []
    for move in moves_iter:
        moves_list.append(move)
    pgn['Moves'] = moves_list

    if moves_list:
        plyCount = len(moves_list) * 2
        if moves_list[-1][1] == '':
            plyCount = plyCount - 1

        pgn['PlyCount'] = plyCount

    if pgn_json.get('winner', '') == "white":
        pgn['Result'] = "1-0"
    elif pgn_json.get('winner', '') == "black":
        pgn['Result'] = "0-1"
    elif pgn_json.get('status', '') == "draw":
        pgn['Result'] = "1/2-1/2"

    pgn['WhiteElo'] = pgn_json.get('players', {}).get('white', {}).get('rating', '')
    pgn['BlackElo'] = pgn_json.get('players', {}).get('black', {}).get('rating', '')
    pgn['Annotator'] = 'lichess.org'

    initial_clock = pgn_json.get('clock', {}).get('initial', '')
    increment = pgn_json.get('clock', {}).get('increment', '')
    if initial_clock != '' and increment != '':
        pgn['TimeControl'] = "%s+%s" % (initial_clock, increment)
    else:
        pgn['TimeControl'] = initial_clock

    if pgn_json.get('rated', '') == True:
        pgn['Event'] = "Rated game"
    else:
        pgn['Event'] = "Rated game"
    

def whiteElo():
    return pgn.get('WhiteElo', '')

def blackElo():
    return pgn.get('BlackElo', '')

def opening():
    return pgn.get('Opening', '')

def annotator():
    return pgn.get('Annotator', '')

def event():
    return pgn.get('Event', '')

def parse_lichess_json(json_text):
    
    json_object = None
    if type(json_text) is dict:
        json_object = json_text
    else:
        try:
            json_object = json.loads(json_text)

        except ValueError as e:
            return None

    fill_pgn(json_object)

    return True


