

see https://pyformat.info/


New style :
    '{} {}'.format('one', 'two')

Output
    one two


Alongside of format, Python 3.6+ offers a flexible way to do string interpolation via [f-strings](https://www.python.org/dev/peps/pep-0498/).


    user = "Jane Doe"
    action = "buy"
    log_message = f'User {user} has logged in and did an action {action}.'
    print(log_message)
    # User Jane Doe has logged in and did an action buy.
