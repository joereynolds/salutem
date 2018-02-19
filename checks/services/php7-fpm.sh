function check
{
    result=$(sudo service php7-fpm status | grep 'running')

    if [[ $result ]]; then
        echo 0
    else
        echo 1
    fi
}
