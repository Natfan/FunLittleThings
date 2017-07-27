# Touch Toggler

## Overview
A dash of bash that allows me to toggle my keyboard to have the TapToClick feature enabled by default on startup, dynamically. Please note that this has only been tested on my machine, and may not work on anything else. This also acts as a toggle.

## How to Use
Just run `chmod +x touch.sh` to give it permissions then execute `./touch.sh` and the feature will be enabled or disabled.

To enable on startup, simple add:

```bash
mkdir -p $HOME/.toggles    # adds the toggles folder as a hidden (dot) folder so that it doesn't clutter your LSing. Used to store if the program has been toggled or not, independant of temporary memory.
touch $HOME/.toggles/touch # adds the toggle file so that
sh /path/to/touch.sh       # runs the touch command, which will enable the protocol dynamically, based on what the touchpad ID is set to on startup.
```

and away you go!
