function check
{
    result=$(ping -w 5 joereynoldsaudio.com | wc -l)

    if [[ "$result" -eq 10 ]]; then
        echo 0
    else
        echo 1
    fi

}
