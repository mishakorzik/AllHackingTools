import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  # \033[1;34m[ 01 ] >> \033[1;36;40mAdminHack - Hack admin panel")
print("  # \033[1;34m[ 02 ] >> \033[1;36;40mSubDom - cname finder tool")
print("  # \033[1;34m[ 03 ] >> \033[1;36;40mBlazy - modern login bruteforcer")
print("  # \033[1;34m[ 04 ] >> \033[1;36;40mSqlMap - SQL injection and database takeover tool")
print("  # \033[1;34m[ 05 ] >> \033[1;36;40mWebSploit - An advanced MiTM Framework")
print("  # \033[1;34m[ 06 ] >> \033[1;36;40mSqlmate - A friend of SQLmap which will do what you always expected from SQLmap")
print("  # \033[1;34m[ 07 ] >> \033[1;36;40mSH33LL - Shell scanner")
print("  # \033[1;34m[ 08 ] >> \033[1;36;40mExit Utility")
print("  # \033[1;34m[ 09 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("Web-Hack1Ng: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd AdminHack && bash AdminHack.sh")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd takeover && python2 SubDom.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Blazy && python2 blazy.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd sqlmap-dev && python sqlmap.py -wizard")
elif(op==5):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd websploit && websploit")
elif(op==6):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd sqlmate && python sqlmate")
elif(op==7):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd SH33LL && python sh33l.py")
elif(op==8):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
elif(op==9):
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
