# WIP

# Salutem ('health' in latin)

A basic healthcheck script for servers.

## Adding checks

### Services

If the service you want to check isn't supported, simply add it to the `checks` directory with the name of the service.
i.e. if we want to monitor php7-fpm, we create `checks/php7-fpm.sh`, the main `healthcheck.sh` file will automatically pick it up.

Inside your newly created `.sh` file, you'll need a main function called `check()` to tell it what to do, make sure
to return the correct exit code so that Salutem knows what to do.

### Custom checks

Add in any check you want to the `checks/custom` directory, in order for the main `healthcheck.sh` file to know whether succeeded or not, you will need to `echo 0` for success or `echo 1` for failure.
