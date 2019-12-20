# Data Analysis

## Session 05: MongoDB Fundamentals (with Docker)

### Pre-Requisites

**1. Install Docker:**

[How to install Docker Community Edition](../docs/docker-installation.md)

**2. Pull the Mongo Docker Image from Docker Hub:**

```sh
docker pull mongo:4.0
```

### Docker Volumes

#### Create a Docker Volume

We need a Docker Volume to **NOT** lost the data we store in the database when working with containers because containers can be removed and created multiple times.

```sh
$ docker volume create --name=bedu_mongodb_data
# bedu_mongodb_data
```

#### Remove a Docker Volume

> WARNING: Use with caution!

If you ever need to delete all your data stored in MongoDB, then you can just remove the Docker Volume and create a new one.

> NOTE: You may need to delete the container that uses the volume first.

```sh
$ docker volume rm bedu_mongodb_data
# bedu_mongodb_data
```

### MongoDB Server

#### Run a container to start the MongoDB Server

> Options:
>
> `--name mongodb_server` Name for the container.
>
> `-v bedu_mongodb_data:/data/db` Volume to store the data.
>
> `-p 0.0.0.0:27017:27017` Accept all incoming connections from port `27017` (host) and target port `27017` (container).
>
> `-d` Run the container in the background.

```sh
$ docker run --name mongodb_server -v bedu_mongodb_data:/data/db -p 0.0.0.0:27017:27017 -d mongo:4.0
# ccf135833b88de2dc746a7a7f393af10083591deea6a3023fecfb755f7b79680
```

#### Inspect that MongoDB Server is running

```sh
$ docker ps
# CONTAINER ID   IMAGE       COMMAND                  CREATED          STATUS          PORTS                      NAMES
# ccf135833b88   mongo:4.0   "docker-entrypoint.s…"   18 seconds ago   Up 16 seconds   0.0.0.0:27017->27017/tcp   mongodb_server
```

#### Stop the container running the MongoDB Server

```sh
$ docker stop mongodb_server
# mongodb_server
```

#### Start the stopped container for the MongoDB Server

```sh
$ docker start mongodb_server
# mongodb_server
```

#### Remove the stopped container for the MongoDB Server

```sh
$ docker rm mongodb_server
# mongodb_server
```

### MongoDB Client - Shell

TODO

### Resources

* [Docker Commands - Cheat Sheet](/docs/docker-cheat-sheet.md)
* [Docker-Compose File - Cheat Sheet](/docs/docker-compose-cheat-sheet.md)
* [Mongo - Docker Hub](https://hub.docker.com/_/mongo)
