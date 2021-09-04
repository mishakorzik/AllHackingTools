import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")
os.system("cd && cd AllHackingTools && bash .desing/desing/SpecialMenu2.sh")

op=int(raw_input("Sett1Ngs: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd .check && mv CheckServerYesAndNo.py /data/data/com.termux/files/home/AllHackingTools/.temp/ && cd && cd AllHackingTools && cd .settings && mv CheckServerYesAndNo.py /data/data/com.termux/files/home/AllHackingTools/.check/ && cd && cd AllHackingTools && cd .temp && mv CheckServerYesAndNo.py /data/data/com.termux/files/home/AllHackingTools/.settings/ && cd && cd AllHackingTools && bash .settings/Applined.sh")
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
