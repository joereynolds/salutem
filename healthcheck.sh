set -o errexit
set -o nounset

[ ! -d ~/.config/salutem/checks ] && echo 'No custom checks found, you can write your own in ~/.config/salutem/checks'


function main
{
    check
}

function check
{
    for file in checks/**/*.sh ~/.config/salutem/checks/*.sh; do
         source $file

         # TODO check the service actuall exists
         # before doing the check() method

         # Calls the check method from each script
         if [[ "$(check)" -eq 0 ]]; then
             echo "[$file] ✔"
         else
             echo "[$file] ✖"
         fi
    done
}

main
