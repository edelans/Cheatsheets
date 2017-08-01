from .base import *  # noqa
import os

# activate with export DJANGO_SETTINGS_MODULE="trellowatch.settings.production"

DEBUG = False

CALLBACK_HOST = 'trello.edelans.com'
ALLOWED_HOSTS = [CALLBACK_HOST]

SECRET_KEY = "pundbdYW6FKgbSNuS8pC4RcG2UWNQ2gp"

ADMINS = (
    ('edelans', 'edelans@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'trellowatch',
        'USER': 'deploy',
        'PASSWORD': 'syVQgKkGXeQghVW7ajsYpmWqBpRR8aX7',
        'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}


SOCIAL_AUTH_TRELLO_KEY = '81f3812822bb14b2bf02ce18c5162f4e'
SOCIAL_AUTH_TRELLO_SECRET = '5c90b09fb2fd71906ec9c1d7a44684697319d2b4646a068ea44f51c8d3b46f0f'
SOCIAL_AUTH_TRELLO_APP_NAME = 'TrelloWatch'


# Email config
# test with :
# from django.core.mail import send_mail
# send_mail('<Test email from Django>', '<it\'s up>', 'deploy@edelans.com', ['edelans@gmail.com'])
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'Trellowatch <deploy@edelans.com>'
