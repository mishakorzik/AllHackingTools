import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mAdminHack - Hack admin panel")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mSubDom - cname finder tool")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mBlazy - modern login bruteforcer")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mSqlMap - SQL injection and database takeover tool")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mWebSploit - An advanced MiTM Framework")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mSqlmate - A friend of SQLmap which will do what you always expected from SQLmap")
print("  \033[1;34m[ 07 ] >> \033[1;36;40mSH33LL - A Easy Shell scanner")
print("  \033[1;34m[ 09 ] >> \033[1;36;40mUltraDDos - Tool for ddos web sites")
print("  \033[1;34m[ 10 ] >> \033[1;36;40mExit System - log out AllHackingTools")
print("  \033[1;34m[ 11 ] >> \033[1;36;40mBack To MainMenu")


op=int(raw_input("Web-Hack1Ng: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd AdminHack && bash AdminHack.sh && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Files && bash SubDom.sh && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Blazy && python2 blazy.py && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd sqlmap-dev && python sqlmap.py -wizard && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==5):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd websploit && websploit && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==6):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd sqlmate && python2 sqlmate && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==7):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd SH33LL && python2 sh33l.py && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==8):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd py-ddoser && python ddos.py && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==9):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Ultra-DDos && python2 main.py && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==10):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting System...")
 sys.exit()
elif(op==11):
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 Files/WebMenu.py")
