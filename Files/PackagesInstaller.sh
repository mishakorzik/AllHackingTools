red='\e[1;31m'
default='\e[0m'
yellow='\e[0;33m'
orange='\e[38;5;166m'
green='\033[92m'

clear
sleep 1
echo -e "$yellow  ___                 __         .__  .__                 "
echo -e "$yellow |   | ____   _______/  |______  |  | |  |   ___________  "    
echo -e "$yellow |   |/    \ /  ___/\   __\__  \ |  | |  | _/ __ \_  __ \ "    
echo -e "$yellow |   |   |  \___  \  |  |  / __ \|  |_|  |_\  ___/|  | \/ "    
echo -e "$yellow |___|___|  /____  > |__| (____  /____/____/\___  >__|    "
echo -e "$yellow          \/     \/            \/               \/        "
echo ""
echo -e "$yellow   Tool Name: AllHackingTools "
echo -e "$yellow   Developer: Misha Korzhik " 

which git > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Git].............................[ SUCCESFUL ]"
sleep 1.5
else
echo -e "$red[-]-[Git]..........................[ FAILED ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Git...]"
apt install git 
fi

which python > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Python]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo -e "$red[-]-[Python].......................[ FAILED ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Python...]"
apt install python > /dev/null
apt install python
apt install python2
apt install python3
pkg install pip
pkg install pip2
pip2 install --upgrade pip
fi

which wget > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Wget]............................[ SUCCESFUL ]"
sleep 1.5
else
echo -e "$red[-]-[Wget].........................[ FAILED ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Wget...]"
apt install wget
fi

which jq > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Jq]..............................[ SUCCESFUL ]"
sleep 1.5
else
echo -e "$red[-]-[Jq]...........................[ FAILED ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Jq...]"
apt install python
fi

which ruby > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Ruby]............................[ SUCCESFUL ]"
sleep 1.5
else
echo -e "$red[-]-[Ruby].........................[ FAILED ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Ruby...]"
apt install ruby 
fi

which toilet > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Toilet]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo -e "$red[-]-[Toilet].......................[ FAILED ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Toilet...]"
apt install toilet 
fi

which figlet > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Figlet]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo -e "$red[-]-[Figlet].......................[ FAILED ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Figlet...]"
apt install figlet 
fi

which lolcat > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Lolcat]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo -e "$red[-]-[Lolcat].......................[ FAILED ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Lolcat...]"
gem install lolcat
fi

which neofetch > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Neofetch]........................[ SUCCESFUL ]"
sleep 1.5
else
echo -e "$red[-]-[Neofetch].....................[ FAILED ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Neofetch...]"
apt install neofetch
fi

which php > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[PHP].............................[ SUCCESFUL ]"
sleep 1.5
else
echo -e "$red[-]-[PHP]..........................[ FAILED ]"
sleep 1.5
echo -e "$yellow[!][Installing Module PHP...]"
apt install php
fi

which ruby > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Clang]...........................[ SUCCESFUL ]"
sleep 1.5
else
echo -e "$red[-]-[Clang]........................[ FAILED ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Clang...]"
apt install clang
fi

which zip > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Zip].............................[ SUCCESFUL ]"
sleep 1.5
else
echo -e "$red[-]-[Zip]..........................[ FAILED ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Zip...]"
apt install zip
fi

which pip > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[PIP].............................[ SUCCESFUL ]"
sleep 1.5
else
echo -e "$red[-]-[PIP]..........................[ FAILED ]"
sleep 1.5
echo -e "$yellow[!][Installing Module pip...]"
apt install pip
pkg install pip
pkg install pip2
apt install pip
apt install pip2
pip2 install --upgrade pip
fi

which zsh > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[zsh].............................[ SUCCESFUL ]"
sleep 1.5
else
echo -e "$red[-]-[zsh]..........................[ FAILED ]"
sleep 1.5
echo -e "$yellow[!][Installing Module zsh...]"
apt install zsh 
fi

which pv > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[pv]..............................[ SUCCESFUL ]"
sleep 1.5
else
echo -e "$red[-]-[pv]...........................[ FAILED ]"
sleep 1.5
echo -e "$yellow[!][Installing Module pv...]"
apt install pv
fi

which curl > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Curl]............................[ SUCCESFUL ]"
sleep 1.5
else
echo -e "$red[-]-[Curl].........................[ FAILED ]"
sleep 1.5
echo -e "$yellow[!]-[Installing Module Curl...]"
apt install curl 
fi

which w3m > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[w3m].............................[ SUCCESFUL ]"
sleep 1.5
else
echo -e "$red[-]-[w3m]..........................[ FAILED ]"
sleep 1.5
echo -e "$yellow[!]-[Installing Module w3m...]"
apt install w3m 
fi

red='\e[1;31m'
default='\e[0m'
yellow='\e[0;33m'
orange='\e[38;5;166m'
green='\033[92m'

if [ -f "ngrok" ]; then
echo -e "$green[+]-[Ngrok].............................[ FOUND ]"
sleep 1.5
else
echo -e "$red[-]-[Ngrok]........................[ NOT FOUND ]"
sleep 0.2
echo -e "$yellow[!]-[Downloading:Ngrok.............[ INSTALLING ]"
sleep 1.2
cd 
cd
cd AllHackingTools
cd Castom
cp ngrok /data/data/com.termux/files/home/
cd
cd
chmod +x ngrok
sleep 2
echo -e "$yellow[+]-[Ngrok Installed!..............[ INSTALLED ]"
sleep 1.5
fi

echo -e $yellow
echo -n [!] Installing Depencies...= ;
sleep 3 & while [ "$(ps a | awk '{print $1}' | grep $!)" ] ; do for X in '-' '\' '|' '/'; do echo -en "\b$X"; sleep 0.1; done; done 
echo ""

apt install apache2
apt install Apache2
apt install openssl -y
apt install python-dev -y
apt install python3 -y
apt-get install pip2
pip install --upgrade pip2
apt-get install termux-api
pkg install termux-api
pip2 install --upgrade pip
pip2 install passlib
pip install passlib
pip2 install progressbar
pip install progressbar
pip2 install future
pip install future
pip2 install colorama
pip install flask
pip2 install flask_socketio
pip install flask_socketio
pip3 install flask_socketio
pip3 install flask_cors
pip2 install flask_cors
pip2 install mechanize
