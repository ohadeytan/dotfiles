#!/bin/bash

# Increase acceleration
xinput set-prop "TPPS/2 IBM TrackPoint" "libinput Accel Speed" 1
# Switch left and right buttons
xinput set-prop "TPPS/2 IBM TrackPoint" "libinput Left Handed Enabled" 1
xinput set-prop "Logitech MX Anywhere 3" "libinput Left Handed Enabled" 1
# Enable tapping
xinput set-prop "Synaptics TM3276-022" "libinput Tapping Enabled" 1
# Enable edge scrolling
xinput set-prop "Synaptics TM3276-022" "libinput Scroll Method Enabled" 0, 1, 0
# Start solaar for Logitech
solaar -w hide &
