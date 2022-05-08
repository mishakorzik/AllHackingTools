g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"

clear
cd
cd AllHackingTools
clear
python2 ismtp.py
echo "Please enter all your required settings to run the program."
echo -e $b">>>"$w"Console/> "$g"iSMTP"$w
read opt
sleep 0.1
python2 ismtp.py $opt
cd
cd
cd AllHackingTools
