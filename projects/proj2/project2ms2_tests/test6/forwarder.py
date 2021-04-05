# ----- forwarder.py -----
from socket import *
import sys
import random
from select import select
host="0.0.0.0"
listening_port = int(sys.argv[1])
sendto_port=int(sys.argv[2])
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind((host,listening_port))

serverAddr = (host,listening_port)
buf=2800

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientAddr = (host, sendto_port)

#load packet loss counter in
counter=0
pipeline=False
input = [serverSocket, clientSocket]
with open("RESULT", "w") as f:
	while True:
		inputready,outputready,exceptready = select(input,[],[])
		for s in inputready:
			if s == serverSocket:
				data, addr = serverSocket.recvfrom(buf)
				if data:
					clientSocket.sendto(data, clientAddr)
					counter=counter+1
			elif s == clientSocket:
				ack, ackaddr = clientSocket.recvfrom(100)
				if ack:
					serverSocket.sendto(ack, addr)
					counter=counter-1
					if(counter > 0):
						if(pipeline == False):
							pipeline=True
							f.write("1")
							f.flush()
			else:
				print("unknown socket:", s)
