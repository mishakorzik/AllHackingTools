echo "Enter module name. To install"
read qip1
echo -e $b">>>"$w" One step. To installing: "$g"$qip1"$w
pkg clean
pkg install "$qip1"
echo -e $b">>>"$w" Two step. To installing: "$g"$qip1"$w
apt clean
apt install "$qip1"
echo -e $b">>>"$w" Three step. To installing: "$g"$qip1"$w
apt-get clean
apt-get install "$qip1"
echo -e $b">>>"$w" Succesfull installed module: "$g"$qip1"$w
