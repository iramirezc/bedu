# Backend Fundamentals

## Session 03: Servers Administration

List of Content:

* [Pre-Requisites](#Pre-Requisites)
* [Secure Shell (SSH)](#Secure-Shell-(SSH))
* [Node.js Package Manager (NPM)](#Node.js-Package-Manager-(NPM))
* [Reference](#Reference)

---

### Pre-Requisites

#### Services Accounts

* Create a [GitHub](https://github.com/) account
* Create a [DockerHub](https://hub.docker.com/) account

#### Software Required

* [Git](https://git-scm.com/)
* [Docker](https://www.docker.com/)
* [Visual Studio Code](https://code.visualstudio.com/)

#### Docker Images

* Pull the [Ubuntu Docker Image](https://hub.docker.com/_/ubuntu/)

---

### Secure Shell (SSH)

SSH is a remote administration protocol to connect and manage remote servers over the Internet.

#### Run a Docker container and install your tools

If you don't have `ssh` installed in your local machine, then you can use a docker container to practice the GitHub connection with SSH.

Spin up a `Ubuntu` container:

```sh
# local machine
$ docker run --name my-ubuntu -it ubuntu bash
# it should run an Ubuntu container and open the container's terminal
# root@e7ddfa5be44c:/#
```

Update the __APT__ (_Advanced Package Tool_):

```sh
# my-ubuntu container
$ apt-get update
# it should update the packages lists
```

##### Installing SSH

Install SSH inside the container using `apt-get`:

```sh
# my-ubuntu container
$ apt-get install openssh-server
# it should download and install the ssh client
```

Test the `ssh` installation:

```sh
# my-ubuntu container
$ ssh
# usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-b bind_address] [-c cipher_spec]
# ...
```

##### Installing Git

Install Git inside the container:

```sh
# my-ubuntu container
$ apt-get install git
# it should download and install git
```

##### Installing VIM

Install VIM inside the container:

```sh
# my-ubuntu container
$ apt-get install vim
# it should download and install vim
```

##### Installing cURL

Install cURL inside the container:

```sh
# my-ubuntu container
$ apt-get install curl
# it should download and install curl
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

---

### Node.js Package Manager (NPM)

NPM is the package manager for Node.js packages and modules.

#### Creating a web server with Express.js

We will use NPM to download the `Express.js` framework and build a web server.

Pull the docker image `node:12.14.1-alpine3.9`

```sh
# local machine
$ docker pull node:12.14.1-alpine3.9
# 12.14.1-alpine3.9: Pulling from library/node
# ...
# Status: Downloaded newer image for node:12.14.1-alpine3.9
```

Run a container using the `sh` terminal.

> _Note: The node's alpine version does NOT include the `bash` terminal_.

```sh
# local machine
$ docker run --name my-server -it -p 0.0.0.0:8080:8080 node:12.14.1-alpine3.9 sh
# now you should be inside the container's shell
```

Create a `server` folder inside the container's `/usr` directory:

```sh
# my-server container
$ mkdir /usr/server && cd /usr/server
# it should create and enter the server directory
# /usr/server
```

Initialize a npm module:

```sh
# my-server container
$ npm init
# it should start a wizard to create the npm module
```

Complete the wizard:

```sh
package name: (server)
version: (1.0.0)
description: A basic express.js web server
entry point: (index.js) server.js
test command:
git repository:
keywords:
author: Your Name <your_email@example.com>
license: (ISC)
```

Now should you have a `package.json` file:

```sh
# my-server container
$ ls
# package.json
```

See the content of your `package.json` file:

```sh
# my-server container
$ cat package.json
{
  "name": "server",
  "version": "1.0.0",
  "description": "A basic express.js web server",
  "main": "server.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "Your Name <your_email@example.com>",
  "license": "ISC"
}
```

Install `express` from NPM:

```sh
# my-server container
$ npm install express
# added 50 packages from 37 contributors and audited 126 packages in 5.537s
```

Inspect your `package.json` file again, you should have `express` installed as a dependency:

```sh
# package.json
{
  ...
  "dependencies": {
    "express": "^x.x.x"
  }
}
```

Create a `server.js` file in your **local** machine with the following code:

```js
const express = require('express')
const server = express()
const port = 8080

server.get('/', (req, res) => {
  res.send({ message: 'Hello from Express server' })
})

server.listen(port, () => {
  console.log(`Server listening on port ${port}...`)
})
```

Copy the `server.js` file from your **local** machine to the container's path `/usr/server`:

```sh
# local machine
$ docker cp server.js my-server:/usr/server
# it should copy the server.js to the container
```

Go back to the container's terminal and run:

```sh
# my-server container
$ node server.js
# Server listening on port 8080...
```

Test the connection to the Express server.

##### Alternative 1: Using a Web Browser

Open the following url `localhost:8080` in the web browser of your preference. You should receive a JSON response:

```json
{ "message": "Hello from Express server" }
```

##### Alternative 2: Using `curl` from your local machine

If you have `curl` installed in your **local** machine run:

```sh
# local machine
$ curl localhost:8080
# {"message":"Hello from Express server"}
```

##### Alternative 3: Using `curl` from another docker container

You can use the previous `my-ubuntu` container to make a request to the `my-server` container.

First, you will need to [install curl](#Installing-cURL) into the `my-ubuntu` container. Then, you will need to know in which IP address `my-server` is running:

```sh
# local machine
$ docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-server
# 172.17.0.2
# Note: (IP address may vary)
```

Finally, inside the `my-ubuntu` container run the `curl` command using the IP address you retrieve from the previous step:

```sh
# my-ubuntu container
$ curl 172.17.0.2:8080
# {"message":"Hello from Express server"}
```

Congratulations! You have created your first npm module!

---

### Reference

#### Git & GitHub

* [Connecting to GitHub with SSH - GitHub Help](https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)
* [First-Time Git Setup - Git Docs](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

#### SSH

* [How does SSH Work - Hostinger](https://www.hostinger.com/tutorials/ssh-tutorial-how-does-ssh-work)

#### Docs

* [NPM](https://www.npmjs.com/)
* [Express.js](https://expressjs.com/)
* [express - npm](https://www.npmjs.com/package/express)
* [How To Use - curl](https://curl.haxx.se/docs/manpage.html)
