import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mLyzen - Telegram users information")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mTGSearch - Discord Leak users ")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mBack To MainMenu")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mExit System")

op=int(raw_input("D1sc0Rd: "))

if(op==1):
 print("Go to the site and enter everything that is listed on the site")
 print("website: https://lyzem.com/")
 os.system("cd && cd AllHackingTools && python src/Timer1.py && python2 MainMenu.py")
elif(op==2):
 print("Go to the site and enter everything that is listed on the site")
 print("website: https://search.buzz.im")
 os.system("cd && cd AllHackingTools && python src/Timer1.py && python2 MainMenu.py")
elif(op==3):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting System...")
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
 os.system("python2 Files/telegramMenu.py")
