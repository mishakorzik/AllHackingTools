import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  # \033[1;34m[ 1 ] >> \033[1;36;40mBattareyStatus - View a battarey status")
print("  # \033[1;34m[ 2 ] >> \033[1;36;40mCalsLogs - View a call log")
print("  # \033[1;34m[ 3 ] >> \033[1;36;40mWifiScanInfo - View wifi scan info")
print("  # \033[1;34m[ 4 ] >> \033[1;36;40mExit Utility")
print("  # \033[1;34m[ 5 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("Adm1nPAne1: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && termux-battery-status && python3 src/Timer.py && cd && cd AllHackingTools && python2 src/aboutMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && termux-call-log && python3 src/Timer.py && cd && cd AllHackingTools && python2 src/aboutMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && termux-wifi-scaninfo && python3 src/Timer.py && cd && cd AllHackingTools && python2 src/aboutMenu.py")
elif(op==4):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
elif(op==5):
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
