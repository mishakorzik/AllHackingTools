import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mShark - Future Of Phishing With less delay")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mZphisher - An automated phishing tool with 30+ templates")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mShellphish - Modded version of shellphish")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mSayCheese - Grab target's webcam shots by link")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mBlackPhish - It's easy phishing tool")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mUserRecon - find people from social")
print("  \033[1;34m[ 07 ] >> \033[1;36;40mMask Phish - An masking phishing url")
print("  \033[1;34m[ 08 ] >> \033[1;36;40mSeeker - Accurately Locate Smartphones")
print("  \033[1;34m[ 09 ] >> \033[1;36;40mAIOPhish - A Social Toolkit for phishing")
print("  \033[1;34m[ 10 ] >> \033[1;36;40mISeeYou- Find the exact location of the users)
print("  \033[1;34m[ 11 ] >> \033[1;36;40mExit System - log out AllHackingTools")
print("  \033[1;34m[ 12 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("Phish1ng: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd shark && shark && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd zphisher && bash zphisher.sh && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd ShellPhish && bash shellphish.sh && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd saycheese && bash saycheese.sh && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==5):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd BlackPhish && sudo python3 blackphish.py && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==6):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash Castom/userrecon.sh && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==7):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Mask-Phish.Termux && bash Mask-Phish.sh && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==8):
 os.system("clear")
 os.system("cd && cd AllHackingTools")
 print("Open a second window in Termux and run ngrok on port 8080: ./ngrok http 8080")
 time.sleep(1.4)
 print("Warning AllHackingTools has already downloaded ngrok")
 time.sleep(2.3)
 os.system("cd && cd AllHackingTools && cd seeker && python3 seeker.py -t manual && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==9):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd AIOPhish && bash aiophish.sh && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==10):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd I-See-You && ./ISeeYou.sh && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==11):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting System...")
 sys.exit()
elif(op==12):
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 Files/PhishingMenu.py")
 
