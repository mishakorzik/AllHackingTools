g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"

clear
cd
cd AllHackingTools
bash Logo.sh
cd XSSCon
echo ""
echo -e $b">>>"$w" Write the site address: "$g"XSScon"$w
read siteURL1
sleep 0.1
echo -e $b">>>"$w" Please wait a moment: "$g"XSScon"$w
sleep 0.6
python3 xsscon.py -u $siteURL1 -v
cd
cd
cd AllHackingTools
