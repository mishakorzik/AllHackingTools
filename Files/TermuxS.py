import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  # \033[1;34m[ 1 ] >> \033[1;36;40mView MySystem")
print("  # \033[1;34m[ 2 ] >> \033[1;36;40mGoogle Search")
print("  # \033[1;34m[ 3 ] >> \033[1;36;40mPassGenerator")
print("  # \033[1;34m[ 4 ] >> \033[1;36;40mTermux Style")
print("  # \033[1;34m[ 5 ] >> \033[1;36;40mClear logs")
print("  # \033[1;34m[ 6 ] >> \033[1;36;40mExit system")
print("  # \033[1;34m[ 7 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("TermUxPane1: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash Files/ViewS.sh")
elif(op==2):
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("w3m http://google.com/")
elif(op==3):
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("bash src/PassGenerator.sh")
elif(op==4):
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("termux-style")
elif(op==5):
 os.system("cd")
 os.system("cd .. && cd usr/var/log/apt && rm -r history.log && rm -r term.log && rm -r eipp.log.xz && cd .. && rm -r alternatives.log")
 time.sleep(0.5)
 print("\033[1;31;40mTermux logs has been cleaned...")
 time.sleep(1)
 os.system("cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==6):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
elif(op==7):
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
