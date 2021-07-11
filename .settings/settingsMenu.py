import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mLogo Setting - d/n")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mMenu Setting - d/n")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mVibration Setting - on/off")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mSpecial Opportunities")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mView My Activity")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mDelete My Activity")
print("  \033[1;34m[ 07 ] >> \033[1;36;40mExit System")
print("  \033[1;34m[ 08 ] >> \033[1;36;40mBack To MainMenu")

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
 os.system("cd && rm -rf AllHackingTools/.settings/deletedfiles/.zsh_history && mv .zsh_history AllHackingTools/.settings/deletedfiles/ && cd && cd AllHackingTools && python2 MainMenu.py")
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

