import requests
from bs4 import BeautifulSoup
import os
import time
import random
import sys

os.system("clear")
os.system("bash Logo.sh")

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
Purple="\033[0;35m"

print("  # \033[1;34m[ 01 ] >> \033[1;36;40mPhishing-Tool")
print("  # \033[1;34m[ 02 ] >> \033[1;36;40mRouter-Hacking")
print("  # \033[1;34m[ 03 ] >> \033[1;36;40mMail-Hack")
print("  # \033[1;34m[ 04 ] >> \033[1;36;40mWeb-HACKING & DDOS")
print("  # \033[1;34m[ 05 ] >> \033[1;36;40mWeb-AdminHack")
print("  # \033[1;34m[ 06 ] >> \033[1;36;40mAndroid-Hack")
print("  # \033[1;34m[ 07 ] >> \033[1;36;40mSQL injection-Tool")
print("  # \033[1;34m[ 08 ] >> \033[1;36;40mSocialMedia-Hacking")
print("  # \033[1;34m[ 09 ] >> \033[1;36;40mAnon-SMS_Tool")
print("  # \033[1;34m[ 10 ] >> \033[1;36;40mDarkSearch-Tool")
print("  # \033[1;34m[ 11 ] >> \033[1;36;40mOther tools")
print("  # \033[1;34m[ 12 ] >> \033[1;36;40mUpdate System")
print("  # \033[1;34m[ 13 ] >> \033[1;36;40mAbout Utility")
print("  # \033[1;34m[ 14 ] >> \033[1;36;40mExit Utility")

op=int(raw_input("Options: "))

if(op==1):
 os.system("python2 Files/PhishingMenu.py")
elif(op==2):
 os.system("python2 Files/RouterMenu.py")
elif(op==3):
 os.system("python2 Files/MailMenu.py")
elif(op==4):
 os.system("python2 Files/WebMenu.py")
elif(op==5):
 os.system("cd AdminHack")
 os.system("bash AdminHack.sh")
 os.system("cd")
 os.system("cd AllHackingTools")
elif(op==6):
 os.system("python2 Files/AndroidMenu.py")
elif(op==7):
 os.system("python2 SQLinjectionMenu.py")
elif(op==8):
 os.system("python2 SocialMenu.py")
elif(op==9):
 os.system("bash files/AnonSMSMenu.sh")
elif(op==10):
 os.system("python2 DarkSearchMenu.py")
elif(op==11):
 os.system("python2 MailHackMenu.py")
elif(op==12):
 time.sleep(1)
 os.system("bash Files/Updater.sh")
elif(op==13):
 os.system("bash src/About.sh")

elif(op==14):
 print("\033[1;31;40mQuiting utility...")
 time.sleep(1)
 sys.exit()
else:
 print("\033[1;31;40mInvalid input. Quiting...")
 time.sleep(1)
 sys.exit()
