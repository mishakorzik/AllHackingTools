g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"

clear
cd
cd AllHackingTools
cd nikto/program
clear
./nikto.pl
echo "Please enter all your required settings to run the program, for example: -h https://www.example.com"
echo -e $b">>>"$w" Consoler "$g"Nikto"$w
read opt
sleep 0.1
./nikto.pl $opt
cd
cd
cd AllHackingTools
