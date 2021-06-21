
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

from shutil import which
import time

print(G + '[+]' + C + ' Checking Dependencies...' + W)
pkgs = ['python3', 'pip', 'php', 'ssh', 'pip2', 'wget', 'curl', 'python', 'python2', 'toilet', 'neofetch', 'figlet', 'lolcat', 'clang', 'w3m', 'jq', 'ruby', 'ssl', 'pv']
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
version = '1.6'
systemAHT = '1.2.4'

def ver_check():
	print(G + '[+]' + C + ' Checking for Updates....', end='')
	ver_url = 'https://raw.githubusercontent.com/mishakorzik/AllHackingTools/main/Castom/version.txt'
	try:
		ver_rqst = requests.get(ver_url)
		ver_sc = ver_rqst.status_code
		if ver_sc == 200:
			github_ver = ver_rqst.text
			github_ver = github_ver.strip()

			elif version == github_ver:
				print(C + '[' + G + ' No Updates ' + C +']' + '\n')
			else:
				print(C + '[' + R + ' Available : {} '.format(github_ver) + C + ']' + '\n')
		else:
			print(C + '[' + R + ' Status : {} '.format(ver_sc) + C + ']' + '\n')
	except Exception as e:
		print('\n' + R + '[-]' + C + ' Exception : ' + W + str(e))

def set_check():
	print(G + '[+]' + C + ' Checking Tools Setting....', end='')
	sys_url = 'https://raw.githubusercontent.com/mishakorzik/AllHackingTools/main/Castom/system.txt'
	try:
		sys_rqst = requests.get(sys_url)
		sys_sc = sys_rqst.status_code
		if sys_sc == 200:
			github_sys = sys_rqst.text
			github_sys = github_sys.strip()

			if systemAHT == github_sys:
				print(C + '[' + G + ' No System Updates ' + C +']' + '\n')
			else:
				print(C + '[' + R + ' The System Is Outdated : {} '.format(github_sys) + C + ']' + '\n')
		else:
			print(C + '[' + R + ' Status : {} '.format(sys_sc) + C + ']' + '\n')
	except Exception as e:
		print('\n' + R + '[-]' + C + ' Exception : ' + W + str(e))
try:
	ver_check()
        set_check()

except KeyboardInterrupt:
	print ('\n' + R + '[!]' + C + ' Keyboard Interrupt.' + W)
	Quit()
