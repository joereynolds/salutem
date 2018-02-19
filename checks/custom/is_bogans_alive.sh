function check
{
    result=$(curl -s bogans.uk | grep 'Instagram' | wc -l)

    if [[ "$result" -eq 1 ]]; then
        echo 0
    else
        echo 1
    fi

}
