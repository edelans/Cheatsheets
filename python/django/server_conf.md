# Server configuration

https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04



gunicorn.service
```
[Unit]
Description=gunicorn daemon for trellowatch app
After=network.target

[Service]
User=deploy
Group=www-data
WorkingDirectory=/var/www/trellowatch
Environment=PATH=/home/deploy/.virtualenvs/trellowatch/bin
Environment=DJANGO_SETTINGS_MODULE=trellowatch.settings.production
ExecStart=/home/deploy/.virtualenvs/trellowatch/bin/gunicorn --pid /tmp/pid-gunicorn --workers 3 --bind 127.0.0.1:8000 trellowatch.wsgi:application
Restart=always

[Install]
WantedBy=multi-user.target
```


nginx.conf

```
server {
    listen 80;
    server_name trello.edelans.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /var/www/trellowatch/;
    }

    location / {
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_pass http://127.0.0.1:8000;
    }
}
```

trellowatch.service

```
[Unit]
Description=gunicorn daemon for trellowatch app
After=network.target

[Service]
User=deploy
Group=www-data
WorkingDirectory=/var/www/trellowatch
ExecStart=/home/deploy/.virtualenvs/trellowatch/bin/gunicorn --workers 1 --bind 127.0.0.1:8000 trellowatch.wsgi:application

[Install]
WantedBy=multi-user.target
```
