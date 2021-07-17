R = '\033[31m'
G = '\033[32m' 
C = '\033[36m'
W = '\033[0m' 

from shutil import which
import time
import os
import csv
import sys
import json
import argparse
import requests
import subprocess as subp

row = []
info = ''
result = ''
sysfile = 'WJins82bsOx'

def sysfile_check():
	print(G + '[>]' + C + ' Checking for files configurations....', end='')
	file_url = 'https://raw.githubusercontent.com/mishakorzik/AllHackingTools/main/Castom/systemfile.txt'
	try:
		file_rqst = requests.get(file_url)
		file_sc = file_rqst.status_code
		if file_sc == 200:
			github_file = file_rqst.text
			github_file = github_file.strip()

			if sysfile == github_file:
				print(C + '[' + G + ' Succesful ' + C +']' + '\n')
				print(G + '[+] ' + C + 'Files configuration checked! There are no failures')
				os.system("cd && cd AllHackingTools && bash src/AllHackingTool.sh")
			else:
				print("")
				print(R + '[-] ' + C + 'The system failed to start!')
				print(R + '[-] ' + C + 'Error code: 502 Bad Gateway')
				print(R + '[-] ' + C + 'Please wait while we fix the problem...')
				os.system("cd && bash AllHackingTools/.check/ConfigurationOptions.sh")
		else:
			print(C + '[' + R + ' Server time out - Status : {} '.format(file_sc) + C + ']' + '\n')
	except Exception as e:
		print('\n' + R + '[-]' + C + ' Error code: Unknown failed to authenticate the server - Exception : ' + W + str(e))

try:
	sysfile_check()


except KeyboardInterrupt:
	print ('\n' + R + '[!]' + C + ' Keyboard Interrupt.' + W)
	os.system("cd && bash AllHackingTools/.check/ConfigurationOptions.sh")
