# use systemd
systemd is an init system used manage processes, like gunicorn. It will launch gunicorn at server start, and respawn it when it fails.

## Configuration
A service configuration file is provided at the root of this repo. It should be stored in `/etc/systemd/system/`.

## Logs consultation
Make use of `journalctl`. It will show the logs of gunicorn, which receive the logs Django sends to the console (depending on you logger config).

You can filter by :

- time : `journalctl --since 09:00 --until "1 hour ago"`, `journalctl --since "2015-01-10" --until "2015-01-11 03:00"`, `journalctl --since yesterday --until today`

- by service : `journalctl -u nginx.service`, journalctl -u trellowatch.service

- as you go (like `tail -f`) : `journalctl -f`

## Logs cleaning

- to keep only 1G of logs : `sudo journalctl --vacuum-size=1G`
- to keep entries from the last year : `sudo journalctl --vacuum-time=1years`
