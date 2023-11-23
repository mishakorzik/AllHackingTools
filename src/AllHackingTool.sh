cd
cd
cd AllHackingTools
python3 src/CheckVersion.py
python3 .check/CheckServerYesAndNo.py
sleep 3
clear
g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
cd
cd
cd AllHackingTools 
cd Tool
mv MainMenu.py /data/data/com.termux/files/home/AllHackingTools
cd
cd AllHackingTools
clear
echo -e $b"[ ✔ ]"$g"Succesfully Verified"$w
python2 MainMenu.py
