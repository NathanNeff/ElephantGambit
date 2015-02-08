import json
import datetime

pgn = {}

def white():
    return pgn.get('White', "")

def black():
    return pgn.get('Black', "")

def site():
    return pgn.get('Site', "")

def date():
    return pgn.get('Date', "")

def parse_lichess_json(json_text):
    try:
        pgn_json = json.loads(json_text)
        pgn['White'] = pgn_json['players']['white']['userId']
        pgn['Black'] = pgn_json['players']['black']['userId']
        pgn['Site'] = pgn_json['url']
        pgn['Date'] = datetime.date.fromtimestamp(int(pgn_json['timestamp']) / 1000).strftime("%Y.%m.%d")
        return True
    except ValueError as e:
        return None
