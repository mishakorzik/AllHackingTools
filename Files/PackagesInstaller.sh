red='\e[1;31m'
default='\e[0m'
yellow='\e[0;33m'
orange='\e[38;5;166m'
green='\033[92m'

which git > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo ""
echo -e "$green[+]-[Git]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo ""
echo -e "$red[-]-[Git].......................[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Git...]"
apt install git > /dev/null
fi

which python > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo ""
echo -e "$green[+]-[Python]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo ""
echo -e "$red[-]-[Python].......................[ NOT FOUND ]"
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
echo ""
echo -e "$green[+]-[Wget]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo ""
echo -e "$red[-]-[Wget].......................[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Wget...]"
apt install wget > /dev/null
fi

which jq > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo ""
echo -e "$green[+]-[Jq]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo ""
echo -e "$red[-]-[Jq].......................[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Jq...]"
apt install python > /dev/null
fi

which ruby > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo ""
echo -e "$green[+]-[Ruby]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo ""
echo -e "$red[-]-[Ruby].......................[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Ruby...]"
apt install ruby > /dev/null
fi

which toilet > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo ""
echo -e "$green[+]-[Toilet]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo ""
echo -e "$red[-]-[Toilet].......................[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Toilet...]"
apt install toilet > /dev/null
fi

which figlet > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo ""
echo -e "$green[+]-[Figlet]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo ""
echo -e "$red[-]-[Figlet].......................[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Figlet...]"
apt install figlet > /dev/null
fi

which lolcat > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo ""
echo -e "$green[+]-[Lolcat]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo ""
echo -e "$red[-]-[Lolcat].......................[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Lolcat...]"
gem install lolcat > /dev/null
fi

which neofetch > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo ""
echo -e "$green[+]-[Neofetch]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo ""
echo -e "$red[-]-[Neofetch].......................[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Neofetch...]"
apt install neofetch > /dev/null
fi

which php > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo ""
echo -e "$green[+]-[PHP]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo ""
echo -e "$red[-]-[PHP].......................[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Installing Module PHP...]"
apt install php > /dev/null
fi

which apache2 > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo ""
echo -e "$green[+]-[Apache2]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo ""
echo -e "$red[-]-[Apache2].......................[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Apache2...]"
apt install apache2 > /dev/null
fi

which ruby > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo ""
echo -e "$green[+]-[Clang]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo ""
echo -e "$red[-]-[Clang].......................[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Clang...]"
apt install clang > /dev/null
fi

which zip > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo ""
echo -e "$green[+]-[Zip]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo ""
echo -e "$red[-]-[Zip].......................[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Zip...]"
apt install zip > /dev/null
fi

which pip > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo ""
echo -e "$green[+]-[PIP]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo ""
echo -e "$red[-]-[PIP].......................[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Installing Module pip...]"
apt install pip > /dev/null
pkg install pip
pkg install pip2
apt install pip
apt install pip2
pip2 install --upgrade pip
fi

which zsh > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo ""
echo -e "$green[+]-[zsh]............................[ SUCCESFUL ]"
sleep 1.5
else
echo ""
echo -e "$red[-]-[zsh].........................[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Installing Module zsh...]"
apt install zsh > /dev/null
fi

which pv > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo ""
echo -e "$green[+]-[pv].............................[ SUCCESFUL ]"
sleep 1.5
else
echo ""
echo -e "$red[-]-[pv]..........................[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Installing Module pv...]"
apt install pv > /dev/null
fi

which curl > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo ""
echo -e "$green[+]-[Curl]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo ""
echo -e "$red[-]-[Curl].......................[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!]-[Installing Module Curl...]"
apt install curl > /dev/null
fi

exit
