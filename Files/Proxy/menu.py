import requests
import os
import time
import random
from bs4 import BeautifulSoup
import sys

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
Purple="\033[0;35m"

color1=["\033[1;34m","\033[1;34m","\033[1;34m","\033[1;34m","\033[1;34m","\033[1;34m"]
def color():
 return str(random.choice(color1))
def generate(url,count):
 try:
  r=requests.get(url)
  soup=BeautifulSoup(r.content,'html.parser')
  list = soup.find(class_='table table-striped table-bordered')
  list1 = list.findAll('td')
  iplist=[]
  portlist=[]
  codelist=[]
  countrylist=[]
  anonymitylist=[]
  googlelist=[]
  httpslist=[]
  last_checklist=[]
  finallist=[]
  j=0
  while(j<(8*count)):
   a=str(list1[j].contents[0])
   iplist.append(a)
   j=j+8
  j=1
  while(j<(8*count)):
   a=str(list1[j].contents[0])
   portlist.append(a)
   j=j+8
  j=2   
  while(j<(8*count)):
   a=str(list1[j].contents[0])
   codelist.append(a)
   j=j+8   
  j=3   
  while(j<(8*count)):
   a=str(list1[j].contents[0])
   countrylist.append(a)
   j=j+8 
  j=4   
  while(j<(8*count)):
   a=str(list1[j].contents[0])
   anonymitylist.append(a)
   j=j+8
  j=5   
  while(j<(8*count)):
   a=str(list1[j].contents[0])
   googlelist.append(a)
   j=j+8  
  j=6   
  while(j<(8*count)):
   a=str(list1[j].contents[0])
   httpslist.append(a)
   j=j+8  
  j=7   
  while(j<(8*count)):
   a=str(list1[j].contents[0])
   last_checklist.append(a)
   j=j+8
  for k in range (0,count):
      print(color()+iplist[k]+":"+color()+portlist[k]+"\t"+color()+codelist[k]+"\t"+color()+countrylist[k]+"\t\t"+color()+anonymitylist[k]+color()+"\tGoogle:"+googlelist[k]+color()+"\thttps:"+httpslist[k]+color()+"\tLast checked "+last_checklist[k]+"\n")
 except:
  print("\033[1;31;40m%d Proxies can't be generated at this time. Try giving a smaller amount(i.e 1) or try again after some time."%count)
def socks(count):
 try:
  r=requests.get("https://www.socks-proxy.net")
  soup=BeautifulSoup(r.content,'html.parser')
  list = soup.find(class_='table table-striped table-bordered')
  list1 = list.findAll('td')
  iplist=[]
  portlist=[]
  codelist=[]
  countrylist=[]
  versionlist=[]
  anonymitylist=[]
  httpslist=[]
  last_checklist=[]
  j=0
  while(j<8*count):
   a=str((list1[j].contents[0]))
   iplist.append(a)
   j=j+8
  j=1
  while(j<8*count):
   a=str((list1[j].contents[0]))
   portlist.append(a)
   j=j+8
  j=2
  while(j<8*count):
   a=str((list1[j].contents[0]))
   codelist.append(a)
   j=j+8
  j=3
  while(j<8*count):
   a=str((list1[j].contents[0]))
   countrylist.append(a)
   j=j+8
  j=4
  while(j<8*count):
   a=str((list1[j].contents[0]))
   versionlist.append(a)
   j=j+8
  j=5
  while(j<8*count):
   a=str((list1[j].contents[0]))
   anonymitylist.append(a)
   j=j+8
  j=6
  while(j<8*count):
   a=str((list1[j].contents[0]))
   httpslist.append(a)
   j=j+8
  j=7
  while(j<8*count):
   a=str((list1[j].contents[0]))
   last_checklist.append(a)
   j=j+8

  for k in range (0,count):
   print(color()+iplist[k]+":"+color()+portlist[k]+"\t"+color()+codelist[k]+"\t"+color()+countrylist[k]+"\t"+color()+versionlist[k]+"\t"+color()+anonymitylist[k]+"\thttps:"+color()+httpslist[k]+"\tLast Checked :"+color()+last_checklist[k]+"\n")
 except:
  print("\033[1;31;40m%d Proxies can't be generated at this time. Try giving a smaller amount(i.e 1) or try again after some time."%count)

print("  # \033[1;34m[ 1 ] >> \033[1;36;40mALL PROXY")
print("  # \033[1;34m[ 2 ] >> \033[1;36;40mUS PROXY")
print("  # \033[1;34m[ 3 ] >> \033[1;36;40mUK PROXY")
print("  # \033[1;34m[ 4 ] >> \033[1;36;40mSSL PROXY")
print("  # \033[1;34m[ 5 ] >> \033[1;36;40mANONYMOUS PROXY")
print("  # \033[1;34m[ 6 ] >> \033[1;36;40mSOCKS PROXY")
print("  # \033[1;34m[ 7 ] >> \033[1;36;40mUPDATE UTILITY")
print("  # \033[1;34m[ 8 ] >> \033[1;36;40mEXIT UTILITY")

op=int(raw_input("Options: "))

if(op==1):
 proxyDomain = "https://free-proxy-list.net" 

 system = requests.get(proxyDomain)
 
 mranonymous_systemSoup = BeautifulSoup(system.content,'html.parser')

 sosBlackhats = mranonymous_systemSoup.find('table',{"id" : "proxylisttable"})
 for row in sosBlackhats.find_all('tr'):
    columns = row.find_all('td')
    try:
        print "%s:%s\t%-20s\t%-10s"  % (columns[0].get_text(),columns[1].get_text(),columns[3].get_text(),columns[4].get_text())
    except:
        pass
elif(op==2):
 generate("https://us-proxy.org",65) 
elif(op==3):
 generate("https://free-proxy-list.net/uk-proxy.html",65)
elif(op==4):
 generate("https://www.sslproxies.org",65)
elif(op==5):
 generate("https://free-proxy-list.net/anonymous-proxy.html",65)
elif(op==6):
 socks(85)
 print " "+Blue+"177.206.186.9:8080   SOCKS4   Brazil   Elite"
 print " "+Blue+"51.81.31.62:54860   SOCKS5  Francia    hing anonymous"
elif(op==7):
 print("Updating tool. Please wait a moment")
 os.system("cd src")
 os.system("bash ProxyUpdater.sh")
elif(op==8):
 print("\033[1;31;40mQuiting Utility...")
 time.sleep(0.8)
 sys.exit()
else:
 print("\033[1;31;40mInvalid input. Quiting...")
 time.sleep(1.5)
 sys.exit()
