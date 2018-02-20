#!/bin/bash
set -o errexit

[ ! -d ~/.config/salutem/checks ] && echo 'No custom checks found, you can write your own in ~/.config/salutem/checks'

main() {

    if [ "$1" == "--help" ]; then
        display_help
        exit 0
    fi
    if [ "$1" != '--help' ] &&
       [ "$1" != '--colored' ] &&
       [ ! -z "$1" ]; then
        echo 'Incorrect option passed, try ./healthcheck.sh --help for more information'
        exit 0
    fi

    check $1
}

display_help() {
    echo '
    Usage: ./healthcheck.sh [OPTION]
    Run checks and output to standard output.

      --help     display this help and exit
      --colored  display the results with ANSI color codes

    Examples:
      ./healthcheck.sh Perform all checks in your ~/.config directory and checks directory.'
}

check() {
    for file in checks/**/*.sh ~/.config/salutem/checks/*.sh; do
         source $file

         # Calls the check method from each script
         if [[ "$(check)" -eq 0 ]]; then

             if [ "$1" == '--colored' ]; then
                 print_coloured_success $file
             else
                 print_plain_success $file
             fi

         else

             if [ "$1" == '--colored' ]; then
                 print_coloured_failure $file
             else
                 print_plain_failure $file
             fi

         fi
    done
}

print_coloured_success() {
    printf "\033[0;32m✔ \033[0m [$1]\n"
}

print_coloured_failure() {
    printf "\033[0;31m✖ \033[0m [$1]\n"
}

print_plain_success() {
    echo "✔ [$1]"
}

print_plain_failure() {
    echo "✖ [$1]"
}

main $1
