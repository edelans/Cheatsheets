
# Generate a SHA1 hash

Generate the SHA1 of the string `password` :

```bash
echo -n password | sha1sum | awk '{print $1}'
```
