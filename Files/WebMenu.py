import requests
from bs4 import BeautifulSoup
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  # \033[1;34m[ 1 ] >> \033[1;36;40mAdminHack - Hack admin panel")
print("  # \033[1;34m[ 2 ] >> \033[1;36;40mSubDom - cname finder tool")
print("  # \033[1;34m[ 3 ] >> \033[1;36;40mBlazy - modern login bruteforcer")
print("  # \033[1;34m[ 4 ] >> \033[1;36;40mSqlMap - SQL injection and database takeover tool")
print("  # \033[1;34m[ 5 ] >> \033[1;36;40mWebSploit - An advanced MiTM Framework")
print("  # \033[1;34m[ 6 ] >> \033[1;36;40mSH33LL - Shell scanner")
print("  # \033[1;34m[ 7 ] >> \033[1;36;40mExit Utility")
print("  # \033[1;34m[ 8 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("Web-Hack1Ng: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd AdminHack && bash AdminHack.sh")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd takeover && python2 SubDom.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Blazy && python blazy.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd sqlmap-dev && python sqlmap.py -wizard")
elif(op==5):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd websploit && websploit")
elif(op==6):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd SH33LL && python sh33l.py")
elif(op==7):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
elif(op==8):
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
