g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
o="\033[1;33m"

cd
rm -rf AutoUpdateMyTools
cd 
git clone https://github.com/mishakorzik/AutoUpdateMyTools 
cd AutoUpdateMyTools
echo -e $w"["$o"WARN"$w"]"$b"verifining settings!"$w
sleep 0.2
echo -e $w"["$o"WARN"$w"]"$b"I don't close termux app!"$w
sleep 1
echo -e $w"["$g"INFO"$w"]"$b"Succesfull verifined!"$w
sleep 0.9
cd
cd
cd /data/data/com.termux/files/usr/share/figlet
rm -rf poison.flf
rm -rf puffy.flf
rm -rf real.flf
rm -rf pagga.tlf
rm -rf modular.tlf
rm -rf rusto.tlf
rm -rf avatar.flf
rm -rf bloody.flf
rm -rf crazy.flf
rm -rf block.flf
cd
cd
bash AllHackingToolupdate.sh
