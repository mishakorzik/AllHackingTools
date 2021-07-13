import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mQuick Start - on/off")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mServers Setting")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mNew ExtraKeys0")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mNew ExtraKeys1")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mAdd AllHackingTool to startup")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mView MySystem Process - ProcessExplorer")
print("  \033[1;34m[ 07 ] >> \033[1;36;40mExit System - log out AllHackingTool")
print("  \033[1;34m[ 08 ] >> \033[1;36;40mBack To MainMenu - go to the home menu")

op=int(raw_input("Sett1Ngs: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd src && mv AllHackingTool.sh /data/data/com.termux/files/home/AllHackingTools/.temp/ && cd && cd AllHackingTools && cd .settings && mv AllHackingTool.sh /data/data/com.termux/files/home/AllHackingTools/src/ && cd && cd AllHackingTools && cd .temp && mv AllHackingTool.sh /data/data/com.termux/files/home/AllHackingTools/.settings/ && cd && cd AllHackingTools && bash .settings/Applined.sh")
elif(op==2):
 os.system("clear")
 print("\033[1;31;40mNot Found! You have no rights....")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Termux-os && bash TermuxNewKeys2.sh && cd && cd AllHackingTools && bash .settings/Applined.sh")
elif(op==4):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Termux-os && bash TermuxNewKeys.sh && cd && cd AllHackingTools && bash .settings/Applined.sh")
elif(op==5):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd .settings && bash StartAllHackingToolsAndTerminal.sh && cd && cd AllHackingTools && bash .settings/Applined.sh")
elif(op==6):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash src/ProcessExplorer.sh")
elif(op==7):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting System...")
 sys.exit()
elif(op==8):
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 MainMenu.py")
