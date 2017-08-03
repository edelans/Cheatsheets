# goal : deploy in one command

The goal is to be able to deploy with a simple push to the git repo hosted on the server (the `live` remote):

```git push live master```


## On the server (example.com)

1. Create a user on `example.com`, as which we (the git client) connect (push) to `exmaple.com`.
  We set `git-shell` as the login shell, so it is not possible to interactively login as this user.
  ```bash
  sudo useradd -m -s /usr/bin/git-shell git
  ```

2. Add your ssh public key to the `authorized_keys` file of the created user:
  ```bash
  ## Because user git can not interactively login, we have to use sudo to get git temporarily
  sudo -u git bash
  cd ~
  ## cd /home/git
  mkdir -p .ssh
  vim .ssh/authorized_keys
  ## Paste your public key and save
  ```

3. Create a `git bare` repo for your project:

        mkdir /var/repo/trellowatch.git && cd "$_"
        git init --bare


4. Copy the `post-receive` script from this gist to the `hooks` dir of the created bare repo.
  ```bash
  nano /var/repo/trellowatch.git/hooks/post-receive
  ## Paste the post-receive script from this gist and save
  ## If you do not need to execute a 'build' and/or 'restart' command,
  ## just delete or comment the lines 'UPDATE_CMD' and 'RESTART_CMD'
  chmod +x /var/repo/trellowatch.git/hooks/post-receive
  ```

5. Set ownership and permissions of the `DEPLOY_ROOT` directory:
  ```bash
  sudo chown root:git -R /var/repo/
  sudo chmod 775 /var/repo/
  ```


## On the client

add our newly created `remote`:
        git remote add live ssh://deploy@eiffel:/var/repo/trellowatch.git

## Git hook

dans `/var/repo/trellowatch.git/hooks/post-receive` :


```
#!/bin/bash
set -eu

TARGET="/var/www/trellowatch"
GIT_DIR="/var/repo/trellowatch.git"
BRANCH="master"

while read oldrev newrev ref
do
        # only checking out the master (or whatever branch you would like to deploy)
        if [[ $ref = refs/heads/"$BRANCH" ]];
        then
                echo "Ref $ref received. Deploying ${BRANCH} branch to production..."
                git --work-tree="$TARGET" --git-dir="$GIT_DIR" checkout -f "${BRANCH}"
                cd "$TARGET"
                sh post-receive.sh
        else
                echo "Ref $ref received. Doing nothing: only the ${BRANCH} branch may be deployed on this server."
        fi
done

```

## Post-receive script :

post-receive.sh

```
#!/bin/bash
#This script is exectuted by the post-receive hook
#it contains commands that must be executed when code is pulled

# some colors
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo  "\n${YELLOW}##########################################${NC}"
echo  "${YELLOW}#    Exectution post-receive.sh script   #${NC}"
echo  "${YELLOW}##########################################${NC}"

# activate virtual env
echo  "\n\n${YELLOW}activate virtual env${NC}"
. ~/.virtualenvs/trellowatch/bin/activate

# install new requirements with pip
echo "\n\n${YELLOW}install new requirements with pip (quiet mode)${NC}"
pip install -r requirements.txt -q

# install new front libs with bower
echo "\n\n${YELLOW}install new front libs with bower${NC}"
bower install

# collectstatic
echo "\n\n${YELLOW}run collectstatic${NC}"
python manage.py collectstatic  --noinput

# restart app
echo "\n\n${YELLOW}restart app${NC}"
sudo systemctl restart trellowatch
```


# Going further
See a more generic version @ https://gist.github.com/thomasfr/9691385 (use of makefile for post-receive.sh for instance)
