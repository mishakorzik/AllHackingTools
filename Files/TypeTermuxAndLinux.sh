RED="$(printf '\033[31m')"  GREEN="$(printf '\033[32m')"  ORANGE="$(printf '\033[33m')"  BLUE="$(printf '\033[34m')"
MAGENTA="$(printf '\033[35m')"  CYAN="$(printf '\033[36m')"  WHITE="$(printf '\033[37m')" BLACK="$(printf '\033[30m')"
REDBG="$(printf '\033[41m')"  GREENBG="$(printf '\033[42m')"  ORANGEBG="$(printf '\033[43m')"  BLUEBG="$(printf '\033[44m')"
MAGENTABG="$(printf '\033[45m')"  CYANBG="$(printf '\033[46m')"  WHITEBG="$(printf '\033[47m')" BLACKBG="$(printf '\033[40m')"
DEFAULT_FG="$(printf '\033[39m')"  DEFAULT_BG="$(printf '\033[49m')"

clear
echo "${BLUE}------------ ---------"
echo "| ${RED} Select Option ${BLUE}     |"
echo "|------- ----  -------|"
echo "| ${GREEN}1. Termux ${BLUE} "
echo "| ${GREEN}2. Linux ${BLUE} "
echo "|                     |"
echo "| ${RED}While 1/2:${BLUE}          |"
echo "----  ---------- ------     "
read numb
clear
echo "${BLUE}------------ ---------"
echo "| ${RED} Select Option ${BLUE}     |"
echo "|------- ----  -------|"
echo "| ${CYAN}1. Termux ${BLUE} "
echo "| ${CYAN}2. Linux ${BLUE} "
echo "|                     |"
echo "| ${RED}While 1/2:${BLUE}          |"
echo "----  ---------- ------     "
if [ $numb = "1" ]
then
        echo -n "${BLUE}[${RED}!${BLUE}] ${GREEN}Loading Installing In Termux..."
	echo ""
	cd
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
	ls
	sleep 0.1
	clear
	cd 
        cd 
        clear
        rm -rf Termux-os
        rm -rf qiq
        cd
        cd 
        cd AllHackingTools 
        cp -r Termux-os /data/data/com.termux/files/home 
        cd 
        cd
        cd Termux-os 
        bash TermuxNewKeys.sh 
        cd
        cd
	sleep 0.9
	echo -n "${BLUE}[${GREEN}+${BLUE}] ${GREEN}Succesful Installed..!"
	echo ""
else
        if [ $numb = "2" ]
        then
                echo -n "${BLUE}[${RED}!${BLUE}] ${GREEN}Loading Installing In Linux..."
		echo ""
		cd
		cd
		cd AllHackingTools
		cd Tool
		cp msdc /usr/local/bin/
		cp msdconsole /usr/local/bin/
		cp msdconsoleUPD /usr/local/bin/
		cp msdServer /usr/local/bin/
		cp msd /usr/local/bin/
		cp ms /usr/local/bin/
		cp m /usr/local/bin/
		cp sys /usr/local/bin/
		cp system /usr/local/bin/
		cp View-deleted-activity /usr/local/bin/
		cp theme /usr/local/bin/
		cp Theme /usr/local/bin/
		cd
        	cd
        	cd /usr/local/bin/
        	chmod +x msdconsole
        	chmod +x msdconsoleUPD
        	chmod +x msdc
        	chmod +x msdServer
        	chmod +x msd
        	chmod +x ms
        	chmod +x m
        	chmod +x sys
        	chmod +x system
		sleep 1
		echo -n "${BLUE}[${GREEN}+${BLUE}] ${GREEN}Succesful Installed..!"
		echo ""
	fi
fi
