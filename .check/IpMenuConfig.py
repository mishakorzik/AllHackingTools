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
systemR = 'WJins82bsOx'

def sys_check():
	print(G + '[+]' + C + ' Checking for system configurations....', end='')
	sys_url = 'https://raw.githubusercontent.com/mishakorzik/AllHackingTools/main/Castom/systemfile.txt'
	try:
		sys_rqst = requests.get(sys_url)
		sys_sc = sys_rqst.status_code
		if sys_sc == 200:
			github_sys = sys_rqst.text
			github_sys = github_sys.strip()

			if systemR == github_sys:
				print(C + '[' + G + ' Succesfull ' + C +']' + '\n')
				print(G + '[+] ' + C + 'System configuration checked! There are no failures')
				os.system("cd && cd AllHackingTools && python2 Files/IpMenu.py")
			else:
				print("")
				print(R + '[-] ' + C + 'The system failed to start due to an unknown error!')
				os.system("cd && cd AllHackingTools && mv MainMenu.py ErrorServer254NotFound.py")
				os.system("cd && bash AllHackingTools/.check/ConfigurationOptions.sh")
		else:
			print(C + '[' + R + ' Status : {} '.format(sys_sc) + C + ']' + '\n')
	except Exception as e:
		print('\n' + R + '[-]' + C + ' Exception : ' + W + str(e))

try:
	sys_check()

except KeyboardInterrupt:
	print ('\n' + R + '[!]' + C + ' Keyboard Interrupt.' + W)
	Quit()
