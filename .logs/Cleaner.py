# python3
import sys
import os

if sys.platform == 'win32':
        # clear in windows
        os.system('cls')
else:
        # clear in android
        os.system('clear')
