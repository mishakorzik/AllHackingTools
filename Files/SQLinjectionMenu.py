import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  # \033[1;34m[ 01 ] >> \033[1;36;40mVirusInjection - create a virus in /sdcard/")
print("  # \033[1;34m[ 02 ] >> \033[1;36;40mDebinject - Inject malicious code into *.debs")
print("  # \033[1;34m[ 03 ] >> \033[1;36;40mZvirus - Create a virus for windows, android, linux")
print("  # \033[1;34m[ 04 ] >> \033[1;36;40mExit Utility")
print("  # \033[1;34m[ 05 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("Iject1onTo0l: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Vitus2.0 && cp VirtualXposed.apk /sdcard/")
 print("Your virus has been created!")
 time.sleep(1)
 print("Find Your virus in /sdcard/")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Debinject && python2 debinject.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd zVirus-Gen && bash zVirus")
elif(op==4):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
elif(op==5):
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 Files/SQLinjectionMenu.py")
