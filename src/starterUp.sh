red='\e[1;31m'
default='\e[0m'
yellow='\e[0;33m'
orange='\e[38;5;166m'
green='\033[92m'
g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
o="\033[1;33m"
printf "\e[1;92m"

python3 ProgressBar.py
python3 Packages.py

ping -c 1 google.com > /dev/null 2>&1
if [[ "$?" == 0 ]]; then
echo -e "$g[+]-[wifi]———[ True ]"
else
echo -e "$r[-]-[wifi]——[ False ]"
echo -e "$rType: CTRL + C to exit"
exit
sleep 9999999
sleep 9999999
sleep 9999999
exit
fi

sleep 2
clear
cd
cd
cd AllHackingTools
mv MainMenu.py /data/data/com.termux/files/home/AllHackingTools/Tool
clear
python3 .check/Configuration.py
