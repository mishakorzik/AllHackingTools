import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mDesing Logo 1")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mDesing Logo 2")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mDesing Logo 3")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mExit System")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("Sett1Ngs: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && mv Logo.sh /data/data/com.termux/files/home/AllHackingTools/.temp/DesingTemp/ && cd && cd AllHackingTools && cd .settings && cd desing && mv Logo.sh /data/data/com.termux/files/home/AllHackingTools/ && cd && cd AllHackingTools && cd .temp && cd DesingTemp && mv Logo.sh /data/data/com.termux/files/home/AllHackingTools/.settings/desing/ && cd && cd AllHackingTools && bash .settings/Applined.sh")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && mv Logo.sh /data/data/com.termux/files/home/AllHackingTools/.temp/ && cd && cd AllHackingTools && cd .settings && mv Logo.sh /data/data/com.termux/files/home/AllHackingTools/ && cd && cd AllHackingTools && cd .temp && mv Logo.sh /data/data/com.termux/files/home/AllHackingTools/.settings/ && cd && cd AllHackingTools && bash .settings/Applined.sh")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && mv Logo.sh /data/data/com.termux/files/home/AllHackingTools/.temp/DesingTemp2/ && cd && cd AllHackingTools && cd .settings && cd desing2 && mv Logo.sh /data/data/com.termux/files/home/AllHackingTools/ && cd && cd AllHackingTools && cd .temp && cd DesingTemp2 && mv Logo.sh /data/data/com.termux/files/home/AllHackingTools/.settings/desing2/ && cd && cd AllHackingTools && bash .settings/Applined.sh")
elif(op==4):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting System...")
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
 os.system("python2 MainMenu.py")
