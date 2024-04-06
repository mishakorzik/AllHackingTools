import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mFacebook - Bruteforce attack on Facebook account using python")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mSherlock - Hunt social media accounts by username across social networks")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mFindUser - Find usernames across over 75 social networks")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mUserFinder - Find UserName in social")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mExit System - Log out AllHackingTools")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("Soc1alF1sh: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Facebook-BruteForce && python3 fb.py or python fb2.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Files && bash SherlockUser.sh")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd finduser && bash finduser.sh && cd && cd AllHackingTools && python3 src/Timer3.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd UserFinder && bash UserFinder.sh && cd && cd AllHackingTools && python3 src/Timer3.py")
elif(op==5):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting System..")
elif(op==6):
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 Files/SocialMenu.py")
