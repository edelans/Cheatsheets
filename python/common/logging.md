#!/usr/bin/env python

"""
## logging
Standard way to output error messages.
Advantages:
- has many useful built-in error formats
- has a level system
- easy to change where logs go, e.g. a file.
https://docs.python.org/3.5/howto/logging.html

"""


import logging


logging.basicConfig(
    # Log to a file. Default is sys.stderr.
    # This can only take file path strings.
    # To log to stdout, use:
    #filename = 'example.log',
    # Mode defaults to `a`, which appends to old log.
    #filemode = 'w'

    # Minimum log level that will get printed.
    # Often taken as a CLI parameter.
    level = logging.DEBUG,
    #level = logging.INFO,
    #level = logging.WARNING,
    #level = logging.ERROR,
    #level = logging.CRITICAL,

    # Default does not contain time, so you very likely want to override this.
    format = '  %(levelname)s %(asctime)s %(message)s',

    # Format for asctime
    datefmt = '%m/%d/%Y %I:%M:%S %p',
)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
