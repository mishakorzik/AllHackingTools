red='\e[1;31m'
default='\e[0m'
yellow='\e[0;33m'
orange='\e[38;5;166m'
green='\033[92m'

arch=`arch`
if [ -f "ngrok" ]; then
echo -e "$green[+]-[Ngrok]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo -e "$red[-]-[Ngrok]........................[ NOT FOUND ]"
sleep 0.2
echo -e "$yellow[!]-[Downloading:Ngrok.................]"
sleep 1.2
cd 
cd
cd AllHackingTools
cd Castom
cp ngrok /data/data/com.termux/files/home/
cd
cd
chmod +x ngrok
echo -e "$yellow[+]-[Ngrok Installed!................]"
sleep 1.5
fi

