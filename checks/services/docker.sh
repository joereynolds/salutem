function check
{
    result=$(sudo service docker status | grep 'running')

    if [[ $result ]]; then
        echo 0
    else
        echo 1
    fi
}
