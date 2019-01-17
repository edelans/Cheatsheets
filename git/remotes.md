


# View existing remotes

```bash
git remote -v
```

# Change remote name from 'origin' to 'destination'

```bash
git remote rename origin destination
```

# Change your remote's URL

```bash
git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
```

prefer the `git@github.com:` over the `https://` to leverage auth with ssh key.


# Set a new remote

```bash
git remote add origin git@github.com:user/repo.git
```

# Remove a remote

```bash
git remote rm destination
```
