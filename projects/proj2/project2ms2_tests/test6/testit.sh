#!/bin/bash
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m'
total=0
fail=0
testname=$0
serverlog=../../../server_output.txt
#set -x

msg="Test 6 works as following:
1. launch unix command: 
       python3.6 ./receiver.py 7006 > RECEIVED_FILE &
2. launch the forwarder which is the unreliable link b/w receiver and sender
       python3.6 ./forwarder.py 7008 7006 &
3. send data: 
       cat SMALL_FILE | python3.6 ./sender.py 127.0.0.1 7008
4. Compare files are the same
       check if forwarder.py exit 0 (pipelined) or 1 (stop-and-wait)"
echo "$msg"
python3.6 ./receiver.py 7008 > RECEIVED_FILE &
python3.6 ./forwarder.py 9006 7008 > RESULT &
cat SMALL_FILE | python3.6 ./sender.py 127.0.0.1 9006 &
sleep 20
sync
kill -9 $(lsof -t -i:9006) > /dev/null 2>&1
kill -9 $(lsof -t -i:7008) > /dev/null 2>&1

result=`cat RESULT`

if [ "$result" = "1" ]; then
        echo "using pipleine"
        exit 0
else
        echo -e "${RED}failed, not using pipeline ${NC}"
        exit 1
fi
