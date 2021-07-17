# python3
import sys
import os

if sys.platform == 'win32':
        # clear in windows, java
        os.system('cls')
else:
        # clear in linux, android, ubuntu
        os.system('clear')
