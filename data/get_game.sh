#!/bin/bash
if [ -z $1 ]; then
    echo "Usage: $0 <gameid> <pgn|json>"
    exit 1
fi

if [[ "$2" == "pgn" ]]; then
    URL="http://en.lichess.org/game/export/$1.pgn"
else
    URL="http://en.lichess.org/api/game/$1?with_moves=1"
fi
echo $URL
curl -v $URL
echo "\n"

