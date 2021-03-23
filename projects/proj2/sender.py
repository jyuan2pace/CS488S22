# ----- sender.py ------

#!/usr/bin/env python
from socket import *
import sys

s = socket(AF_INET,SOCK_DGRAM)
host =sys.argv[1]
port = 9999
buf =1024
addr = (host,port)

f=open("a.txt","rb")
data = f.read(buf)
while (data):
    if(s.sendto(data,addr)):
        print("sending ...")
        data = f.read(buf)
s.close()
f.close()
