pkg install zsh
chsh -s zsh

rm -rf ~/.zshrc
git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
apt update && apt upgrade
pkg install zsh -y
pkg install git -y
pkg install ruby  -y
pkg install wget  -y
gem install lolcat 
pkg install curl -y
pkg install zsh -y
dpkg --configure -a
clear
wget -O $PREFIX/share/figlet/ASCII-Shadow.flf https://raw.githubusercontent.com/xero/figlet-fonts/master/ANSI%20Shadow.flf
git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh
cd
cd
apt install toilet figlet exa wget ruby 
rm -rf ~/.termux/colors.properties
rm -rf /data/data/com.termux/files/usr/etc/motd
cd ~/AllHackingTools/Themes/.object ; cp -r .colors.properties5 ~/.termux/colors.properties
