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
counter = -1
with open('LOSEUS.txt', 'r') as f:
    shouldBeLost = [int(line.rstrip()) for line in f]

input = [serverSocket, clientSocket]
while True:
	inputready,outputready,exceptready = select(input,[],[])
	for s in inputready:
		if s == serverSocket:
			data, addr = serverSocket.recvfrom(buf)
			counter=counter+1
			if data:
				if (not counter in shouldBeLost):
					clientSocket.sendto(data, clientAddr)
				else:
					print("yucks, forwarder just ate your datagram!:", counter)
			#else:
			#	serverSocket.close()
			#	close1=True
		elif s == clientSocket:
			ack, ackaddr = clientSocket.recvfrom(100)
			if ack:
				serverSocket.sendto(ack, addr)
			#else:
			#	clientSocket.close()
			#	close2=True
		else:
			print("unknown socket:", s)
print("forwarder done")
