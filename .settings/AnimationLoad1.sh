clear
g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
o="\033[1;33m"
printf "\e[1;92m"

cd
cd
cd AllHackingTools 
cd src
termux-vibrate -d 200
python3 ProgressBar.py
python3 Packages.py
termux-vibrate -d 300

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
python3 .check/Configuration.py
