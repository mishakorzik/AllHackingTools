import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && bash src/LiteLogo.sh")

print("")
print("  \033[1;34m[ 01 ] \033[1;36;40mDefault  -  Standart installing")
print("  \033[1;34m[ 02 ] \033[1;36;40mCoded  -  Install via encoded code")
print("  \033[1;34m[ 03 ] \033[1;36;40mQuit  -  Exit and do not download")

op=int(raw_input("1nStall: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash Files/Modules.sh")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash Files/CodedModules.sh")
elif(op==3):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
else:
 print("\033[1;31;40mInvalid input. Quiting") 
 time.sleep(0.8)
