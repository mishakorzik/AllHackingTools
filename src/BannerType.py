import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mPoison")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mPuffy")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mAvatar")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mBloody")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mModular")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mDefault")
print("  \033[1;34m[ 07 ] >> \033[1;36;40mExit")

op=int(raw_input("TeRMuxBannER: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash src/CreateTermuxBannerPoison.sh")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash src/CreateTermuxBannerPuffy.sh")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash src/CreateTermuxBannerAvatar.sh")
elif(op==4):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash src/CreateTermuxBannerBloody.sh")
elif(op==5):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash src/CreateTermuxBannerModular.sh")
elif(op==6):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash src/CreateTermuxBanner.sh")
elif(op==7):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 Files/TermuxS.py")
