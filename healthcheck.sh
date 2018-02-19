function main
{
    touch healthcheck.lock
    check_services
    rm healthcheck.lock
}

function check_services
{
    for file in checks/services/*.sh; do
         source $file

         # Calls the check method from each script
         result_from_service=$(check)

         if [[ $result_from_service -eq 0 ]]; then
             echo "[$file] ✔"
         else
             echo "[$file] ✖"
         fi
    done
}

main

