import requests
import os
import time
import random
import sys

print(" \033[1;34m[1] \033[1;36;40mInstall module")
print(" \033[1;34m[2] \033[1;36;40mReinstall module")
print(" \033[1;34m[3] \033[1;36;40mRemove module")

op=int(raw_input("qip: "))

if(op==1):
 os.system("cd && cd /data/data/com.termux/files/usr/bin/packQIP/ && bash InstallModuleqip62491.sh")
elif(op==2):
 os.system("cd && cd /data/data/com.termux/files/usr/bin/packQIP/ && bash ReinstallModuleqip62491.sh")
elif(op==3):
 os.system("cd && cd /data/data/com.termux/files/usr/bin/packQIP/ && bash RemoveModuleqip62491.sh")
else:
 time.sleep(0.2)
 os.system("echo qip stopped!")
