import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  # \033[1;34m[ 01 ] >> \033[1;36;40mAstraNmap - Security scanner used to find hosts and services on a computer network")
print("  # \033[1;34m[ 02 ] >> \033[1;36;40mRed Hawk - Information Gathering, Vulnerability Scanning and Crawling")
print("  # \033[1;34m[ 03 ] >> \033[1;36;40mWeeman - HTTP server for phishing in python")
print("  # \033[1;34m[ 04 ] >> \033[1;36;40mTM-scanner - websites vulnerability scanner for termux")
print("  # \033[1;34m[ 05 ] >> \033[1;36;40mRang3r - Multi Thread IP + Port Scanner")
print("  # \033[1;34m[ 06 ] >> \033[1;36;40mSqlmap - Automatic SQL injection and database takeover tool")
print("  # \033[1;34m[ 07 ] >> \033[1;36;40mMaxSubdoFinder - Tool for Discovering Subdomain")
print("  # \033[1;34m[ 08 ] >> \033[1;36;40mEasymap - Nmap Shortcut")
print("  # \033[1;34m[ 09 ] >> \033[1;36;40mExit Utility")
print("  # \033[1;34m[ 10 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("1nf0rmatI0n: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd AstraNmap && bash astranmap.sh")
elif(op==8):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Easymap && php easymap.php")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd weeman && python2 weeman.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd RED_HAWK && php rhawk.php")
elif(op==4):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd TM-scanner && python2 tmscanner.py")
elif(op==7):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd MaxSubdoFinder && python2 maxteroit.py")
elif(op==6):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd sqlmap-dev && python sqlmap.py -wizard")
elif(op==5):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd rang3r && python2 rang3r.py --ip 192.168.0.1")
elif(op==9):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
elif(op==10):
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 Files/AnalistickMenu.py")
