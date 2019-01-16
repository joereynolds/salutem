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

Inside your newly created check file, you'll need a main function called `check()` to tell it what to do. Make sure
to throw an `Exception` for failure so that Salutem knows what to do.

A check can also contain a `name` variable. This is a friendly name for the
check instead of the default filepath of the check.

There are some examples of custom checks in `checks/custom` to get an idea of what you can do.
As long as you throw an `Exception` when it fails, it will 'just work'.

## Built-in checks

There are a few built-in checks to give you an idea of what is capable. You can `rm` these if they're an annoyance.

## Contributing

### Running the tests   

```
python3 -m unittest discover -v
```
## Inspiration

Cool ideas for Salutem:

### Email it nightly

```
./healthcheck | mail -s "Salutem Healthcheck results" youremailhere@email.com
```

Put this on a cron once a day and you now have a nightly report on the health of your server!

![Imgur](https://i.imgur.com/nSkbUNH.png)
