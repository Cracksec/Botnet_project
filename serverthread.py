import socket
import threading
import os
import sys


class client(threading.Thread):
	def __init__(self, ip, port, socket):
		threading.Thread.__init__(self)
		self.address = ip
		self.port = port
		self.socketclient = socket
	
	def run(self):
		while True:
			data = raw_input(">>")
			if data == 'deco':
				break
			if data == "":
					data = raw_input("target: ")
			self.socketclient.send(data)
			rec = self.socketclient.recv(1024)
			print str(rec)
#main
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 443
connection.bind((host, port))

while True:
	connection.listen(5)
	(clientsocket , (address, ports )) = connection.accept()
	newthread = client(address, ports, clientsocket)
	newthread.start()
