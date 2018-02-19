function check
{
    result=$(sudo service apache2 status | grep 'running')

    if [[ $result ]]; then
        echo 0
    else
        echo 1
    fi
}
