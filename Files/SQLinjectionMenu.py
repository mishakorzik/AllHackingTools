import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  # \033[1;34m[ 1 ] >> \033[1;36;40mVirusInjection - create a virus in /sdcard/")
print("  # \033[1;34m[ 2 ] >> \033[1;36;40mMailHack - email hacker tool")
print("  # \033[1;34m[ 3 ] >> \033[1;36;40mExit Utility")
print("  # \033[1;34m[ 4 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("Iject1onTo0l: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Vitus2.0 && cp VirtualXposed.apk /sdcard/")
 print("Your virus has been created!")
 time.sleep(1)
 print("Find Your virus in /sdcard/")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Debinject && python debinject.py")
elif(op==3):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
elif(op==4):
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
