from src.checker import Checker
from src.config import Configuration
from src.salutem import Salutem

if __name__ == '__main__':
    salutem = Salutem(Checker(Configuration('~/.config/salutem/checks')))
    salutem.run()


#check() {
#    for file in checks/**/*.sh ~/.config/salutem/checks/*.sh; do
#         source $file

#         # Calls the check method from each script
#         if [[ "$(check)" -eq 0 ]]; then

#             if [ "$1" == '--only-show-failures' ]; then
#                 continue
#             fi

#             if [ "$1" == '--colored' ]; then
#                 print_coloured_success $file
#             else
#                 print_plain_success $file
#             fi

#         else

#             if [ "$1" == '--colored' ]; then
#                 print_coloured_failure $file
#             else
#                 print_plain_failure $file
#             fi

#             if [ "$1" == '--stop-on-failure' ]; then
#                 exit 1
#             fi

#         fi
#    done
#}

#print_coloured_success() {
#    printf "\033[0;32m✔ \033[0m [$1]\n"
#}

#print_coloured_failure() {
#    printf "\033[0;31m✖ \033[0m [$1]\n"
#}

#print_plain_success() {
#    echo "✔ [$1]"
#}

#print_plain_failure() {
#    echo "✖ [$1]"
#}

#main $1
