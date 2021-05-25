import requests
from bs4 import BeautifulSoup
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  # \033[1;34m[ 1 ] >> \033[1;36;40mRouterSploit")
print("  # \033[1;34m[ 2 ] >> \033[1;36;40mWebSploit")
print("  # \033[1;34m[ 3 ] >> \033[1;36;40mCommix")
print("  # \033[1;34m[ 4 ] >> \033[1;36;40mExit")
print("  # \033[1;34m[ 5 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("RouterHack: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd routersploit && python3 rsf.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd websploit && sudo websploit")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Commix && sudo python commix.py --wizard")
elif(op==4):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
elif(op==5):
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
 
