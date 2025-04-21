g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
red='\e[1;31m'
default='\e[0m'
yellow='\e[0;33m'
orange='\e[38;5;166m'
green='\033[92m'

clear
sleep 1.5
echo -e "$default"
apt install python
apt install python2 
apt install pip
apt install pip2
pip install requests
pip2 install requests

# Install Docker if not already installed
if ! command -v docker &> /dev/null
then
    echo -e "$r Docker not found, installing... $w"
    apt-get update
    apt-get install -y docker.io
    systemctl start docker
    systemctl enable docker
else
    echo -e "$g Docker is already installed $w"
fi

# Install Docker Compose if not already installed
if ! command -v docker-compose &> /dev/null
then
    echo -e "$r Docker Compose not found, installing... $w"
    curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
else
    echo -e "$g Docker Compose is already installed $w"
fi

# Build and run the Docker container
cd /path/to/AllHackingTools
docker-compose up --build -d

cd
cd
cd AllHackingTools
python2 src/InstallMenu.py
