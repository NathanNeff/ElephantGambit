while true; do
        fil=lichess-dump-`date +%F-%H-%M-%S`.json
        DEST=/ElephantGambit/raw_json/$fil
        curl "http://en.lichess.org/api/game?rated=1&nb=200&with_moves=1&with_opening=1" | hadoop fs -put - $DEST
        sleep 30
done
