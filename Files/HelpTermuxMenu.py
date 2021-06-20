import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mFiles and base commands")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mProcess controlers commands")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mAccess rights and files commands")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mSystem Information commands ")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mPackages and working commads")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mSearch commands")
print("  \033[1;34m[ 07 ] >> \033[1;36;40mArchive commands")
print("  \033[1;34m[ 08 ] >> \033[1;36;40mNetwork commands")
print("  \033[1;34m[ 09 ] >> \033[1;36;40mExit System")
print("  \033[1;34m[ 10 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("1nf0rmatI0nHe1p: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash Help/FilesAndBaseCommads.sh")
 os.system("cd && cd AllHackingTools && python3 src/Timer1.py && python2 src/aboutMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash Help/ProcessControlerCommands.sh")
 os.system("cd && cd AllHackingTools && python3 src/Timer1.py && python2 src/aboutMenu.py")
elif(op==6):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash Help/SearchCommand.sh")
 os.system("cd && cd AllHackingTools && python3 src/Timer1.py && python2 src/aboutMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash Help/AccesRightAndFilesCommands.sh")
 os.system("cd && cd AllHackingTools && python3 src/Timer1.py && python2 src/aboutMenu.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash Help/SystemInformationCommands.sh")
 os.system("cd && cd AllHackingTools && python3 src/Timer1.py && python2 src/aboutMenu.py")
elif(op==5):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash Help/InstallingPackagesAndWorkingCommands.sh")
 os.system("cd && cd AllHackingTools && python3 src/Timer1.py && python2 src/aboutMenu.py")
elif(op==7):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash Help/ArchiveFilesCommands.sh")
 os.system("cd && cd AllHackingTools && python3 src/Timer1.py && python2 src/aboutMenu.py")
elif(op==8):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash Help/NetworkComands.sh")
 os.system("cd && cd AllHackingTools && python3 src/Timer1.py && python2 src/aboutMenu.py")
elif(op==9):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
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
 os.system("python2 Files/HelpTermuxMenu.py")

