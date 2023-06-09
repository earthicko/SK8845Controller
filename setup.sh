#!/bin/bash
sudo apt-get update -y | sudo apt-get upgrade -y

sudo apt-get install git libglib2.0-dev python3-pip -y

sudo pip3 install asyncio
sudo pip3 install asyncio_glib
sudo pip3 install watchgod

sudo hostnamectl set-hostname SK-8845
sudo sed -Ei 's/^127\.0\.1\.1.*$/127.0.1.1\tSK-8845/' /etc/hosts

sudo reboot
