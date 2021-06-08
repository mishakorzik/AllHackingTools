import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  # \033[1;34m[ 01 ] >> \033[1;36;40mShark - Future Of Phishing With less delay")
print("  # \033[1;34m[ 02 ] >> \033[1;36;40mZphisher - An automated phishing tool with 30+ templates")
print("  # \033[1;34m[ 03 ] >> \033[1;36;40mShellphish - Modded version of shellphish")
print("  # \033[1;34m[ 04 ] >> \033[1;36;40mSayCheese - Grab target's webcam shots by link")
print("  # \033[1;34m[ 05 ] >> \033[1;36;40mBlackPhish - It's easy phishing tool")
print("  # \033[1;34m[ 06 ] >> \033[1;36;40mUserRecon - find people from social")
print("  # \033[1;34m[ 07 ] >> \033[1;36;40mMask Phish - An masking phishing url")
print("  # \033[1;34m[ 08 ] >> \033[1;36;40mExit Utility")
print("  # \033[1;34m[ 09 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("Phishing: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd shark && shark")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd zphisher && bash zphisher.sh")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd ShellPhish && bash shellphish.sh")
elif(op==4):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd saycheese && bash saycheese.sh")
elif(op==5):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd BlackPhish && sudo python3 blackphish.py")
elif(op==6):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Castom && bash userrecon.sh")
elif(op==7):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Mask-Phish.Termux && bash Mask-Phish.sh")
elif(op==8):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
elif(op==9):
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
 
