# Salutem ('health' in latin)

A basic healthcheck script for server admins on a budget.

![](https://i.imgur.com/UHA7h7f.gif)

Things like Netdata and Graylog are too RAM hungry for a $5 DigitalOcean box.
This is where Salutem comes into play!

## Installation

```
git clone https://github.com/joereynolds/salutem
cd salutem
./healthcheck
```

## Custom checks

Custom checks should be stored in `~/.config/salutem/checks` (Though can also be stored in `checks/custom` if you prefer).
There are some examples of custom checks in `checks/custom` to get an idea of what you can do.
Basically, as long as you `echo 0` for success and `echo 1` for failure, it will 'just work'.

## Built-in checks

There are a few built-in checks to give you an idea of what is capable. You can `rm` these if they're an annoyance.

If the service you want to check isn't supported, simply add it to the `checks/services` directory.
Inside your newly created check file, you'll need a main function called `check()` to tell it what to do, make sure
to return the correct exit code (0 for success, 1 for failure) so that Salutem knows what to do.

## Inspiration

Cool ideas for Salutem:

### Email it nightly

```
./healthcheck | mail -s "Salutem Healthcheck results" youremailhere@email.com
```

Put this on a cron once a day and you now have a nightly report on the health of your server!
