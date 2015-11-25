#!/bin/bash

# seconds
POLL_FREQUENCY=60
USER=$USER
PORT=50011
URL="http://swift.rcc.uchicago.edu:$PORT/retrieve/$USER"
NAP=300
LOG="listener.log"

listen(){
    while :
    do
        message=$(curl -s -X GET $URL)
        if [[ "$?" != "0" ]]
        then
            echo "[FAIL] Unable to reach the server"
            sleep $NAP
        fi

        if [[ "$message" == "No new notifications" ]]
        then
            echo "None"
        else
            notify-send "$message"
        echo "Message : [$message]"
        fi
        sleep $POLL_FREQUENCY
    done

}

listen | tee -a $LOG
