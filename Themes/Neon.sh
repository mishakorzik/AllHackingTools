cd
cd
apt install toilet figlet exa wget ruby 
rm -rf ~/.termux/colors.properties
rm -rf /data/data/com.termux/files/usr/etc/motd
cd ~/AllHackingTools/Themes/.object ; cp -r .colors.properties ~/.termux/colors.properties
cd ~/AllHackingTools/Themes/.object ; cp -r .termux.properties ~/.termux/termux.properties
