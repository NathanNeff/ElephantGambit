import json
import datetime
import itertools

pgn = {}

def pgnString():
    pgn_string = ""
    for k in ['White', 'Black', 'Result', 'WhiteElo', 'BlackElo']:
        pgn_string = pgn_string + "[%s \"%s\"]\n" % (k, str(pgn.get(k, '')))

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

def eco():
    return pgn.get('Eco', "")

def result():
    return pgn.get('Result', "")

def fill_pgn(pgn_json):
    pgn['White'] = pgn_json.get('players', {}).get('white', {}).get('userId', '')
    pgn['Black'] = pgn_json.get('players', {}).get('black', {}).get('userId', '')
    pgn['Site'] = pgn_json.get('url', '')
    pgn['Eco'] = pgn_json.get('opening', {}).get('code', '')
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
    if pgn_json.get('winner', '') == "white":
        pgn['Result'] = "1-0"
    elif pgn_json.get('winner', '') == "black":
        pgn['Result'] = "0-1"
    elif pgn_json.get('status', '') == "draw":
        pgn['Result'] = "1/2-1/2"

    pgn['WhiteElo'] = pgn_json.get('players', {}).get('white', {}).get('rating', '')
    pgn['BlackElo'] = pgn_json.get('players', {}).get('black', {}).get('rating', '')
    pgn['Annotator'] = 'lichess.org'
    

def whiteElo():
    return pgn.get('WhiteElo', '')

def blackElo():
    return pgn.get('BlackElo', '')

def opening():
    return pgn.get('Opening', '')

def annotator():
    return pgn.get('Annotator', '')

def parse_lichess_json(json_text):
    try:
        pgn_json = json.loads(json_text)

    except ValueError as e:
        return None

    fill_pgn(pgn_json)
    return True


