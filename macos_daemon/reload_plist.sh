#!/bin/sh

set -ex


if [ "$EUID" -eq 0 ]; then
    echo "Unloading startup daemon from launchctl..."
    sudo launchctl unload /Library/LaunchDaemons/com.startup.daemon.plist

    echo "Copying $pwd/startup.sh to /Library/LaunchDaemons/com.startup.daemon"
    cp com.startup.daemon.plist /Library/LaunchDaemons/com.startup.daemon.plist

    echo "Loading startup daemon to lauchctl"
    sudo launchctl load -w /Library/LaunchDaemons/com.startup.daemon.plist
else
    echo "Please run as root (sudo)"
fi

