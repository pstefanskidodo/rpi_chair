import socket
import os

TCP_IP='0.0.0.0'
TCP_PORT=0000
BUFFER_SIZE=1024


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connected=False
try:
	if(KeyboardInterrupt):
		exit()
except Exception as e:
	while not connected:
		os.system('clear')
		try:
			s.connect((TCP_IP, TCP_PORT))
			connected = True
			print('Connected to tcp server')
		except Exception as e:
			print('Not connected')

if connected:
	data = s.recv(BUFFER_SIZE)
	