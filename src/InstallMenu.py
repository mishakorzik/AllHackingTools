import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && bash src/LiteLogo.sh")

print("")
print("  \033[1;34m[01] \033[1;36;40mDefault  -  Standart installing and default")
print("  \033[1;34m[02] \033[1;36;40mRestore  -  Restore AllHackingTools in backup")
print("  \033[1;34m[03] \033[1;36;40mCoded  -  Install via encoded code NOT RECOMMENDED")
print("  \033[1;34m[04] \033[1;36;40mQuit  -  Exit and do not download AllHackingTools")

op=int(raw_input("1nStall: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash Files/Modules.sh")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash src/LiteLogo.sh")
 os.system("cd && rm -rf AutoUpdateMyTools && git clone https://github.com/mishakorzik/AutoUpdateMyTools")
 os.system("bash AutoUpdateMyTools/Files/RestoreAllHackingToolBackup.sh")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash Files/CodedModules.sh")
elif(op==4):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting AllHackingTool Installer...")
 sys.exit()
else:
 print("\033[1;31;40mInvalid input. Quiting AllHackingTools Installer") 
 time.sleep(0.8)
