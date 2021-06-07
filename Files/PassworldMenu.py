import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  # \033[1;34m[ 1 ] >> \033[1;36;40mHasher - Hash cracker with auto detect hash")
print("  # \033[1;34m[ 2 ] >> \033[1;36;40mHasherDoid - A tool for find an encrypted text")
print("  # \033[1;34m[ 3 ] >> \033[1;36;40mHash Generator - Beautiful Hash Generator")
print("  # \033[1;34m[ 4 ] >> \033[1;36;40mHash Buster - Crack hashes in seconds")
print("  # \033[1;34m[ 5 ] >> \033[1;36;40mExit Utility")
print("  # \033[1;34m[ 6 ] >> \033[1;36;40mBack To MainMenu")

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
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
