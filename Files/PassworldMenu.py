import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  # \033[1;34m[ 01 ] >> \033[1;36;40mHasher - Hash cracker with auto detect hash")
print("  # \033[1;34m[ 02 ] >> \033[1;36;40mHasherDoid - A tool for find an encrypted text")
print("  # \033[1;34m[ 03 ] >> \033[1;36;40mHash Generator - Beautiful Hash Generator")
print("  # \033[1;34m[ 04 ] >> \033[1;36;40mHash Buster - Crack hashes in seconds")
print("  # \033[1;34m[ 05 ] >> \033[1;36;40mExit Utility")
print("  # \033[1;34m[ 06 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("Ma1lHacK: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd hasher && python2 hash.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd hasherdoid && python2 hasherdotid.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd hash-generator && python2 hashgen.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Hash-Buster && python3 hash.py")
elif(op==5):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
elif(op==6):
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 Files/PassworldMenu.py")
