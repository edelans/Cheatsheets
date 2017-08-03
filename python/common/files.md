
#Common files read/write

The modes are:

* ‘r’ – Read mode which is used when the file is only being read
* ‘w’ – Write mode which is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated)
* ‘a’ – Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end
* ‘r+’ – Special read and write mode, which is used to handle both actions when working with a file


## Read
```python
with open(“hello.text”, “r”) as f:
  data = f.readlines()

  for line in data:
    words = line.split()
    print(words)
```

## Write

```python
with open(“hello.txt”, “w”) as f:
  f.write(“Hello World”)
```


# CSV files

use the [csv module](https://docs.python.org/3.5/library/csv.html)
