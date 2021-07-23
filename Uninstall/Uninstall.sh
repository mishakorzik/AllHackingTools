g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
o="\033[1;33m"

RED="$(printf '\033[31m')"  GREEN="$(printf '\033[32m')"  ORANGE="$(printf '\033[33m')"  BLUE="$(printf '\033[34m')"
MAGENTA="$(printf '\033[35m')"  CYAN="$(printf '\033[36m')"  WHITE="$(printf '\033[37m')" BLACK="$(printf '\033[30m')"
REDBG="$(printf '\033[41m')"  GREENBG="$(printf '\033[42m')"  ORANGEBG="$(printf '\033[43m')"  BLUEBG="$(printf '\033[44m')"
MAGENTABG="$(printf '\033[45m')"  CYANBG="$(printf '\033[46m')"  WHITEBG="$(printf '\033[47m')" BLACKBG="$(printf '\033[40m')"
DEFAULT_FG="$(printf '\033[39m')"  DEFAULT_BG="$(printf '\033[49m')" YELLOW="$(printf '\e[0;33m')"

red='\e[1;31m'
default='\e[0m'
yellow='\e[0;33m'
orange='\e[38;5;166m'
green='\033[92m'

echo "${YELLOW}  ____ ___      .__                 __         .__  .__     "
echo "${YELLOW} |    |   \____ |__| ____   _______/  |______  |  | |  |    "
echo "${YELLOW} |    |   /    \|  |/    \ /  ___/\   __\__  \ |  | |  |    "
echo "${YELLOW} |    |  /   |  \  |   |  \\___ \   |  |  / __ \|  |_|  |__ "
echo "${YELLOW} |______/|___|  /__|___|  /____  > |__| (____  /____/____/  "
echo "${YELLOW}              \/        \/     \/            \/             "
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
