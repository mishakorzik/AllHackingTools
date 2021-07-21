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

echo -e "$yellow  ____ ___      .__                 __         .__  .__     "
echo -e "$yellow |    |   \____ |__| ____   _______/  |______  |  | |  |    "
echo -e "$yellow |    |   /    \|  |/    \ /  ___/\   __\__  \ |  | |  |    "
echo -e "$yellow |    |  /   |  \  |   |  \\___ \   |  |  / __ \|  |_|  |__ "
echo -e "$yellow |______/|___|  /__|___|  /____  > |__| (____  /____/____/  "
echo -e "$yellow              \/        \/     \/            \/             "
echo ""
echo -e $w"["$o"SYSTEM"$w"]"$w" Press enter to uninstall AllHackingTools"$w
read a1
echo -e $w"["$o"SYSTEM"$w"]"$w" Uninstalling AllHackingTools. Please wait a moment!"$w
sleep 0.8
ping -c 1 google.com > /dev/null 2>&1
if [[ "$?" == 0 ]]; then
echo -e "$green[+]-[Internet Connection]............[ true ]"
sleep 1.5
else
echo -e "$red[-]-[Internet Connection].........[ False ]"
echo ""
sleep 9999
fi

sleep 2.8
cd
cd
cd AllHackingTools
cd termux-style
./uninstall
cd
cd 
rm -rf AutoUpdateMyTools
git clone https://github.com/mishakorzik/AutoUpdateMyTools
cd
cd
cd .termux
rm -rf termux.properties
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
Rootkite-delete-qiq
cd
cd
cd AutoUpdateMyTools
bash Files/UninstallAllHackingTools.sh
