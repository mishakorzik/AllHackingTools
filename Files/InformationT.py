import requests
from bs4 import BeautifulSoup
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  # \033[1;34m[ 1 ] >> \033[1;36;40mEvilURL - Generate unicode evil domains for IDN Homograph Attack and detect them")
print("  # \033[1;34m[ 2 ] >> \033[1;36;40mDevploit - Simple Information Gathering Tool")
print("  # \033[1;34m[ 3 ] >> \033[1;36;40mOSIF - Open Source Information Facebook")
print("  # \033[1;34m[ 4 ] >> \033[1;36;40mExit Utility")
print("  # \033[1;34m[ 5 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("1pAdressHaCK: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd EvilURL && python3 evilurl.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Devploit && Devploit")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd OSIF && python2 osif.py")
elif(op==4):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
elif(op==5):
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
