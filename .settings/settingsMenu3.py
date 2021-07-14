import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")
os.system("cd && bash AllHackingTools/.desing/SettingMenu3.sh")

op=int(raw_input("Sett1Ngs: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd .settings && python2 DesingLogo.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd .settings && python2 DesingMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd src && mv AnimationLoad1.sh /data/data/com.termux/files/home/AllHackingTools/.temp/ && cd && cd AllHackingTools && cd .settings && mv AnimationLoad1.sh /data/data/com.termux/files/home/AllHackingTools/src/ && cd && cd AllHackingTools && cd .temp && mv AnimationLoad1.sh /data/data/com.termux/files/home/AllHackingTools/.settings/ && cd && cd AllHackingTools && bash .settings/Applined.sh")
elif(op==4):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd .settings && python2 SpecialOpportunities.py")
elif(op==5):
 os.system("clear")
 os.system("cd && nano .zsh_history")
elif(op==6):
 os.system("clear")
 os.system("cd && rm -rf AllHackingTools/.settings/deletedfiles/.zsh_history && cd && mv .zsh_history AllHackingTools/.settings/deletedfiles/ && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==7):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash Logo.sh")
 time.sleep(0.2)
 print("\033[1;31;40mRestoring AllHackingTools backup...")
 os.system("cd /sdcard/ && cp -r AllHackingTools /data/data/com.termux/files/home/")
 os.system("cd && bash AllHackingTools/.settings/RestoreAllHackingToolsBackup.sh")
 print("successfully restored backup in: sdcard...")
elif(op==8):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash Logo.sh")
 time.sleep(0.2)
 print("\033[1;31;40mWait A Bit For The Backup To Be Created...")
 os.system("cd && cd && cp -r AllHackingTools /sdcard/")
 print("successfully created a backup in: sdcard...")
elif(op==9):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting System...")
 sys.exit()
elif(op==10):
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 MainMenu.py")

