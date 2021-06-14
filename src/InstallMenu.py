import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && bash src/LiteLogo.sh")

print("  \033[1;34mChoice installing options:")
print("")
print("  \033[1;34m[ 01 ] \033[1;36;40mDefault")
print("  \033[1;34m[ 02 ] \033[1;36;40mCoded")
print("  \033[1;34m[ 03 ] \033[1;36;40mQuit")

op=int(raw_input("Ma1lHacK: "))

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
 time.sleep(1.6)
