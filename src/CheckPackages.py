R = '\033[31m'
G = '\033[32m' 
C = '\033[36m' 
W = '\033[0m'  

from shutil import which

print(G + '[ ✔ ]' + C + ' Checking Packages...' + W)
pkgs = ['python', 'pip', 'python2', 'ssh', 'lolcat', 'figlet', 'pip2', 'git', 'wget', 'openssh', 'clang', 'neofetch']
inst = True
for pkg in pkgs:
        present = which(pkg)
        if present == None:
                print(R + '[ ✘ ] ' + W + packages + C + ' is not Installed!')
                inst = False
        else:
                pass
if inst == False:
        exit()
else:
        pass
print(G + '[ ✔ ]' + C + ' All modules succesfull checked...' + W)
