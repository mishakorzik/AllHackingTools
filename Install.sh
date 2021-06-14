clear
g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
echo "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╭╮╱╱╱╱╱╱╭━━━━╮╱╱╭━━━╮╭╮╱╱╱╱╱╭╮"
echo "┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱┃╭━━╯╱╭╯╰╮╱╱╱╱╱┃╭╮╭╮┃╱╱┃╭━╮┣╯╰╮╱╱╱╭╯╰╮"
echo "┃╰━╯┣━┳━━┳━━┳━━╮┃╰━━┳━╋╮╭╋━━┳━╮╰╯┃┃┣┻━╮┃╰━━╋╮╭╋━━┳┻╮╭╯"
echo "┃╭━━┫╭┫┃━┫━━┫━━┫┃╭━━┫╭╮┫┃┃┃━┫╭╯╱╱┃┃┃╭╮┃╰━━╮┃┃┃┃╭╮┃╭┫┃"
echo "┃┃╱╱┃┃┃┃━╋━━┣━━┃┃╰━━┫┃┃┃╰┫┃━┫┃╱╱╱┃┃┃╰╯┃┃╰━╯┃┃╰┫╭╮┃┃┃╰╮"
echo "╰╯╱╱╰╯╰━━┻━━┻━━╯╰━━━┻╯╰┻━┻━━┻╯╱╱╱╰╯╰━━╯╰━━━╯╰━┻╯╰┻╯╰━╯"
echo "Please press enter to start installing tool..."
read a1
echo -e $r"PLEASE A DON'T CLOSE TERMUX APP!"$w
sleep 1
cd
cd
cd AllHackingTools
pkg remove game-repo
pkg remove science-repo
pkg clean
bash Files/Modules.sh
