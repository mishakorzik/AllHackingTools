import requests
from bs4 import BeautifulSoup
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  # \033[1;34m[ 1 ] >> \033[1;36;40mAstraNmap - Security scanner used to find hosts and services on a computer network")
print("  # \033[1;34m[ 2 ] >> \033[1;36;40mWeeman - HTTP server for phishing in python")
print("  # \033[1;34m[ 3 ] >> \033[1;36;40mRang3r - Tool for Discovering Subdomain")
print("  # \033[1;34m[ 4 ] >> \033[1;36;40mMaxSubdoFinder - Tool for Discovering Subdomain")
print("  # \033[1;34m[ 5 ] >> \033[1;36;40mEasymap - Nmap Shortcut")
print("  # \033[1;34m[ 6 ] >> \033[1;36;40mExit Utility")
print("  # \033[1;34m[ 7 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("1nf0rmatI0n: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd AstraNmap && bash astranmap.sh")
elif(op==5):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Easymap && php easymap.php")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd weeman && python2 weeman.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd MaxSubdoFinder && python2 maxteroit.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd rang3r && python rang3r.py --ip 192.168.0.1")
elif(op==6):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
elif(op==7):
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
