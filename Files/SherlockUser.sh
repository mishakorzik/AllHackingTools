g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"

clear
cd
cd AllHackingTools
bash Logo.sh
cd sherlock
echo ""
echo -e $b">>>"$w" Write the UserName: "$g"Sherlock"$w
read NameOrUser
sleep 0.1
echo -e $b">>>"$w" Please wait a moment: "$g"Sherlock"$w
sleep 0.8
clear
python3 sherlock $NameOrUser
cd
cd
cd AllHackingTools
python3 src/Timer2.py
