clear
cd
cd
cd AllHackingTools
bash src/AnimationLoad1.sh
clear
g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
echo '
╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╭╮╱╱╱╱╱╱╭━━━━╮╱╱╭━━━╮╭╮╱╱╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱┃╭━━╯╱╭╯╰╮╱╱╱╱╱┃╭╮╭╮┃╱╱┃╭━╮┣╯╰╮╱╱╱╭╯╰╮
┃╰━╯┣━┳━━┳━━┳━━╮┃╰━━┳━╋╮╭╋━━┳━╮╰╯┃┃┣┻━╮┃╰━━╋╮╭╋━━┳┻╮╭╯
┃╭━━┫╭┫┃━┫━━┫━━┫┃╭━━┫╭╮┫┃┃┃━┫╭╯╱╱┃┃┃╭╮┃╰━━╮┃┃┃┃╭╮┃╭┫┃
┃┃╱╱┃┃┃┃━╋━━┣━━┃┃╰━━┫┃┃┃╰┫┃━┫┃╱╱╱┃┃┃╰╯┃┃╰━╯┃┃╰┫╭╮┃┃┃╰╮
╰╯╱╱╰╯╰━━┻━━┻━━╯╰━━━┻╯╰┻━┻━━┻╯╱╱╱╰╯╰━━╯╰━━━╯╰━┻╯╰┻╯╰━╯
Please press enter to launch...'|lolcat -p 1.7 -a -d 7 -s 45.0
read a1
echo -e $b">"$w" verify modules: "$g"python2"$w
apt-get install python
echo -e $b"[ ✔ ]"$g"succesfull verifined"$w
echo -e $b">"$w" verify modules: "$g"pip2"$w
apt-get install pip2
echo -e $b"[ ✔ ]"$g"succesfull verifined"$w
echo -e $b">"$w" verify modules: "$g"requests"$w
pip3 install requests
echo -e $b"[ ✔ ]"$g"succesfull verifined"$w
echo -e $b">"$w" verify modules: "$g"php"$w
apt-get install php
echo -e $b"[ ✔ ]"$g"succesfull verifined"$w
echo -e $b">"$w" verify modules: "$g"wget"$w
apt-get install wget
echo -e $b"[ ✔ ]"$g"succesfull verifined"$w
echo ""
echo "$g"Checking AllHackingTools for updates....."
python3 src/CheckVersion.py
clear
sleep 0.2
python2 MainMenu.py
