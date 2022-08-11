g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"

clear
cd
cd AllHackingTools
bash Logo.sh
cd Files
echo ""
echo -e $b">>>"$w" Write the Ip Address: "$g"IpHack"$w
read victimIP
sleep 0.1
echo -e $b">>>"$w" Please wait a moment: "$g"IpHack"$w
sleep 0.6
python IpHack.py -t $victimIP
cd
cd
cd AllHackingTools
