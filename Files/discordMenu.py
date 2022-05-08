import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mDSLeaks - Discord Leak mass users information")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mDSHub - Discord Leak users ")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mDSLookup - Discord Mass Lookup")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mDSHT - Discord History Tracker")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mBack To MainMenu")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mExit System")

op=int(raw_input("D1sc0Rd: "))

if(op==1):
 print("Go to the site and enter the ID of the user you want to track.")
 print("website: https://discordleaks.unicornriot.ninja/discord/users")
elif(op==2):
 print("Go to the site and enter the ID of the user you want to track.")
 print("website: https://discordhub.com/user/search")
elif(op==3):
 print("Go to the site and enter the ID of the user you want to track.")
 print("website: https://discord.id/")
elif(op==4):
 print("Go to the site and enter the ID of the user you want to track.")
 print("website: https://dht.chylex.com/")
elif(op==5):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting System...")
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
 os.system("python2 Files/discordMenu.py")
