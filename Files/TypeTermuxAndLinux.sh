RED="$(printf '\033[31m')"  GREEN="$(printf '\033[32m')"  ORANGE="$(printf '\033[33m')"  BLUE="$(printf '\033[34m')"
MAGENTA="$(printf '\033[35m')"  CYAN="$(printf '\033[36m')"  WHITE="$(printf '\033[37m')" BLACK="$(printf '\033[30m')"
REDBG="$(printf '\033[41m')"  GREENBG="$(printf '\033[42m')"  ORANGEBG="$(printf '\033[43m')"  BLUEBG="$(printf '\033[44m')"
MAGENTABG="$(printf '\033[45m')"  CYANBG="$(printf '\033[46m')"  WHITEBG="$(printf '\033[47m')" BLACKBG="$(printf '\033[40m')"
DEFAULT_FG="$(printf '\033[39m')"  DEFAULT_BG="$(printf '\033[49m')"

echo -n "${BLUE}[${RED}!${BLUE}] ${GREEN}Loading Installing In Termux..,"
echo ""
echo -n "${BLUE}[${RED}!${BLUE}] ${GREEN}All utilities will work..."
echo ""
cd
cd
cd AllHackingTools
cd termux-style
./uninstall
cd && cd && cd AllHackingTools
git clone https://github.com/adi1090x/termux-style
cd termux-style
./install
cd
cd
clear
cd
cd 
Rootkite-delete-qiq
cd
cd
rm -rf qiq
cd
cd
git clone https://github.com/mishakorzik/qiq
cd qiq
bash install.sh
cd
cd
cd AllHackingTools
cd Termux-os
bash TermuxNewKeys.sh
cd
cd
clear
rm -rf Termux-os
rm -rf qiq
cd
cd
cd AllHackingTools
cp -r Termux-os /data/data/com.termux/files/home
am broadcast --user 0 -a com.termux.app.reload_style com.termux > /dev/null
cd
cd
cd AllHackingTools
cd .fonts
chmod +x *
cp * /data/data/com.termux/files/usr/share/figlet
cd
cd AllHackingTools
cd Tool
cp msdc /data/data/com.termux/files/usr/bin/
cp msdconsole /data/data/com.termux/files/usr/bin/
cp msdconsoleUPD /data/data/com.termux/files/usr/bin/
cp msdServer /data/data/com.termux/files/usr/bin/
cp msd /data/data/com.termux/files/usr/bin/
cp ms /data/data/com.termux/files/usr/bin/
cp m /data/data/com.termux/files/usr/bin/
cp sys /data/data/com.termux/files/usr/bin/
cp system /data/data/com.termux/files/usr/bin/
cp View-deleted-activity /data/data/com.termux/files/usr/bin/
cp Theme /data/data/com.termux/files/usr/bin/
cp theme /data/data/com.termux/files/usr/bin/
cp standart /data/data/com.termux/files/usr/bin/
cp edit /data/data/com.termux/files/usr/bin/
cd
cd
cd /data/data/com.termux/files/usr/bin/
chmod +x msdconsole
chmod +x msdconsoleUPD
chmod +x msdc
chmod +x msdServer
chmod +x msd
chmod +x ms
chmod +x m
chmod +x sys
chmod +x system
chmod +x View-deleted-activity
chmod +x Theme
chmod +x theme
chmod +x standart
chmod +x edit
cd
cd
rm -rf Termux-os
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
sleep 0.1
am broadcast --user 0 -a com.termux.app.reload_style com.termux > /dev/null
echo -n "${BLUE}[${GREEN}+${BLUE}] ${GREEN}Succesful Installed..!"
echo ""
