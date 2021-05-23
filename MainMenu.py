import requests
from bs4 import BeautifulSoup
import os
import time
import random
import sys

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
Purple="\033[0;35m"

print("  # \033[1;34m[ 1 ] >> \033[1;36;40mPhishing-Tool")
print("  # \033[1;34m[ 2 ] >> \033[1;36;40mSmS-Bomber")
print("  # \033[1;34m[ 3 ] >> \033[1;36;40mWifi-Jumming")
print("  # \033[1;34m[ 4 ] >> \033[1;36;40mWeb-DDOS")
print("  # \033[1;34m[ 5 ] >> \033[1;36;40mWeb-AdminHack")
print("  # \033[1;34m[ 6 ] >> \033[1;36;40mAndroid-Hack")
print("  # \033[1;34m[ 7 ] >> \033[1;36;40mSQL injection-Tool")
print("  # \033[1;34m[ 8 ] >> \033[1;36;40mSocialMedia-Finder")
print("  # \033[1;34m[ 9 ] >> \033[1;36;40mSocialMedia-Attack")
print("  # \033[1;34m[ 10 ] >> \033[1;36;40mDarkSearch-Tool")
print("  # \033[1;34m[ 11 ] >> \033[1;36;40mMail-Hack")
print("  # \033[1;34m[ 12 ] >> \033[1;36;40mMasking-url")
print("  # \033[1;34m[ 13 ] >> \033[1;36;40mAnon-SMS_Tool")
print("  # \033[1;34m[ 14 ] >> \033[1;36;40mUpdate Utility")
print("  # \033[1;34m[ 15 ] >> \033[1;36;40mAbout Utility")
print("  # \033[1;34m[ 16 ] >> \033[1;36;40mExit Utility")

op=int(raw_input("Options: "))

if(op==1):
 os.system("Python2 PhishingMenu.py")
elif(op==2):
 os.system("Python2 SMSbomberMenu.py")
elif(op==3):
 os.system("WifiJummingMenu.py")
elif(op==4):
 os.system("WebDDOSMenu.py")
elif(op==5):
 os.system("WebAdminHackMenu.py")
elif(op==6):
 os.system("AndroidHackMenu.py")
elif(op==7):
 os.system("SQLinjectionMenu.py")
elif(op==8):
 os.system("SocialFinderMenu.py")
elif(op==9):
 os.system("SocialAttackMenu.py")
elif(op==10):
 os.system("DarkSearchMenu.py")
elif(op==11):
  os.system("MailHackMenu.py")
elif(op==12:
 os.system("MaskingUrlMenu.py")
elif(op==13):
 os.system("AnonSMSMenu.py")
elif(op==14):

elif(op==15):
 os.system("python2 About.py")
elif(op==16):
 print("\033[1;31;40mQuiting utility...")
 time.sleep(1)
 sys.exit()
else:
 print("\033[1;31;40mInvalid input. Quiting...")
 time.sleep(1)
 sys.exit()
