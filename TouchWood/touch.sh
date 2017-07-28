#!/bin/bash
# This is a command to enable tap-to-click on the fly for @Natfan's laptop.
# This has only been tested to work with a Toshiba Satellite P50D-C-104.

TOGGLE=$HOME/.toggles/touch

pointerstats=$(xinput | grep "Elantech Touchpad" | cut -d "=" -f 2) 
pointerid=$(echo "$pointerstats" | grep -o "[0-9][0-9]" )
tapstats=$(xinput list-props $pointerid | grep "libinput Tapping Enabled (")
tapid=$(echo "$tapstats" | grep -o "[0-9][0-9][0-9]" )

if [ -e $TOGGLE ] ; then
    rm $TOGGLE
    xinput set-prop $pointerid $tapid 0
    echo "Toggled TapToClick OFF"
else
    touch $TOGGLE
    xinput set-prop $pointerid $tapid 1
    echo "Toggled TapToClick ON"
fi

