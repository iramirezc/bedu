# Backend Fundamentals

## Session 03: Servers Administration

List of Content:

* [Pre-Requisites](#Pre-Requisites)
* [SSH](#SSH)
* [Reference](#Reference)

### Pre-Requisites

**1. A GitHub Account:**

Create a [GitHub](https://github.com/) account.

**2. Git:**

Install [Git](https://git-scm.com/) in your local machine.

**3. Docker Community Edition:**

Create a [DockerHub](https://hub.docker.com/) account and install [Docker](https://www.docker.com/) Community Edition.

**4. Pull the `Ubuntu` Docker Image:**

```sh
$ docker pull ubuntu
# it will download the docker image
```

### Secure Shell (SSH)

SSH is a remote administration protocol to connect and manage remote servers over the Internet.

#### Run a Docker container and install your tools

If you don't have `ssh` installed in your local machine, then you can use a docker container to practice the GitHub connection with SSH.

Spin up a `Ubuntu` container:

```sh
$ docker run --name my-ubuntu -it ubuntu bash
# it should run an Ubuntu container and open the container's terminal
root@e7ddfa5be44c:/#
```

Update the __APT__ (_Advanced Package Tool_):

```sh
$ apt-get update
# it should update the packages lists
```

##### Installing SSH

Install SSH inside the container using `apt-get`:

```sh
$ apt-get install openssh-server
# it should download and install the ssh client
```

Test the `ssh` installation:

```sh
$ ssh
# usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-b bind_address] [-c cipher_spec]
# ...
```

##### Installing Git

Install Git inside the container:

```sh
$ apt-get install git
# it should download and install git
```

##### Installing VIM

Install VIM inside the container:

```sh
$ apt-get install vim
# it should download and install vim
```

#### Connecting to GitHub with SSH

You can run these commands in your local machine to persists your SSH keys or within the docker container as an exercise.

Check for existing SSH Keys:

```sh
$ ls -al ~/.ssh
# it should show .pub files if they exists
```

Generate a new SSH key:

```sh
$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
# Generating public/private rsa key pair.
# Enter file in which to save the key (/root/.ssh/id_rsa):
# Enter passphrase (empty for no passphrase):
# ...
```

Start the `ssh-agent` in the background:

```sh
$ eval "$(ssh-agent -s)"
# Agent pid 14
```

Add your SSH key to the `ssh-agent`:

```sh
$ ssh-add ~/.ssh/id_rsa
# Identity added: /root/.ssh/id_rsa (your_email@example.com)
```

Copy the SSH key:

```sh
$ cat ~/.ssh/id_rsa.pub
# ssh-rsa AAAAB3NzaC1yc2EAAAADAQABA... your_email@example.com
# select & copy the ssh key
```

Go to your GitHub Account:

* Click on your profile
* Select __Settings__
* Click on __SSH and GPG keys__ from the left menu
* Click the button __New SSH key__
* Type a title
* Paste the SSH key
* Click the button __Add SSH key__
* You may be prompted for your password.

Test your SSH connection:

```sh
$ ssh -T git@github.com
# The authenticity of host 'github.com (x.x.x.x)' can't be established.
# RSA key fingerprint is SHA256:nThb........................
# Are you sure you want to continue connecting (yes/no)? yes
# Warning: Permanently added 'github.com,x.x.x.x' (RSA) to the list of known hosts.
# Hi your_username! You've successfully authenticated, but GitHub does not provide shell access.
```

Congratulations! You're all set!

#### Configure your Git identity

Check if you have your `name` and `email` configured in Git:

```sh
$ git config --global user.name
# Your Name
$ git config --global user.email
# your_email@example.com
```

Alternatively you can issue:

```sh
$ git config --list
# user.name=Your Name
# user.email=your_email@example.com
```

Set your `name`:

```sh
$ git config --global user.name "Your Name"
# it should update your username
```

Set your `email`:

```sh
$ git config --global user.email "your_email@example.com"
# it should update your email
```

#### Pushing a repository to GitHub using SSH

Create a `test-ssh` directory inside `/usr/src`:

```sh
$ mkdir /usr/src/test-ssh
# it should create the directory
```

Change to the `test-ssh` directory:

```sh
$ cd /usr/src/test-ssh && pwd
# /usr/src/test-ssh
```

Initialize a new Git repository:

```sh
$ git init
# Initialized empty Git repository in /usr/src/test-ssh/.git/
```

Create a `README.md` file inside the `test-ssh` directory using VIM with the following content:

```txt
# test-ssh

This is a repository to test my SSH connection to my GitHub account.
```

Check the content of your file:

```sh
$ cat README.md
# it should show the content of your file
```

Add your `README.md` file to the working tree:

```sh
$ git add README.md
# it should add the README.md file to be committed
```

Check the status of tour working tree:

```sh
$ git status
# On branch master
# No commits yet
# Changes to be committed:
#    (use "git rm --cached <file>..." to unstage)
#         new file:   README.md
```

Commit your changes:

```sh
$ git commit -m "first commit"
# [master (root-commit) de179bc] first commit
#  1 file changed, 3 insertions(+)
#  create mode 100644 README.md
```

Check your git logs:

```sh
$ git log
# commit de179bc7359fe83373574736dcf3132dd208b6d4 (HEAD -> master)
# Author: Your Name <your_email@example.com>
# Date:   Fri Jan 31 08:57:57 2020 +0000
#     first commit
```

Create a new repository in your GitHub account:

* Click on the `+` button next to your profile
* Select __New repository__ from the drop down
* Give your repository a name: `test-ssh`
* Click the button __Create repository__

Push your existing repository from the command line:

```sh
$ git remote add origin git@github.com:iramirezc/test-ssh.git
# it should add your GitHub repo as a remote to your local repository.
$ git push -u origin master
# it should push your local master branch to your remote master branch.
```

Refresh the page of your GitHub repository in your browser.

Congratulations! You have pushed your first repository to a remote server!

Now you can check the status of your SSH key:

* Click on your profile
* Select __Settings__
* Click on __SSH and GPG keys__ from the left menu
* Validate that your SSH key now says when it was the last time it was used in green color.

### Reference

* [Ubuntu Docker Image - DockerHub](https://hub.docker.com/_/ubuntu/)
* [Connecting to GitHub with SSH - GitHub Help](https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)
* [First-Time Git Setup - Git Docs](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
* [How does SSH Work - Article](https://www.hostinger.com/tutorials/ssh-tutorial-how-does-ssh-work)
