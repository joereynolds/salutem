# Salutem ('health' in latin)

A basic healthcheck script for servers.

![](https://i.imgur.com/wNUgVlO.gif)


## Adding checks

### Services

If the service you want to check isn't supported, simply add it to the `checks/services` directory with the name of the service.
i.e. if we want to monitor php7-fpm, we create `checks/services/php7-fpm.sh`, the main `healthcheck.sh` file will automatically pick it up.

Inside your newly created `.sh` file, you'll need a main function called `check()` to tell it what to do, make sure
to return the correct exit code so that Salutem knows what to do.

### Custom checks

Add in any custom checks you want to the `checks/custom` directory (There are 2 example ones to get you started), in order for the main `healthcheck.sh` file to know whether succeeded or not, you will need to `echo 0` for success or `echo 1` for failure.
