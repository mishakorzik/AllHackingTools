clear
echo By mishakorzhik
sleep 2
echo Loading please wait. Settings tool.
sleep 1
cd
apt update
apt upgrade
apt upgraded
sleep 1
echo Installing tools.
sleep 1
pkg install python2
pkg install git
pkg install python3
pkg install python
pkg install pip
pkg install curl
sleep 1
echo Installing Impulse.
sleep 1
git clone https://github.com/LimerBoy/Impulse
cd Impulse
pip3 install -r requirements.txt
cd
sleep 1
echo Installing SocialBox-Termux.
sleep 1
git clone https://github.com/samsesh/SocialBox-Termux.git 
cd SocialBox-Termux
chmod +x install-sb.sh
./install-sb.sh
cd
sleep 1
echo Installing haxorbd.
sleep 1
git clone https://github.com/htr-tech/haxorbd.git
cd
sleep 1 
echo Installing Mask-Phish
sleep 1
git clone https://github.com/mishakorzik/Mask-Phish
cd Mask-Phish
cd
sleep 2
echo Succesfull installed tools.
sleep 1
echo Trank for downloading tools.
echo By mishakorzhik.
echo 3
rand1=$( shuf -i 0-${#colors[@]} -n 1 )
rand2=$( shuf -i 0-${#colors[@]} -n 1 )
# Colors
r='\e[91m'
g='\e[92m'
y='\e[93m'
b='\e[94m'
p='\e[95m'
c='\e[96m'
w='\e[97m'
n='\e[0m'
# effect colors
bd='\e[1m'
dm='\e[2m'
it='\e[3m'
ul='\e[4m'
rv='\e[7m'
echo -e "\t${colors[rand1]} ██████╗░░█████╗░███╗░░██╗███████╗
echo -e "\t${colors[rand1]} ██╔══██╗██╔══██╗████╗░██║██╔════╝
echo -e "\t${colors[rand1]} ██║░░██║██║░░██║██╔██╗██║█████╗░░
echo -e "\t${colors[rand1]} ██║░░██║██║░░██║██║╚████║██╔══╝░░
echo -e "\t${colors[rand1]} ██████╔╝╚█████╔╝██║░╚███║███████╗
echo -e "\t${colors[rand1]} ╚═════╝░░╚════╝░╚═╝░░╚══╝╚══════╝
echo -e "\t${colors[rand1]} Developer: mishakorzhik 
echo -e "\t${colors[rand2]} Update on: 17 05 2021
echo -e "\t${colors[rand2]} Run command: bash Mask-Phish.sh
echo -e "\t${colors[rand2]} Run command: cd haxorbd && python2 haxor.py
echo -e "\t${colors[rand2]} Run command: cd SocialBox-Termux && ./SocialBox.sh
echo -e "\t${colors[rand2]} Run command: python3 impulse.py --method SMS --time 20 --threads 15 --target Номер
