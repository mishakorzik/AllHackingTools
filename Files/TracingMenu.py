import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mSeeker - Remote Access Trojan - RAT")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mTrape - People tracker on the Internet OSINT")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mExit System - log out AllHackingTools")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("IpTrac1Ng: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools")
 print("Open a second window in Termux and run ngrok on port 8080: ./ngrok http 8080")
 time.sleep(1.4)
 print("Warning AllHackingTools has already downloaded ngrok")
 time.sleep(2.3)
 os.system("cd && cd AllHackingTools && cd seeker && python3 seeker.py -t manual && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd trape && python trape.py && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==3):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting System...")
 sys.exit()
elif(op==4):
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 Files/AndroidMenu.py")
