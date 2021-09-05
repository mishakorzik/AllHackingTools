clear
g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
o="\033[1;33m"
printf "\e[1;92m"


cd AllHackingTools 
cd src
python3 ProgressBar.py
bash src/CheckWifi.sh
python3 Packages.py
sleep 1
clear
sleep 0.1
cd
cd
cd AllHackingTools
python3 .check/Configuration.py
