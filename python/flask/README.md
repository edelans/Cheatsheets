Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``, ``db``, and the ``User`` model.


Running Tests
-------------

To run all tests, run ::

    python manage.py test


Migrations
----------

* we use flask migrate : https://flask-migrate.readthedocs.io/en/latest/

* change `models.py` on dev
* generate the migration files :
::

    python manage.py db migrate

* The migration scripts are meant to be hand-edited, consider the generated script a starting version. You should always review and correct the generated scripts. Column renames is one example where there is really no safe way for the software to determine that you renamed a column.

* apply the migration on dev
::

    python manage.py db upgrade

* check if everything is OK
* git push to the server (the migration folder MUST be versioned)
* apply the migration on **prod**
::

    python manage.py db upgrade


For a full migration command reference, run ``python manage.py db --help``.


# Flask CLI
----------

` export FLASK_APP=/home/edelans/github/louonsmieux/app/__init__.py`
` export FLASK_APP=/var/www/louonsmieux.com/app/__init__.py`

a mettre dans le script post activate du venv :
` nano ~/.virtualenvs/louonsmieux/bin/postactivate`
