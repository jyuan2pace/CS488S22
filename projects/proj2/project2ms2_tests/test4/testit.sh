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
Repeat the following test 10 times, each time with different acks dropped:
1. launch unix command: 
       python3.6 ./receiver.py 6006 > RECEIVED_FILE &
2. launch the forwarder which is the unreliable link b/w receiver and sender
       python3.6 ./forwarder.py 6008 6006 &
   SMALL_FILE contains 7-8 chunks, and forwarder drops 30% of acks.ewww!.
3. send data: 
       cat SMALL_FILE | python3.6 ./sender.py 127.0.0.1 6008
4. Compare files are the same
       diff RECEIVED_FILE SMALL_FILE"

echo "$msg"

i=0
fail=0
while [ $i -lt 10 ]; do
    let i=i+1 
	python3.6 ./generate_loseme.py 7 0.3
	python3.6 ./receiver.py 6008 > RECEIVED_FILE &
	python3.6 ./forwarder.py 6006 6008 &
	cat SMALL_FILE | python3.6 ./sender.py 127.0.0.1 6006 &
	sleep 30s
	sync
	diff RECEIVED_FILE SMALL_FILE
	if [ $? != 0 ]; then
		let fail=fail+1 
	fi
	kill -9 $(lsof -t -i:6006) > /dev/null 2>&1
	kill -9 $(lsof -t -i:6008) > /dev/null 2>&1
done

if [ $fail != 0 ]; then
        echo -e "${RED}failed [$fail /10] times ${NC}"
        exit 1
else
        echo "passed $testname "
        exit 0
fi
