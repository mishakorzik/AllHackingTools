echo -e "${WHITE}              [1] Termux "
echo -e "${WHITE}              [0] Exit "
echo -n -e "НаСK1NG >> "
read choice
INSTALL_DIR="/usr/share/doc/Tools-Hacking"
BIN_DIR="/usr/bin/"
if [ $choice == 1 ]; then 
	echo "[*] Checking Internet Connection .."
	wget -q --tries=10 --timeout=20 --spider https://google.com
	if [[ $? -eq 0 ]]; then
        cd
        cd AllHackingTools
        bash Files/Modules.sh
