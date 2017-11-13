# version

        $ mongod --version



# connect

Connect to local host on default port 27017
        mongo

Connect to remote host on specified port
        mongo --host <hostname or ip address> --port <port no>
        mongo --host 10.121.65.23 --port 23020

Connect to a database
        mongo <host>/<database>
        mongo 10.121.65.58/mydb



# explore

Show current database
	db

Select or switch database [1]

Show all databases
        show dbs

Show all collections in current database
        show collections

Show all users on current database
        show users

Show all roles on current database
        show roles


# manipulate
cheatsheet :

- https://blog.codecentric.de/files/2012/12/MongoDB-CheatSheet-v1_0.pdf
- http://www.opentechguides.com/how-to/article/mongodb/118/mongodb-cheatsheat.html

## count
Simply count objects. The function accepts filters as parameters.

```javascript
        const user_count = await _db.users.count({
          "firstName": {
            $exists : true,
            $ne : ""
          }
        });
        console.log("user_count :" +user_count);
```

## aggregate

Equivalent of groupby clause in SQL.

Count companies by salestype :

        ```javascript
        const company_count = await _db.companies.aggregate({
          "$group" : {
            _id : {salesType:"$salesType"},
            count : { $sum : 1}
          }
        });
        console.log(company_count);
        ```
