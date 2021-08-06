g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"

clear
cd
cd AllHackingTools
bash Logo.sh
cd HatCloud
echo ""
echo -e $b">>>"$w" Write the name of the site without http & https: "$g"HatCloud"$w
read siteURL3
sleep 0.1
echo -e $b">>>"$w" Please wait a moment: "$g"HatCloud"$w
sleep 0.6
ruby hatcloud.rb -b $siteURL3
cd
cd
cd AllHackingTools
