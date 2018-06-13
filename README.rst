.. image:: https://github.com/FFY00/discord-github-release-notifier/raw/master/logo.png

=======================
Discord Github Release Notifier
=======================

.. image:: https://img.shields.io/github/release/FFY00/discord-github-release-notifier.svg
    :alt: latest release
    :target: http://github.com/FFY00/discord-github-release-notifier/releases
.. image:: https://img.shields.io/pypi/v/discord-github-release-notifier.svg
    :alt: latest release
    :target: https://pypi.org/project/discord-github-release-notifier/
    
This a fork of `femtopixel <https://github.com/femtopixel>`_'s `Github Release Notifier <https://github.com/femtopixel/github-release-notifier>`_ with the notifications adapted to Discord.

Installation
------------

.. code::

    pip3 install discord-github-release-notifier

Usage
-----

.. code::

    usage: discord-github-release-notifier [-h] [--action {cron,subscribe,unsubscribe}]
                  [--package PACKAGE] [--webhook WEBHOOK] [--uuid UUID]

    optional arguments:
      -h, --help            show this help message and exit
      --action {cron,subscribe,unsubscribe}, -a {cron,subscribe,unsubscribe}
                            Action to do (default: cron)
      --package PACKAGE, -p PACKAGE
                            Github package name / url (required for
                            subscribe/unsubscribe) - prints uuid on subscription
      --webhook WEBHOOK, -w WEBHOOK
                            URL to your webhook (required for
                            subscribe/unsubscribe)
      --uuid UUID, -u UUID  UUID of your webhook (required for unsubscribe)

Example
~~~~~~~

First, I register my webhook :

.. code::

    discord github-release-notifier --action subscribe --webhook https://discordapp.com/api/webhooks/{webhook.id}/{webhook.token} --package jaymoulin/google-music-manager

an UUID is printed. this UUID will be required to unsubscribe the webhook.

When `jaymoulin/google-music-manager` releases a new version, `https://discordapp.com/api/webhooks/{webhook.id}/{webhook.token}` will be called with the release details.

For this to happen, the system should check if a new version have been released.
We can do that by calling `discord-github-release-notifier` without any parameter or setting `--action` to `cron` (which is default).

To automate this process, we could add this process in a cronjob:

.. code::

    (crontab -l ; echo "0 0 * * * discord-github-release-notifier") | sort - | uniq - | crontab -

This will check every day at midnight if new versions have been released.

Submitting bugs and feature requests
------------------------------------

Bugs and feature request are tracked on GitHub

Author
------

Jay MOULIN jaymoulin+github-release-notifier@gmail.com See also the list of contributors which participated in this program.
Filipe LAÍNS filipe.lains@gmail.com (adaptatiion to discord)

License
-------

Discord Github Release Notifier is licensed under the MIT License

