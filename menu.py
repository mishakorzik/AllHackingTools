import requests
from bs4 import BeautifulSoup
import os
import time
import random
import sys

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
Purple="\033[0;35m"

print("  # \033[1;34m[ 1 ] >> \033[1;36;40mDefault")
print("  # \033[1;34m[ 2 ] >> \033[1;36;40mIMPORT")
print("  # \033[1;34m[ 3 ] >> \033[1;36;40mEXIT")

op=int(raw_input("Options: "))

if(op==1):
 bash Default.sh
elif(op==2):
 bash Import.sh
elif(op==3):
 print("\033[1;31;40mQuiting utility...")
 time.sleep(1)
 sys.exit()
else:
 print("\033[1;31;40mInvalid input. Quiting...")
 time.sleep(1)
 sys.exit()

