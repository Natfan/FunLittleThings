#!/bin/bash

return=$PWD

function syntax {
    echo "Syntax: $0 <stats|keys|uauth> <commit message>"
}

if [[ -z $1 || -z $2 || "$#" -gt 3 ]]; then
    syntax
    exit 1
fi

function gitstuff {
    git add .
    git commit -m "$1"
    git push
}

# pushthatcode("code" "message")
function pushthatcode {
    case $1 in
        "stats")
            cd ~/code/hypixel
            gitstuff $2
            ssh nat "cd /var/www/html/natfan.io/public_html/hypixel/; git pull;"
            ;;
        "keys")
            cd ~/code/keys
            gitstuff $2
            ssh nat "cd /var/www/html/natfan.io/public_html/keys/; git pull;"
            ;;
        "undertone auth")
            cd ~/code/undertone/auth
            gitstuff $2
            ssh nat "cd /var/www/html/code.natfan.io/public_html/undertone/; git pull;"
            ;;
        *)
            echo "ERROR: invalid 'push that code' sequence"
            ;;
    esac
}

case $1 in
    "stats") 
        pushthatcode "stats" $2
        cd $return
        ;;
    "keys")
        pushthatcode "keys" $2
        cd $return
        ;;
    "uauth")
        pushthatcode "undertone auth" $2
        cd $return
        ;;
    *)
        syntax
        cd $return
        ;;
esac
