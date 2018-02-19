function main
{
    touch healthcheck.lock
    check_services
    check_custom_checks
    rm healthcheck.lock
}

function check_services
{
    for file in checks/services/*.sh; do
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

function check_custom_checks
{
    for file in checks/custom/*.sh; do
         source $file

         # Calls the check method from each script
         if [[ "$(check)" -eq 0 ]]; then
             echo "[$file] ✔"
         else
             echo "[$file] ✖"
         fi
    done
}

main
