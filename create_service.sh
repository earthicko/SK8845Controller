#!/bin/bash

# Get the current directory
CWD=$(pwd)

# Compose executable's path
EXECPATH="$CWD/$1"

# Create the service file
cat > $2 << EOF
[Unit]
Description=HIDI2CRelay
After=multi-user.target
 
[Service]
Type=simple
ExecStart=$EXECPATH
ExecStartPost=/usr/bin/bash -c 'echo none > /sys/class/leds/led0/trigger'
ExecStopPost=/usr/bin/bash -c 'echo heartbeat > /sys/class/leds/led0/trigger'
WorkingDirectory=$CWD
Restart=on-abort
 
[Install]
WantedBy=multi-user.target
EOF
