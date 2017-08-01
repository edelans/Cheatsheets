# Settings

The settings folder is a python module. The module is loaded by the `manage.py` script and the `wsgi.py` script, according to the variable `DJANGO_SETTINGS_MODULE`, which is set by default to `trellowatch.settings` (which includes `base.py` and `local.py` files) if no environment variable is found.

To set an environment variable :

```
export DJANGO_SETTINGS_MODULE="trellowatch.settings.production"
export DJANGO_SETTINGS_MODULE="trellowatch.settings.local"
```

The standard way for permanently store global environment variables (system wide) is to add an entry in `/etc/environment`

NB: beware, env variables must be defined in the wsgi.py file.


Content of manage.py :

```
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trellowatch.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
```
