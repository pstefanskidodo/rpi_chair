import socket
import os
import time
import sys
from curtsies import Input

from uuid import getnode


TCP_IP='192.168.0.111'
TCP_PORT=56789
BUFFER_SIZE=1024

h = iter(hex(getnode())[2:].zfill(12))
mac_address = "".join(i+next(h) for i in h)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connected=False
try:
	while not connected:
		os.system('clear')
		try:
			s.connect((TCP_IP, TCP_PORT))
			connected = True
			print('Connected to tcp server')
		except Exception as e:
			print('Not connected')
except KeyboardInterrupt:
	pass

if connected:
	data=''
	data = s.recv(BUFFER_SIZE)
	print(data.decode("utf-8"))
	data=data.decode("utf-8")
	parseList = data.split(';')
	print(parseList)
	id = parseList[1]
	print(id)
	rep_mess = "@1;" + id + ";" + mac_address + ";"
	print(rep_mess)
	s.send(rep_mess.encode("utf-8"))
	data = ''
	reactor = Input(keynames='curses')
	sttr=''
	with reactor:
		while True:
			try:
				e=Input(keynames='curses').send(0.05)
				left = False
				right = False
				up = False
				down = False
				#print(s.recv(BUFFER_SIZE).decode("utf-8").split(";"))
				if repr(e) == "'KEY_LEFT'":
					left = True
				if repr(e) == "'KEY_RIGHT'":
					right = True
				if repr(e) == "'KEY_UP'":
					up = True
				if repr(e) == "'KEY_DOWN'":
					down = True
				sttr = "@4;" + str(id) + ";" + "connected" + ";" + str(10) + ";" + str(down) + ";" + str(right) + ";" + str(left) + ";" + str(up) + ";"
				s.send(sttr.encode("utf-8"))
				print(sttr)
			except KeyboardInterrupt:
				break
exit_mess = "@6;" + id + ";"
s.send(exit_mess.encode("utf-8"))
s.close()
print("Closing program")
	