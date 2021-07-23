cd
cd
rm -rf ~/.termux/colors.properties
rm -rf /data/data/com.termux/files/usr/etc/motd
cd ~/AllHackingTools/Themes/.object ; cp -r .colors.properties5 ~/.termux/colors.properties
tput sgr0 #reset attributes
tput op #reset color
am broadcast --user 0 -a com.termux.app.reload_style com.termux > /dev/null
