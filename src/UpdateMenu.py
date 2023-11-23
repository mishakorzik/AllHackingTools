import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && bash src/LiteLogo.sh")

print("")
print("  \033[1;34m[01] \033[1;36;40mDefault Installing  -  Standart installing RECOMMEND")
print("  \033[1;34m[02] \033[1;36;40mSpeed Installing  -  Very fast download NOT RECOMMEND")
print("  \033[1;34m[03] \033[1;36;40mQuit Updater  -  Exit and do not update AllHackingTools")

op=int(raw_input("UPda1Er: "))

if(op==1):
 os.system("clear")
 os.system("cd && rm -rf AutoUpdateMyTools && cd && git clone https://github.com/mishakorzik/AutoUpdateMyTools && cd AutoUpdateMyTools && cd")
 os.system("cd /data/data/com.termux/files/usr/share/figlet && rm -rf poison.flf && rm -rf puffy.flf && rm -rf real.flf && rm -rf pagga.tlf && rm -rf modular.tlf && rm -rf rusto.tlf && rm -rf avatar.flf && rm -rf bloody.flf && rm -rf crazy.flf && rm -rf block.flf && cd && cd AutoUpdateMyTools && bash AllHackingToolupdate.sh")
elif(op==2):
 os.system("cd && cd AllHackingTools && cd src && bash SpeedUpdate.sh")
elif(op==3):
 time.sleep(0.2)
 print("\033[1;31;40mQuitting TarkDOXX Updater...")
 sys.exit()
else:
 print("\033[1;31;40mInvalid input. Quitting TarkDOXX Updater") 
 time.sleep(0.8)
