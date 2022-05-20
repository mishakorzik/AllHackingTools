wget https://bin.equinox.io/a/e93TBaoFgZw/ngrok-2.2.8-linux-arm.zip > /dev/null 2>&1
if [[ -e ngrok-2.2.8-linux-arm.zip ]]; then
unzip ngrok-2.2.8-linux-arm.zip > /dev/null 2>&1
rm -rf $HOME/.ngrok2 > /dev/null 2>&1
chmod +x ngrok
rm -rf ngrok-2.2.8-linux-arm.zip
