tput sgr0 #reset attributes
tput op #reset color
cd
cd
rm -rf ~/.termux/colors.properties
rm -rf /data/data/com.termux/files/usr/etc/motd
cd ~/AllHackingTools/Themes/.object ; cp -r .colors.properties3 ~/.termux/colors.properties
