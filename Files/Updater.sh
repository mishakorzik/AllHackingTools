g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
o="\033[1;33m"

red='\e[1;31m'
default='\e[0m'
yellow='\e[0;33m'
orange='\e[38;5;166m'
green='\033[92m'

echo -e "$yellow  ____ ___            .___                      "
echo -e "$yellow |    |   \______   __| _/____ _/  |_  ____     "
echo -e "$yellow |    |   /\____ \ / __ |\__  \\   __\/ __ \    "
echo -e "$yellow |    |  / |  |_> > /_/ | / __ \|  | \  ___/    "
echo -e "$yellow |______/  |   __/\____ |(____  /__|  \___  >   "
echo -e "$yellow           |__|        \/     \/          \/    "
echo ""
ping -c 1 google.com > /dev/null 2>&1
if [[ "$?" == 0 ]]; then
echo ""
echo -e "$green[+]-[Internet Connection]............[ True ]"
sleep 1.5
else
echo ""
echo -e "$red[-]-[Internet Connection].........[ False ]"
echo ""
sleep 99999
fi

cd
rm -rf AutoUpdateMyTools
cd 
git clone https://github.com/mishakorzik/AutoUpdateMyTools 
cd AutoUpdateMyTools
cd
cd
cd /data/data/com.termux/files/usr/share/figlet
rm -rf poison.flf
rm -rf puffy.flf
rm -rf real.flf
rm -rf pagga.tlf
rm -rf modular.tlf
rm -rf rusto.tlf
rm -rf avatar.flf
rm -rf bloody.flf
rm -rf crazy.flf
rm -rf block.flf
cd
cd
cd AutoUpdateMyTools
bash AllHackingToolupdate.sh
