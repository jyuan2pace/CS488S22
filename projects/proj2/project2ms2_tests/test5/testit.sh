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
msg="Test 4 works as following:
1. launch unix command: 
       python3 ./receiver.py 5008 > RECEIVED_FILE
2. send data: 
       cat REAL_HUGE_FILE | python3 ./sender.py 127.0.0.1 5008
3. Compare files are the same
       diff RECEIVED_FILE REAL_HUGE_FILE"

echo "$msg"


i=0
succ=1
while [ $i -lt 10 ]
do
        python3.6 ./receiver.py 5009 > RECEIVED_FILE &
       	cat REAL_HUGE_FILE | python3.6 ./sender.py 127.0.0.1 5009 &
        sync
        sleep 50s
		kill -9 $(lsof -t -i:5009) > /dev/null 2>&1
		diff RECEIVED_FILE REAL_HUGE_FILE
        if [ $? != 0 ]; then
                succ=0
                break
        fi
        ((i++))
done

if [ $succ == 0 ]; then
        echo -e "${RED}failed [$testname] ${NC}"
        exit 1
else
        echo "passed $testname "
        exit 0
fi
