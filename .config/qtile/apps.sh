#!/bin/bash
.screenlayout/home.sh
picom &
flameshot &
nm-applet &
blueman-applet &
redshift -m randr:crtc=1 -b 0.8 0.6 &
redshift -m randr:crtc=0 -b 0.95 0.85 &
perl ./xscreensaver_keep_layout.pl &
