# Data Analysis

## Session 05: MongoDB Fundamentals (with Docker)

Content Session:

* [Pre-Requisites](#Pre-Requisites)
* [DB Storage](#DB-Storage)
* [MongoDB Server](#MongoDB-Server)
* [MongoDB Client - Shell](#MongoDB-Client---Shell)
* [MongoDB Client - GUI](#MongoDB-Client---GUI)
* [Resources](#Resources)

### Pre-Requisites

**1. Install Docker:**

[How to install Docker Community Edition](../docs/docker-installation.md)

**2. Pull the Mongo Docker Image from Docker Hub:**

```sh
$ docker pull mongo:4.0
# 4.0: Pulling from library/mongo
```

**3. Install a GUI for MongoDB:**

You can choose any of these or both:

* [Robo 3T](https://robomongo.org/download)
* [MongoDB Compass](https://www.mongodb.com/download-center/compass)

### DB Storage

We need a Docker Volume to **NOT** lost the data we store in the database when working with containers because containers can be removed and created multiple times.

#### Create a Docker Volume

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

> NOTE: if you did NOT run the container with a volume, then all your data inside the container will be lost!

```sh
$ docker rm mongodb_server
# mongodb_server
```

#### MongoDB Server IP Address & Port

Before attempting to connect to the MongoDB Server, you should know in which IP address and port is running on.

There can be different scenarios but the most commons are:
  
* The MongoDB Server is running in you host computer.
* The MongoDB Server is running in a Docker Container inside your host computer.
* The MongoDB Server is running in a remote computer.

For any case, you should know the `IP` address and the `Port`.

##### The MongoDB Server is running in you host computer

If you have installed the MongoDB Server in your host computer, then you can use the following values:

* __MongoDB Server IP Address__: `localhost` or `127.0.0.1`
* __MongoDB Server Port__: `27017`

##### The MongoDB Server is running in a Docker Container inside your host computer

If you have been following the instructions so far using Docker, then you can use the following configuration values:

* __MongoDB Server IP Address__: `localhost` or `127.0.0.1`
* __MongoDB Server Port__: `27017`

> **NOTE:** If you can NOT connect using the values above or you are running Docker in a Windows computer, then try to retrieve the IP address from the Docker Machine:

```sh
$ docker-machine ip
# 192.168.0.2
```

If you want to connect to the MongoDB Server from a different container, then inspect the Docker Container. Take note about the Network's name `mongo-server_default` and the IP Address `192.168.0.2`.

```sh
$ docker inspect mongodb_server
# ...
# "NetworkSettings": {
#   ...
#   "Networks": {
#     "mongo-server_default": {
#       ...
#       "IPAddress": "192.168.0.2",
# ...
```

##### The MongoDB Server is running in a remote computer

If the MongoDB Server is running in a remote computer, then you should request the IP address, the port and maybe the credentials to the DB Admin.

> **NOTE:** Ask your expert for this information during the class.

### MongoDB Client - Shell

#### Connect to the MongoDB Server using the mongo shell client inside the same container

Execute the `mongo` command inside the `mongodb_server` container to run the mongo shell and connect to the MongoDB Server. Finally, test the connection by issuing the command `show dbs`.

```sh
$ docker exec -it mongodb_server mongo
# MongoDB shell version v4.0.14
# connecting to: mongodb://127.0.0.1:27017
> show dbs
# admin   0.000GB
# config  0.000GB
# local   0.000GB
>
```

#### Connect to the MongoDB Server from a different container

> NOTE: You should already know the IP address from the container that is running the Server. Check the section: [The MongoDB Server is running in a Docker Container inside your host computer](#The-MongoDB-Server-is-running-in-a-Docker-Container-inside-your-host-computer).

Options:

> `--rm` Automatically remove the container when it exits.
>
> `-it` Interactive & pseudo-TTY
>
> `--network mongo-server_default` Connect the container to the network `mongo-server_default`.

Arguments:

> `--host 192.168.0.2` The MongoDB Server IP
>
> `--port 27017` The MongoDB Server port

```sh
$ docker run --rm -it --network mongo-server_default mongo:4.0 mongo --host 192.168.0.2 --port 27017
# MongoDB shell version v4.0.14
# connecting to: mongodb://192.168.0.2:27017/
> show dbs
# admin   0.000GB
# config  0.000GB
# local   0.000GB
>
```

### MongoDB Client - GUI

Before you continue, you should already know the [MongoDB Server IP Address & Port](MongoDB-Server-IP-Address-&-Port) in which the Server is running on.

Placeholders:

> `SERVER_IP` The MongoDB Server IP address.
>
> `PORT` The MongoDB Server port.

#### Connect to the MongoDB Server using `Robo 3T`

> NOTE: These instructions may vary depending on your Operating System.

1. Open __Robo 3T__
2. In the __MongoDB Connections__ click __Create__
    1. Fill in the following data:
        * __Name__: `localhost`
        * __Address__: `SERVER_IP` : `PORT`
    2. Click __Test__
        * You should see a successful message.
        * Close the pop-up message.
    3. Click __Save__.
3. Click __Connect__.
4. You are all set!

#### Connect to the MongoDB Server using `MongoDB Compass`

> NOTE: These instructions may vary depending on your Operating System.

1. Open __MongoDB Compass__
2. Select __New Connection__
3. Fill in the following data:
    * __Hostname__: `SERVER_IP`
    * __Port__: `PORT`
    * __Favorite Name__: `localhost`
4. Click __Create Favorite__
5. Click __Connect__
6. You are all set!

### Resources

* [Mongo - Docker Hub](https://hub.docker.com/_/mongo)
* [Docker Commands - Cheat Sheet](/docs/docker-cheat-sheet.md)
* [Docker-Compose File - Cheat Sheet](/docs/docker-compose-cheat-sheet.md)
