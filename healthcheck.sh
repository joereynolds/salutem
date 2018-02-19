function main
{
    touch healthcheck.lock
    check
    rm healthcheck.lock
}

function check
{
    for file in checks/**/*.sh; do
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
