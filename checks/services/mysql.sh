function check
{
    result=$(sudo service mysql status | grep 'running')

    if [[ $result ]]; then
        echo 0
    else
        echo 1
    fi
}
