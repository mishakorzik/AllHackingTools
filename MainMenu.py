import requests
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

g="\033[1;32m"
r="\033[1;31m"
w="\033[0m"
b="\033[1;34m"
o="\033[1;33m"

print("  # \033[1;34m[ 01 ] >> \033[1;36;40mInformation Gathering:  -  Collects information from a different database")
print("  # \033[1;34m[ 02 ] >> \033[1;36;40mExploitation-Tools:  -  selection of tools for operation and hacking")
print("  # \033[1;34m[ 03 ] >> \033[1;36;40mSniffing and Spoofing:  -  Tools for forgery of data and databases")
print("  # \033[1;34m[ 04 ] >> \033[1;36;40mWeb Hacking:  -  Tools for hacking websites and servers")
print("  # \033[1;34m[ 05 ] >> \033[1;36;40mCam Hacking:  -  Tools for hacking cams and front camera")
print("  # \033[1;34m[ 06 ] >> \033[1;36;40mAndroid Hack:  -  Utilities for creating RAT virus ")
print("  # \033[1;34m[ 07 ] >> \033[1;36;40mSQL injection-Tool:  -  Tools for creating viruses")
print("  # \033[1;34m[ 08 ] >> \033[1;36;40mSocialMedia-Hacking:  -  Tools for hacking social networks")
print("  # \033[1;34m[ 09 ] >> \033[1;36;40mSMS-spaming Tools:  -  Utilities for spam and anonymous SMS")
print("  # \033[1;34m[ 10 ] >> \033[1;36;40mVulnerability Analysis:  -  Systems for vulnerability analysis")
print("  # \033[1;34m[ 11 ] >> \033[1;36;40mDarkSearch-Tool:  -  Tools for Secret and Onion search ")
print("  # \033[1;34m[ 12 ] >> \033[1;36;40mPhishing-Tool:  -  Tools for phishing and fake websites")
print("  # \033[1;34m[ 13 ] >> \033[1;36;40mPassworld Attack:  -  Utilities for cracking passwords")
print("  # \033[1;34m[ 14 ] >> \033[1;36;40mOther tools:  -  Separate and other tools for hacking")
print("  # \033[1;34m[ 15 ] >> \033[1;36;40mTermux Panel:  -  Termux control and special features")
print("")
print("  # \033[1;34m[ 16 ] >> \033[1;36;40mUpdate System:  -  Update system and all tools & menu")
print("  # \033[1;34m[ 17 ] >> \033[1;36;40mAbout System:  -  View system information and developer")
print("  # \033[1;34m[ 18 ] >> \033[1;36;40mExit System:  -  log out system")

op=int(raw_input("Options: "))

if(op==1):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/IpMenu.py")
elif(op==2):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/RouterMenu.py")
elif(op==3):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/MailMenu.py")
elif(op==4):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/WebMenu.py")
elif(op==5):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/CamHackMenu.py")
elif(op==6):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/AndroidMenu.py")
elif(op==7):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/SQLinjectionMenu.py")
elif(op==8):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/SocialMenu.py")
elif(op==9):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/SpamMenu.py")
elif(op==10):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/AnalistickMenu.py")
elif(op==11):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/DarkSearchMenu.py")
elif(op==12):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/PhishingMenu.py")
elif(op==13):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/PassworldMenu.py")
elif(op==14):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("bash src/InfErr.sh")
elif(op==15):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/TermuxS.py")
elif(op==16):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 time.sleep(1)
 os.system("bash Files/Updater.sh")
elif(op==17):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("bash src/About.sh")
elif(op==18):
 print("\033[1;31;40mQuiting utility...")
 time.sleep(1)
 sys.exit()
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
