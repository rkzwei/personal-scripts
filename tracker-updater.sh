#!/bin/bash

# Set the URL of the trackers list file
TRACKERS_URL="https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt"

# Set the path to the qBittorrent.conf file
QBITTORRENT_CONF="/home/qbtuser/.config/qBittorrent/qBittorrent.conf"

# Backup the original qBittorrent.conf file
cp "$QBITTORRENT_CONF" "$QBITTORRENT_CONF.backup"

# Download the new trackers list
curl -o /tmp/trackers_best.txt "$TRACKERS_URL"

# Escape special characters in the trackers list
NEW_TRACKERS=$(sed ':a;N;$!ba;s/\n/\\n/g' /tmp/trackers_best.txt)

# Replace the content of AdditionalTrackers in qBittorrent.conf
sed -i "s|\(Session\\AdditionalTrackers=\).*|\1${NEW_TRACKERS}|" "$QBITTORRENT_CONF"

# Clean up the temporary file
rm /tmp/trackers_best.txt

