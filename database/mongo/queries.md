# aggregate

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

# count
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
