# Use a suitable base image for a lean and compatible Linux distro
FROM debian:latest

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Update and install necessary dependencies
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    git \
    curl \
    wget \
    openssh-client \
    php \
    neofetch \
    figlet \
    toilet \
    jq \
    ruby \
    pv \
    unzip \
    && apt-get clean

# Install Ciphey
RUN git clone https://github.com/bee-san/Ciphey.git /opt/ciphey && \
    cd /opt/ciphey && \
    pip3 install -r requirements.txt && \
    python3 -m pip install .

# Install hackingtool
RUN git clone https://github.com/Z4nzu/hackingtool.git /opt/hackingtool && \
    cd /opt/hackingtool && \
    chmod +x install.sh && \
    ./install.sh

# Copy AllHackingTools repository
COPY . /opt/AllHackingTools

# Set working directory
WORKDIR /opt/AllHackingTools

# Expose necessary ports
EXPOSE 80 443 8080

# Start the application
CMD ["bash", "Install.sh"]
