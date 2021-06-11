import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  # \033[1;34m[ 01 ] >> \033[1;36;40mRouterSploit - universality instrument for hacking rounters")
print("  # \033[1;34m[ 02 ] >> \033[1;36;40mWebSploit - An advanced MiTM Framework")
print("  # \033[1;34m[ 03 ] >> \033[1;36;40mCommix - OS Command Injection Exploitation Tool.")
print("  # \033[1;34m[ 04 ] >> \033[1;36;40mTxtool - an easy pentesting tool.")
print("  # \033[1;34m[ 05 ] >> \033[1;36;40mExit Utility")
print("  # \033[1;34m[ 06 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("RouterHack: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd routersploit && python3 rsf.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd websploit && sudo websploit")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd commix && python commix.py --wizard")
elif(op==4):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd txtool && txtool")
elif(op==5):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
elif(op==6):
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 Files/RouterMenu.py")
 
