g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"

clear
cd
cd AllHackingTools
bash Logo.sh
cd XanXSS
echo ""
echo -e $b">>>"$w" Write the site address: "$g"XanXSS"$w
read siteURL2
sleep 0.1
echo -e $b">>>"$w" Please wait a moment: "$g"XanXSS"$w
sleep 0.6
python3 xanxss.py -u $siteURL2
cd
cd
cd AllHackingTools
