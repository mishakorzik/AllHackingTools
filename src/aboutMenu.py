import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools")
os.system("bash src/Logo.sh")
os.system("bash src/MenuA.sh")

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
Purple="\033[0;35m"

op=int(raw_input("Y0uR D1ya: "))

if(op==1):
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
elif(op==2):
 print("\033[1;31;40mRebooting...")
 time.sleep(1)
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("bash AllHackingTool.sh")
elif(op==3):
 print("\033[1;31;40mQuiting system...")
 time.sleep(1)
 sys.exit()
else:
 print("\033[1;31;40mInvalid input. Back To MainMenu...")
 time.sleep(1)
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
 
