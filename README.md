# Salutem ('health' in latin)

A basic healthcheck script for server admins on a budget.

![](https://i.imgur.com/lAkomtC.gif)

Things like Netdata and Graylog are too RAM hungry for a $5 DigitalOcean box.
This is where Salutem comes into play!

## Adding checks

### Services

If the service you want to check isn't supported, simply add it to the `checks/services` directory with the name of the service.
i.e. if we want to monitor php7-fpm, we create `checks/services/php7-fpm.sh`, the main `healthcheck.sh` file will automatically pick it up.

Inside your newly created `.sh` file, you'll need a main function called `check()` to tell it what to do, make sure
to return the correct exit code so that Salutem knows what to do.

### Custom checks

Custom checks should be stored in `~/.config/salutem/checks` (Though can also be stored in `checks/custom` if you prefer).
There are some examples of custom checks in `checks/custom` to get an idea of what you can do.
Basically, as long as you `echo 0` for success and `echo 1` for failure, it will 'just work'.
