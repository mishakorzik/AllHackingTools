red='\e[1;31m'
default='\e[0m'
yellow='\e[0;33m'
orange='\e[38;5;166m'
green='\033[92m'

ping -c 1 google.com > /dev/null 2>&1
sleep 2
if [[ "$?" == 0 ]]; then
echo -e "$green[+]-[Internet Connection]............[ True ]"
sleep 1.5
else
echo -e "$red[-]-[Internet Connection].........[ False ]"
echo ""
exit
exit
fi

