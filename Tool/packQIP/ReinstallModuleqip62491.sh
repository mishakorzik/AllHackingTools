echo "Enter module name. To reinstall"
read qip3
echo -e $b">>>"$w" One step. To reinstalling: "$g"$qip3"$w
pkg clean
pkg reinstall "$qip3"
echo -e $b">>>"$w" Two step. To reinstalling: "$g"$qip3"$w
apt clean
apt reinstall "$qip3"
echo -e $b">>>"$w" Three step. To reinstallig: "$g"$qip3"$w
apt-get clean
apt-get reinstall "$qip3"
echo -e $b">>>"$w" Succesfull reinstalled module: "$g"$qip3"$w
