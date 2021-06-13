import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mCreate Banner")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mRemove Banner")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mExit Utility")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("BanNer: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Termux-Banner && bash t-ban.sh")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Termux-Banner && bash remove.sh")
elif(op==3):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
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
 os.system("python2 Files/SpamMenu.py")
 
