from .base import *  # noqa
import os

CALLBACK_HOST = 'b90fa9f1.ngrok.io'
ALLOWED_HOSTS = ['.ngrok.io', '127.0.0.1', 'localhost', CALLBACK_HOST]

DEBUG = True

ADMINS = (
    ('edelans', 'username@yourdomain.com'),
)


MANAGERS = ADMINS

# needed to define callbackUrl for webhooks

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'trelloweb',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}

# You might want to use sqlite3 for testing in local as it's much faster.
if IN_TESTING:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/tmp/trellowatch_test.db',
        }
    }

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    ] + MIDDLEWARE

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]



SOCIAL_AUTH_TRELLO_KEY = '81f3812822bb14b2bf02ce18c5162f4e'
SOCIAL_AUTH_TRELLO_SECRET = '5c90b09fb2fd71906ec9c1d7a44684697319d2b4646a068ea44f51c8d3b46f0f'
SOCIAL_AUTH_TRELLO_APP_NAME = 'TrelloWatch'
