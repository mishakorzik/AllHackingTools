
R = '\033[31m'
G = '\033[32m' 
C = '\033[36m'
W = '\033[0m' 

from shutil import which
import time

print(G + '[+]' + C + ' Checking Dependencies And Packages...' + W)
pkgs = ['python3', 'pip', 'php', 'ssh', 'pip2', 'wget', 'curl', 'python', 'python2', 'toilet', 'neofetch', 'figlet', 'lolcat', 'clang', 'w3m', 'jq', 'ruby', 'pv']
inst = True
for pkg in pkgs:
	present = which(pkg)
	if present == None:
		print(R + '[-] ' + W + pkg + C + ' is not Installed!')
		inst = False
	else:
		pass
if inst == False:
	exit()
else:
	pass

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
version = '1.7'

def ver_check():
	print(G + '[+]' + C + ' Checking the AllHackingTools for updates....', end='')
	ver_url = 'https://raw.githubusercontent.com/mishakorzik/AllHackingTools/main/Castom/version.txt'
	try:
		ver_rqst = requests.get(ver_url)
		ver_sc = ver_rqst.status_code
		if ver_sc == 200:
			github_ver = ver_rqst.text
			github_ver = github_ver.strip()

			if version == github_ver:
				print(C + '[' + G + ' No Updates ' + C +']' + '\n')
			else:
				print(C + '[' + R + ' Available : {} '.format(github_ver) + C + ']' + '\n')
				print(R + '[-] ' + C + 'Please update the system: msdconsoleUPD')
		else:
			print(C + '[' + R + ' Status : {} '.format(ver_sc) + C + ']' + '\n')
	except Exception as e:
		print('\n' + R + '[-]' + C + ' Exception : ' + W + str(e))

try:
	ver_check()

except KeyboardInterrupt:
	print ('\n' + R + '[!]' + C + ' Keyboard Interrupt.' + W)
	Quit()
