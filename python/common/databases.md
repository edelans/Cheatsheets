# SQlite

## Initialize

To use the module, you must first create a Connection object that represents the database. Here the data will be stored in the example.db file:

```python
        import sqlite3
        conn = sqlite3.connect('example.db')
```

## Query

Once you have a Connection, you can create a Cursor object and call its execute() method to perform SQL commands:

```python
        c = conn.cursor()

        # Create table
        c.execute('''CREATE TABLE stocks
                     (date text, trans text, symbol text, qty real, price real)''')

        # Insert a row of data
        c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

        # Save (commit) the changes
        conn.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        conn.close()
```

## MitigateSQL injections

```python
        # Never do this -- insecure!
        symbol = 'RHAT'
        c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

        # Do this instead
        t = ('RHAT',)
        c.execute('SELECT * FROM stocks WHERE symbol=?', t)
        print(c.fetchone())

        # Larger example that inserts many records at a time
        purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
                     ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
                     ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
                    ]
        c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
```


## Retrieve data

To retrieve data after executing a SELECT statement, you can either

* treat the cursor as an iterator,
* call the cursor’s fetchone() method to retrieve a single matching row,
* or call fetchall() to get a list of the matching rows.

This example uses the iterator form:

```python
        for row in c.execute('SELECT * FROM stocks ORDER BY price'):
            print(row)
```
