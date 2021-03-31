i=0
succ=1
while [ $i -lt 10 ]
do
        timeout 5s python3 ./receiver.py 5009 > RECEIVED_FILE &
        timeout 5s cat REAL_HUGE_FILE | python3 ./sender.py 127.0.0.1 5009
        sync
        sleep 5s
        diff RECEIVED_FILE REAL_HUGE_FILE
        if [ $? != 0 ]; then
                succ=0
                break
        fi
        ((i++))
done
if [ $succ == 1 ]; then
        echo -e "failed"
        exit 1
else
        echo "passed "
        exit 0
fi
