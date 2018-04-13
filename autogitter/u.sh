#!/bin/bash

return="$PWD"

function syntax {
    echo "Syntax: $0 <stats|keys|uauth> <commit message>"
}

if [[ -z $1 || -z $2 ]]; then
    syntax
    exit 1
fi

case $1 in
    "stats") 
    cd ~/code/hypixel
        git add .
        git commit -S -m "$2"
        git push
        ssh nat "cd /var/www/html/natfan.io/public_html/hypixel/; git pull;"
        cd $return
        ;;
    "keys")
        cd ~/code/keys
        git add .
        git commit -S -m "$2"
        git push
        ssh nat "cd /var/www/html/natfan.io/public_html/keys/; git pull;"
        cd $return
        ;;
    "uauth")
        cd ~/code/undertone/auth
        git add .
        git commit -S -m "$2"
        git push
        ssh nat "cd /var/www/html/code.natfan.io/public_html/undertone/; git pull;"
        cd $return
        ;;
    *)
        syntax
        cd $return
        ;;
esac
