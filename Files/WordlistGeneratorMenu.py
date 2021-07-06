import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mWlcreator - Wordlist creator written in C")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mGoblinWordGenerator - Useful wordlist generator in python")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mSMWYG - tool allows you to perform OSINT and reconnaissance")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mExit System - log out AllHackingTools")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("Ma1lHacK: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd wlcreator && ./wlcreator 5 && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd GoblinWordGenerator && python3 goblin.py && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd SMWYG-Show-Me-What-You-Got && python3 SMWYG.py && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==4):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
elif(op==5):
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 Files/AndroidMenu.py")
