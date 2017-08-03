use template : https://github.com/pydanny/cookiecutter-django

# Start new django project and app
$ django-admin.py startproject mysite
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py startapp watcher

# Run Django
$ python manage.py shell
$ python manage.py runserver

# django migration
$ python manage.py makemigrations watcher
$ python manage.py sqlmigrate watcher 0001
$ python manage.py migrate
$ python manage.py squashmigrations watcher 0004

# django database backup & restore
$ python manage.py dumpdata --indent 2 --exclude auth.permission --exclude contenttypes > db.json
$ python manage.py loaddata db.json

# sqlite3
$ sqlite3 db.sqlite3
sqlite> .tables

# test
from django.test.utils import setup_test_environment
setup_test_environment()
$ python manage.py test watcher

# assets
$ python manage.py collectstatic
