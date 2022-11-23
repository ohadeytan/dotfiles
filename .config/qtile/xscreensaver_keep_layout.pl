#!/usr/bin/perl

system("xscreensaver &");
system("sleep 3");
my $blanked = 0;
open (my $in, "xscreensaver-command -watch |") || die;
while (<$in>) {
    if (m/^(LOCK)/) {
        if (!$blanked) {
            system ("setxkbmap -layout us");
            $blanked = 1;
        }
    } elsif (m/^UNBLANK/) {
        $blanked = 0;
    }
}
