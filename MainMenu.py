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
print("  # \033[1;34m[ 8 ] >> \033[1;36;40mSocialMefia-Finder")
print("  # \033[1;34m[ 9 ] >> \033[1;36;40mDarkSearch-Tool")
print("  # \033[1;34m[ 10 ] >> \033[1;36;40mMail-Hack")
print("  # \033[1;34m[ 11 ] >> \033[1;36;40m")
print("  # \033[1;34m[ 12 ] >> \033[1;36;40mEXIT")
print("  # \033[1;34m[ 13 ] >> \033[1;36;40mEXIT")
print("  # \033[1;34m[ 14 ] >> \033[1;36;40mEXIT")
print("  # \033[1;34m[ 15 ] >> \033[1;36;40mEXIT")

op=int(raw_input("Options: "))

if(op==1):
 bash Default.sh
elif(op==2):
 bash Import.sh
elif(op==3):
 print("\033[1;31;40mQuiting utility...")
 time.sleep(1)
 sys.exit()
else:
 print("\033[1;31;40mInvalid input. Quiting...")
 time.sleep(1)
 sys.exit()
