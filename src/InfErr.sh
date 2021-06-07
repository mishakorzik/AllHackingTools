g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
o="\033[1;33m"

echo -e $w"["$g"INFO"$w"]"$b"Starting tool menu. Please wait a moment!"$w
sleep 0.06
echo -e $w"["$o"WARN"$w"]"$b"A don't close termux app! And exit termux!"$w
sleep 0.07
echo -e $w"["$r"ERROR"$w"]"$b"Error to starting tool! Error code 25-39"$w
sleep 0.02
echo -e $w"["$g"INFO"$w"]"$b"Reloading Tools. Please wait!"$w
cd
cd AllHackingTools
python2 MainMenu.py




