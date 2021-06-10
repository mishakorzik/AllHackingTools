import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  # \033[1;34m[ 01 ] >> \033[1;36;40mSMS-Bomber-300 - ultra bomber for 300 services")
print("  # \033[1;34m[ 02 ] >> \033[1;36;40mXLR8_BOMBER - hard bomber & cals")
print("  # \033[1;34m[ 03 ] >> \033[1;36;40mAnon-SMS - Send Messages Anonymously")
print("  # \033[1;34m[ 04 ] >> \033[1;36;40mSpymer - more options sms and cals bomber")
print("  # \033[1;34m[ 05 ] >> \033[1;36;40mAres-Bomb - medium bomber")
print("  # \033[1;34m[ 06 ] >> \033[1;36;40mExit Utility")
print("  # \033[1;34m[ 07 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("SpymER: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd SMS-Bomber-300-Free && python SMS-Bomber.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd XLR8_BOMBER && bash xlr8.sh")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Anon-SMS && bash Run.sh")
elif(op==4):
 os.system("clear")
 os.system("cd && cd AllHackingTools && spymer")
elif(op==5):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd AresBomb && python boom.py")
elif(op==6):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
elif(op==7):
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 Files/SpamMenu.py")
 
