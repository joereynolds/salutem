set -o errexit

[ ! -d ~/.config/salutem/checks ] && echo 'No custom checks found, you can write your own in ~/.config/salutem/checks'


function main
{
    check
}

function check
{
    for file in checks/**/*.sh ~/.config/salutem/checks/*.sh; do
         source $file

         # Calls the check method from each script
         if [[ "$(check)" -eq 0 ]]; then
             printf "\033[0;32m✔ \033[0m [$file]\n"
         else
             printf "\033[0;31m✖ \033[0m [$file]\n"
         fi
    done
}

main
