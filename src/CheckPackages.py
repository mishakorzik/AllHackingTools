R = '\033[31m'
G = '\033[32m' 
C = '\033[36m' 
W = '\033[0m'  

from shutil import which
import time

print(G + '[ ✔ ]' + C + ' Checking Packages...' + W)
time.sleep(1)
pkgs = ['python', 'pip', 'python2', 'ssh', 'lolcat', 'figlet', 'pip2', 'git', 'wget', 'clang', 'neofetch', 'pv', 'zsh', 'curl', 'w3m']
inst = True
for pkg in pkgs:
        present = which(pkg)
        if present == None:
                print(R + '[ ✘ ] ' + W + pkg + C + ' is not Installed!')
                inst = False
        else:
                pass
if inst == False:
        exit()
else:
        pass
print(G + '[ ✔ ]' + C + ' Succesfull checked! modules...' + W)
time.sleep(0.2)
print(G + '[ ✔ ]' + C + ' All modules installed...' + W)
time.sleep(0.1)
