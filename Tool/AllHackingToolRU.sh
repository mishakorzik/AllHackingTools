clear
cd
cd AllHackingTools
bash Tool/AnimationLoadRU.sh
g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
echo "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╭╮╱╱╱╱╱╱╭━━━━╮╱╱╭━━━╮╭╮╱╱╱╱╱╭╮"
echo "┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱┃╭━━╯╱╭╯╰╮╱╱╱╱╱┃╭╮╭╮┃╱╱┃╭━╮┣╯╰╮╱╱╱╭╯╰╮"
echo "┃╰━╯┣━┳━━┳━━┳━━╮┃╰━━┳━╋╮╭╋━━┳━╮╰╯┃┃┣┻━╮┃╰━━╋╮╭╋━━┳┻╮╭╯"
echo "┃╭━━┫╭┫┃━┫━━┫━━┫┃╭━━┫╭╮┫┃┃┃━┫╭╯╱╱┃┃┃╭╮┃╰━━╮┃┃┃┃╭╮┃╭┫┃"
echo "┃┃╱╱┃┃┃┃━╋━━┣━━┃┃╰━━┫┃┃┃╰┫┃━┫┃╱╱╱┃┃┃╰╯┃┃╰━╯┃┃╰┫╭╮┃┃┃╰╮"
echo "╰╯╱╱╰╯╰━━┻━━┻━━╯╰━━━┻╯╰┻━┻━━┻╯╱╱╱╰╯╰━━╯╰━━━╯╰━┻╯╰┻╯╰━╯"
echo "Для запуска системи нажмите enter"
read a1
echo -e $b">"$w" Проверка модуля: "$g"python2"$w
apt-get install python
echo -e $b"[ ✔ ]"$g"succesfull verifined"$w
echo -e $b">"$w" Проверка модуля: "$g"pip3"$w
apt-get install pip3
echo -e $b"[ ✔ ]"$g"succesfull verifined"$w
echo -e $b">"$w" Проверка модуля: "$g"requests"$w
pip3 install requests
echo -e $b"[ ✔ ]"$g"succesfull verifined"$w
echo -e $b">"$w" Проверка модуля: "$g"php"$w
apt-get install php
echo -e $b"[ ✔ ]"$g"succesfull verifined"$w
echo -e $b">"$w" Проверка модуля: "$g"wget"$w
apt-get install wget
echo -e $b"[ ✔ ]"$g"succesfull verifined"$w
echo -e $b">"$w" Проверка модуля: "$g"openssh"$w
apt-get install openssh
echo -e $b"[ ✔ ]"$g"succesfull verifined"$w
echo "Succesfull verifined!"
clear
bash Logo1.sh
sleep 0.2
python2 Tool/MainMenuRU.py
termux-vibrate -d 120 -f
