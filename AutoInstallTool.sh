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
echo ██████╗░░█████╗░███╗░░██╗███████╗
echo ██╔══██╗██╔══██╗████╗░██║██╔════╝
echo ██║░░██║██║░░██║██╔██╗██║█████╗░░
echo ██║░░██║██║░░██║██║╚████║██╔══╝░░
echo ██████╔╝╚█████╔╝██║░╚███║███████╗
echo ╚═════╝░░╚════╝░╚═╝░░╚══╝╚══════╝
echo Developer: mishakorzhik
echo Update on: 17 05 2021
echo Run command: bash Mask-Phish.sh
echo Run command: cd haxorbd && python2 haxor.py
echo Run command: cd SocialBox-Termux && ./SocialBox.sh
echo Run command: python3 impulse.py --method SMS --time 20 --threads 15 --target Номер
