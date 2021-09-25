import time
import sys
import os
from colorama import Fore, Back, Style
import random
import requests
from random import randint
from threading import Thread
import threading

global info
global proxy
global proxies

tor = "Not Connected"
proxy = "localhost"

def updateproxy():
	global proxy
	global info
	try:
		print("Write proxy in the format: ip:port.")
		print("Example: "+Fore.GREEN+"123.45.6.78:8080"+Style.RESET_ALL)
		proxy = input(Fore.BLUE+"Proxy > "+Style.RESET_ALL)
		if proxy == "":
			info = Fore.RED+"\nIncorect database!"+Style.RESET_ALL
			proxy = "localhost"
		else:
			print(Fore.YELLOW+"I'm checking the proxy...")
			ip = requests.get("https://flyzero.000webhostapp.com/project/ip6.php", verify=False, timeout=10).text
			try:
				ipx = requests.get("https://flyzero.000webhostapp.com/project/ip6.php", proxies={'http': "http://{}".format(proxy), 'https':"http://{}".format(proxy)}, verify=False, timeout=10).text
			except:
				ipx = ip
			if ip != ipx:
				info = Fore.GREEN+"Proxy works."+Style.RESET_ALL
			else:
				print(Fore.RED+"{} does not work. Write a new proxy!".format(proxy)+Style.RESET_ALL)
				time.sleep(2)
				os.system("clear")
				updateproxy()
	except:
		info = Fore.RED+"\nIncorect entered database"+Style.RESET_ALL
		proxy = "localhost"

def main():

	global tor
	os.system("clear")

	print ("Proxy: "+Fore.BLUE+"{}".format(proxy)+Style.RESET_ALL)
	print ("tor: "+Fore.BLUE+"{}".format(tor)+Style.RESET_ALL)
	print ("")
	print (Fore.GREEN+"1. Proxy Server"+Style.RESET_ALL)
	print (Fore.GREEN+"2. Tor Server"+Style.RESET_ALL)
	print (Fore.GREEN+"3. Quit Utility"+Style.RESET_ALL)
	diya = input(Fore.BLUE+"Options: "+Style.RESET_ALL)
	if diya == "1":
	    os.system("clear")
	    updateproxy()
	    print(Fore.GREEN+"Succesful actived!"+Style.RESET_ALL)
	    time.sleep(2)
	    main()

	elif diya == "2":
	    os.system("clear")
	    print ("Write a tor port: "+Fore.GREEN+"1-65534")
	    print ("to cancel, press: "+Fore.RED+"CTRL + C")
	    tor = input(Fore.BLUE+"Tor > "+Style.RESET_ALL)
	    if tor == "":
	            info = Fore.RED+"\nIncorect database!"+Style.RESET_ALL
	            tor = "Not Connected"
	    else:
	            print (Fore.YELLOW+"Connecting a tor server ...")
	            time.sleep(1)
	            print (Fore.YELLOW+"proxy for telegram and twitter")
	            os.system("tor --HTTPTunnelPort 8118")

	elif diya == "3":
	    print (Fore.RED+"Terminaling..."+Style.RESET_ALL)


main()
