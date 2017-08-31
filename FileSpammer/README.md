# File Spammer

## Overview
Quick little piece of BASH script that I wrote to spam my friend's Mac with files after he foolishly let me SSH into his machine.

## How to Use
### Running
Just run `chmod +x spam.sh` to give it permissions then execute `./spam.sh` and watch it go!

### Stopping
To stop it, just do `^C` (for normal people, the ^ means to hold the Control key and the C means to press the C key).

### Removing
If you want to remove the mess that you've made, just run `rm *.spam` within the directory. This will remove all files with the extention `.spam`, which are the only files which are created within this program.
