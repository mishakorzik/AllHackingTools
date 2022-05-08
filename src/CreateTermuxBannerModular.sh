cd
cd 
cd /data/data/com.termux/files/usr/etc/
rm -rf zshrc
cd
cd
cd AllHackingTools
cd Tool
cp zshrc /data/data/com.termux/files/usr/etc/
cd
cd
clear
figlet -f big Termux Banner | lolcat -p 0.7

cyan='\e[0;36m'
lightgreen='\e[1;32m'
red='\e[1;31m'
yellow='\e[1;33m'

echo " "
echo " "
echo -e "\e[1m\e[33m\nEnter Your \e[31mBanner \e[33mName\e[32m :\n\n"
read eybn
echo
echo -e "\e[1m\e[33m\nEnter Your Cowsay Name\e[32m :\n\n "
read eycn
echo  "clear && cowsay -f eyes "$eycn" | lolcat -p 1.0" > C0w54y.txt
echo "toilet -f modular ' $eybn' -F gay | lolcat -p 1.0" > 84nn3r.txt
echo "cd && bash AllHackingTools/Tool/UserInfo.sh" > U3eR1nf0.txt
echo
cat "C0w54y.txt" >> /data/data/com.termux/files/usr/etc/zshrc
ls
cat "84nn3r.txt" >> /data/data/com.termux/files/usr/etc/zshrc
cat "U3eR1nf0.txt" >> /data/data/com.termux/files/usr/etc/zshrc
cd
cd
rm -rf 84nn3r.txt
rm -rf C0w54y.txt
rm -rf cl34r.txt
rm -rf U3eR1nf0.txt
