g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
o="\033[1;33m"

echo -e $w"["$g"INFO"$w"]"$b"Easy passworlds"$w
sleep 0.1
dd bs=12 count=1 if=/dev/urandom status=none | base32
dd bs=12 count=1 if=/dev/urandom status=none | base32
dd bs=12 count=1 if=/dev/urandom status=none | base64
dd bs=12 count=1 if=/dev/urandom status=none | base64
dd bs=16 count=1 if=/dev/urandom status=none | base64
dd bs=16 count=1 if=/dev/urandom status=none | base64
cd
cd
cd AllHackingTools
python3 src/Timer1.py
python2 src/aboutMenu.py   
cd
cd AllHackingTools
