import requests
import os
import time
import random
import sys

os.system("clear")
os.system("bash src/Logo.sh")
os.system("bash src/MenuOps.sh")

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
bl="\033[1;36;40m"

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
 os.system("python2 Files/Other.py")
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
 os.system("cd && cd AllHackingTools && bash src/Logo.sh")
 print("\033[1;31;40mExiting System...")
 time.sleep(0.7)
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
except KeyboardInterrupt:
        os.system("cd && cd AllHackingTools && bash src/Logo.sh")
	print("\n%Exiting System..."%(c))
