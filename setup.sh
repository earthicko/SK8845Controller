#!/bin/bash
sudo apt update -y | sudo apt upgrade -y

sudo apt install python3-pip -y

sudo pip3 install asyncio_glib
sudo pip3 install watchgod
sudo pip3 install spidev

sudo hostnamectl set-hostname SK-8845
sudo sed -Ei 's/^127\.0\.1\.1.*$/127.0.1.1\tSK-8845/' /etc/hosts

sudo reboot
