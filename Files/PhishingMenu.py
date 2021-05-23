import requests
from bs4 import BeautifulSoup
import os
import time
import random
import sys

print("  # \033[1;34m[ 1 ] >> \033[1;36;40mShark")
print("  # \033[1;34m[ 2 ] >> \033[1;36;40mZphisher")
print("  # \033[1;34m[ 3 ] >> \033[1;36;40mShellphish")
print("  # \033[1;34m[ 4 ] >> \033[1;36;40mExit")

op=int(raw_input("Phishing: "))

if(op==1):
 os.system("cd && cd AllHackingTools && cd shark && Shark")
elif(op==2):
 os.system("cd && cd AllHackingTools && cd zphisher && bash zphisher.sh")
elif(op==3):
 os.system("cd && cd AllHackingTools && cd ShellPhish && bash shellphish.sh")
elif(op==4):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
 
