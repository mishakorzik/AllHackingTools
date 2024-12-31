import os
import sys
import time

def default_install():
    os.system("cd && rm -rf AutoUpdateMyTools && cd && git clone https://github.com/mishakorzik/AutoUpdateMyTools && cd AutoUpdateMyTools && bash AllHackingToolupdate.sh")

def speed_install():
    os.system("cd && cd AllHackingTools && cd src && bash SpeedUpdate.sh")

def quit_updater():
    print("\033[1;31;40mQuiting AllHackingTool Updater...")
    sys.exit()

def main():
    os.system("clear")
    os.system("cd && cd AllHackingTools && bash src/LiteLogo.sh")

    print("")
    print("  \033[1;34m[01] \033[1;36;40mDefault Installing  -  Standard installing RECOMMEND")
    print("  \033[1;34m[02] \033[1;36;40mSpeed Installing  -  Very fast download NOT RECOMMEND")
    print("  \033[1;34m[03] \033[1;36;40mQuit Updater  -  Exit and do not update AllHackingTools")

    op = int(input("UPda1Er: "))

    if op == 1:
        default_install()
    elif op == 2:
        speed_install()
    elif op == 3:
        quit_updater()
    else:
        print("\033[1;31;40mInvalid input. Quiting AllHackingTools Updater")
        time.sleep(0.8)

if __name__ == "__main__":
    main()
