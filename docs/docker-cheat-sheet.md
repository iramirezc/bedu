# Docker Cheat Sheet

## General Purpose

### Docker version

```sh
docker --version
```

> Example

```sh
$ docker --version
# Docker version 19.03.2, build 6a30dfc
```

### Docker help

```sh
docker --help
```

> Example

```sh
$ docker --help
# Usage: docker [OPTIONS] COMMAND
```

### Docker help for a command

```sh
docker COMMAND --help
```

> Example

```sh
$ docker run --help
# Usage: docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
# Run a command in a new container
```

### Docker Hello World

```sh
docker run hello-world
```

> Example

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

### Download a Docker Image or a Repository

```sh
docker pull IMAGE[:TAG]
```

> Example

```sh
$ docker pull mariadb:10.4
# 10.4: Pulling from library/mariadb
# ...
# Status: Downloaded newer image for mariadb:10.4
```

### List all your downloaded Docker Images

```sh
docker image ls
```

> Example

```sh
$ docker image ls
# REPOSITORY   TAG    IMAGE ID       CREATED      SIZE
# mariadb      10.4   e93d99aa9076   4 days ago   355MB
```

### Remove a Docker Image

```sh
docker image rm IMAGE[:TAG]
```

> Example

```sh
$ docker image rm mariadb:10.4
# Untagged: mariadb:10.4
# Untagged: mariadb@sha256:a62bf6dd62bf71f1fa66887b1d3e0a9d6a7583e6a5ff08df4e53f4451d2c1571
# Deleted: sha256:e93d99aa9076c3582e36fd458be51d2d389cf421b711f03b8767f156be4d2cfb
# ...
```

## Docker Volumes

### Create a Docker Volume

```sh
docker volume create --name=NAME
```

> Example

```sh
$ docker volume create --name=mariadb_data
# mariadb_data
```

### List all your Docker Volumes

```sh
docker volume ls
```

> Example

```sh
$ docker volume ls
# DRIVER              VOLUME NAME
# local               mariadb_data
```

### Remove a Docker Volume

```sh
docker volume rm NAME
```

> Example

```sh
$ docker volume rm mariadb_data
# mariadb_data
```
