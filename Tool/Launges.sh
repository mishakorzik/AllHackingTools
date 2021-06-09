echo "please select launges!"
echo " 1.Russian
echo " 2.English
echo " 3.ERROR
read lan
if [ $lan -eq 1 ];then
echo "Succesfull! Choised Russian"
cd
cd
cd AllHackingTools
cd Tool
cp msdconsoleRU /data/data/com.termux/files/home/
ls
rm -rf msdconsoleRU
cd 
cd 
chmod +x msdconsoleRU
elif [ $lan -eq 2 ];then
echo "Succesfull! Choised English"
cd
cd
cd AllHackingTools
cd Tool
cp msdconsole /data/data/com.termux/files/home/
ls
rm -rf msdconsole
cd 
cd 
chmod +x msdconsole
elif [ $lan -eq 3 ];then
echo "Succesfull! Choised English"
cd
cd
cd AllHackingTools
cd Tool
cp msdconsole /data/data/com.termux/files/home/
ls
rm -rf msdconsole
cd 
cd 
chmod +x msdconsole
