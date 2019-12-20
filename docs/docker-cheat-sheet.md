# Docker Cheat Sheet

## General Purpose

### Docker version

Usage:

```sh
docker --version
```

Example:

```sh
$ docker --version
# Docker version 19.03.2, build 6a30dfc
```

### Docker help

Usage:

```sh
docker --help
```

Example:

```sh
$ docker --help
# Usage: docker [OPTIONS] COMMAND
```

### Docker help for a command

Usage:

```sh
docker COMMAND --help
```

Example:

```sh
$ docker run --help
# Usage: docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
# Run a command in a new container
```

### Docker Hello World

Usage:

```sh
docker run hello-world
```

Example:

```sh
$ docker run hello-world
# Unable to find image 'hello-world:latest' locally
# latest: Pulling from library/hello-world
# 1b930d010525: Pull complete
# Digest: sha256:4fe721ccc2e8dc7362278a29dc660d833570ec2682f4e4194f4ee23e415e1064
# Status: Downloaded newer image for hello-world:latest

# Hello from Docker!
# This message shows that your installation appears to be working correctly.
```

## Docker Images

### Download an Image or a Repository

Usage:

```sh
docker pull IMAGE[:TAG]
```

Example:

```sh
$ docker pull mariadb:10.4
# 10.4: Pulling from library/mariadb
# ...
# Status: Downloaded newer image for mariadb:10.4
```

### List all your downloaded Images

Usage:

```sh
docker image ls
```

Example:

```sh
$ docker image ls
# REPOSITORY   TAG    IMAGE ID       CREATED      SIZE
# mariadb      10.4   e93d99aa9076   4 days ago   355MB
```

### Remove an Image

Usage:

```sh
docker image rm IMAGE[:TAG]
```

Example:

```sh
$ docker image rm mariadb:10.4
# Untagged: mariadb:10.4
# Untagged: mariadb@sha256:a62bf6dd62bf71f1fa66887b1d3e0a9d6a7583e6a5ff08df4e53f4451d2c1571
# Deleted: sha256:e93d99aa9076c3582e36fd458be51d2d389cf421b711f03b8767f156be4d2cfb
# ...
```

## Docker Volumes

### Create a Volume

Usage:

```sh
docker volume create --name=NAME
```

Example:

```sh
$ docker volume create --name=mariadb_data
# mariadb_data
```

### List all your Volumes

Usage:

```sh
docker volume ls
```

Example:

```sh
$ docker volume ls
# DRIVER              VOLUME NAME
# local               mariadb_data
```

### Remove a Volume

Usage:

```sh
docker volume rm NAME
```

Example:

```sh
$ docker volume rm mariadb_data
# mariadb_data
```

## Docker Containers

### Run a Container from a Docker Image

Usage:

```sh
docker run [OPTIONS] IMAGE[:TAG] [COMMAND]
```

Options:

> `--name NAME` Container's name.
>
> `-v VOLUME:CONTAINER_PATH` Bind mount a volume.
>
> `-p HOST_PORT:CONTAINER_PORT` Publish a container's port(s) to the host.
>
> `-e KEY=VAL` Set environmental variables.
>
> `-d` Run container in background.
>
> `--rm` Automatically remove the container when it exits
>
> `-it` Interactive & pseudo-TTY.
>
> `--network NETWORK_NAME` Connect the container to a network.

Example 1: Launching a MariaDB Server

```sh
$ docker run --name mariadb_server -v mariadb_data:/var/lib/mysql -p 0.0.0.0:3306:3306 -e MYSQL_ROOT_PASSWORD=secret -d mariadb:10.3
# 6706d3d7066b8797f88f09ea86a04237d592e01d95bf70f153aed4511f80768b
```

Example 2: Running a temporary container to connect to the MariaDB server.

```sh
$ docker run --rm -it --network mariadb-server_default mariadb:10.3 mysql -h192.168.16.2 -uroot -p
# Enter password:
# Welcome to the MariaDB monitor. Commands end with ; or \g.
# ...
MariaDB [(none)]>
```

### List all running Containers

Usage:

```sh
docker ps
```

Example:

```sh
$ docker ps
# CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                    NAMES
# 6706d3d7066b   mariadb:10.3   "docker-entrypoint.s…"   33 seconds ago   Up 32 seconds   0.0.0.0:3306->3306/tcp   mariadb_server
```

### List all Containers including the stopped ones

Usage:

```sh
docker ps -a
```

Example:

```sh
$ docker ps -a
# CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS                            PORTS   NAMES
# 6706d3d7066b   mariadb:10.3   "docker-entrypoint.s…"   3 minutes ago   Exited (0) About a minute ago             mariadb_server
```

### Inspect a Container

Usage:

```sh
docker inspect [OPTIONS] CONTAINER
```

Options:

> `-f` Format the output using the given Go template

Example 1: Shows all information about the Docker object.

```sh
$ docker inspect mariadb_server
# ...
# "NetworkSettings": {
#   ...
#   "Networks": {
#     "mariadb-server_default": {
#       ...
#       "IPAddress": "192.168.16.2",
# ...
```

Example 2: Shows only the IP address.

```sh
$ docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mariadb_server
# 192.168.16.2
```

### Stop a running Container

Usage:

```sh
docker stop CONTAINER
```

Example:

```sh
$ docker stop mariadb_server
# mariadb_server
```

### Start an stopped Container

Usage:

```sh
docker start CONTAINER
```

Example:

```sh
$ docker start mariadb_server
# mariadb_server
```

### Restart a container

Usage:

```sh
docker restart CONTAINER
```

Example:

```sh
$ docker restart mariadb_server
# mariadb_server
```

### Remove an stopped Container

Usage:

```sh
docker rm CONTAINER
```

Example:

```sh
$ docker rm mariadb_server
# mariadb_server
```

### Execute a command inside a Container

Usage:

```sh
docker exec [OPTIONS] CONTAINER COMMAND [ARGUMENTS...]
```

Options:

> `-i` Interactive. Keep STDIN open even if not attached.
>
> `-t` Allocate a pseudo-TTY

Example:

```sh
$ docker exec -it mariadb_server mysql -p
# Enter password:
# Welcome to the MariaDB monitor. Commands end with ; or \g.
# ...
MariaDB [(none)]>
```

## Other Resources

* [Use the Docker command line](https://docs.docker.com/engine/reference/commandline/cli/)
