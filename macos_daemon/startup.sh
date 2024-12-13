#!/bin/sh

set -ex


USER="omkar"
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

echo "$TIMESTAMP - Updating wallpaper as $(whoami) ... "

# Check if the current user is root
if [ "$EUID" -eq 0 ]; then
    su - "$USER" -c "/usr/bin/python3 /Users/omkar/scripts/background_blender/macos_daemon/macos_daemon.py"
else
    /usr/bin/python3 /Users/omkar/scripts/background_blender/macos_daemon/macos_daemon.py
fi

echo "Successfully updated wallpaper"
