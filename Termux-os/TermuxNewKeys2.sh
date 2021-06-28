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
apt install toilet figlet exa wget ruby 
rm -rf ~/.termux/colors.properties
rm -rf ~/.termux/termux.properties
rm -rf ~/.termux/termux.properties2
rm -rf /data/data/com.termux/files/usr/etc/motd
cd ~/Termux-os/.object ; cp -r .colors.properties2 ~/.termux/colors.properties
cd ~/Termux-os/.object ; cp -r .termux.properties2 ~/.termux/termux.properties
