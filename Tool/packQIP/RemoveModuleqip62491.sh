echo "Enter module name. To uninstall"
read qip2
echo -e $b">>>"$w" One step. To uninstalling: "$g"$qip2"$w
pkg clean
pkg uninstall "$qip2"
echo -e $b">>>"$w" Two step. To uninstalling: "$g"$qip2"$w
apt clean
apt remove "$qip2"
echo -e $b">>>"$w" Three step. To uninstalling: "$g"$qip2"$w
apt-get clean
apt-get remove "$qip2"
echo -e $b">>>"$w" Succesfull uninstalled module: "$g"$qip2"$w
