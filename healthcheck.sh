

touch healthcheck.lock

# bunch of stuff
for file in checks/*.sh; do
     echo "[$file]"
done

rm healthcheck.lock


