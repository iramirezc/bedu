# Data Analysis

## Session 05: MongoDB Fundamentals (with Docker)

Content Session:

* [Pre-Requisites](#Pre-Requisites)
* [DB Storage](#DB-Storage)
* [MongoDB Server](#MongoDB-Server)
* [MongoDB Client - Shell](#MongoDB-Client---Shell)
* [MongoDB Client - GUI](#MongoDB-Client---GUI)
* [The `mongo` Shell](#The-`mongo`-Shell)
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

**4. Download the data sets:**

* [ml-1m](https://www.dropbox.com/s/08m65ee45t5225u/ml-1m.zip?dl=0)

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

##### Option 1: Using `docker run` command

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

##### Option 2: Using a `docker-compose.yaml` file

Create a `docker-compose.yaml` in a `mongodb-server` folder with the following content:

```yaml
version: '3'

services:
  mongodb:
    image: mongo:4.0
    container_name: mongodb_server
    volumes:
      - mongodb_data:/data/db
    ports:
      - 27017:27017

volumes:
  mongodb_data:
    external: true
```

Then execute:

```sh
$ docker-compose up -d mongodb
# Creating mongodb_server ... done
```

> More info: [Docker-Compose File - Cheat Sheet](/docs/docker-compose-cheat-sheet.md)

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

### The `mongo` Shell

You can find most of the `mongo` commands in this [Mongo - Cheat Sheet](/docs/mongo-cheat-sheet.md) document.

#### Create a new Database and a Collection

Create a new Database using `yourLastName_yourFistName` as the DB name. Then, create an `users` collection.

```sh
> show dbs
# admin   0.000GB
# config  0.000GB
# local   0.000GB
> use ramirez_isaac
# switched to db ramirez_isaac
> db.createCollection('users')
# { "ok" : 1 }
> show dbs
# admin          0.000GB
# config         0.000GB
# local          0.000GB
# ramirez_isaac  0.000GB
```

#### Remove a Database

```sh
> use ramirez_isaac
# switched to db ramirez_isaac
> db.dropDatabase()
# { "dropped" : "ramirez_isaac", "ok" : 1 }
> show dbs
# admin   0.000GB
# config  0.000GB
# local   0.000GB
```

:cat: _**xercise 1**: Try to remove and create (again) your database using the MongoDB GUI of your preference. Then, add a `movies` collection._

#### Import data from a CSV file

In order to import the `csv` file to the MongoDB Server, we need to copy such file inside the Docker Container. The most easiest way to do this is to mount a folder with all your data sets as a volume pointing to any directory you choose inside the Docker Container.

Placeholders:

> `HOST_PATH` The directory in your host computer where you have the data sets.
>
> `CONTAINER_PATH` The directory inside the Docker Container where you can access your data sets.

Example values:

> `HOST_PATH` = `/Users/isaac.ramirez/bedu/mongo-server/ml-1m`
>
> `CONTAINER_PATH` = `/usr/scr/data`

##### Using `docker run` command

Add the following option to the `docker run` command:

```sh
-v HOST_PATH:CONTAINER_PATH
```

Example:

```sh
$ docker run --name mongodb_server -v bedu_mongodb_data:/data/db -v /Users/isaac.ramirez/bedu/mongo-server/ml-1m:/usr/src/data -p 0.0.0.0:27017:27017 -d mongo:4.0
# 612f26ac1b2a98d0290131241ae294fe2552f7236799df754514ea76307fde50
```

##### Using `docker-compose.yaml` file

Add the following under `volumes:`

```yaml
    volumes:
      - HOST_PATH:CONTAINER_PATH
```

Example:

```yaml
    volumes:
      - bedu_mongodb_data:/data/db
      - ./ml-1m:/usr/src/data
```

##### Import the CSV file using the `mongoimport` command

Now that you have mounted the data sets inside the Docker Container you can run the `mongoimport` command:

```sh
$ docker exec mongodb_server mongoimport --db=ramirez_isaac --collection=users --type=csv --headerline --file=/usr/src/data/users-h.csv
# 2019-12-20T08:59:51.063+0000 connected to: localhost
# 2019-12-20T08:59:51.194+0000 imported 6040 documents
```

:cat: _**xercise 2**: Import the `ratings-h.csv` file using `mongoimport`. Then, import the `movies-h.csv` file using MongoDB Compass._

#### JSON (JavaScript Object Notation)

Example of a JSON object:

```json
{
    "string": "myString",
    "number": 27,
    "boolean": true,
    "date": "2019-12-20T22:42:08.127Z",
    "null": null,
    "object": {
        "prop1": "anyString",
        "prop2": 0
    },
    "array": ["cat", 99, false, { "data": null }]
}
```

Example of a JSON array:

```json
[
    {
        "id": 1,
        "firstName": "Roberto",
        "lastName": "Gómez"
    },
    {
        "id": 2,
        "firstName": "María",
        "lastName": "Mercedes"
    }
]
```

#### CRUD Operations

##### Insert a new document (Create)

```sh
> use ramirez_isaac
> db.users.insertOne({
    "id": 1987,
    "gen": "M",
    "edad": 32,
    "ocup": 10,
    "cp": 44600
})
# {
#   "acknowledged" : true,
#   "insertedId" : ObjectId("5dfd4feea9288f2e0d4d55c2")
# }
>
```

##### Insert multiple documents (Create)

```sh
> db.users.insertMany([
    {
        "id": 6041,
        "gen": "M",
        "edad": 25,
        "ocup": 15,
        "cp": 11106
    },
    {
        "id": 6042,
        "gen": "F",
        "edad": 40,
        "ocup": 4,
        "cp": 45123
    },
])
# {
#   "acknowledged" : true,
#   "insertedIds" : [
#       ObjectId("5dfd537ba9288f2e0d4d55c5"),
#       ObjectId("5dfd537ba9288f2e0d4d55c6")
#   ]
# }
>
```

##### Find a document by `ObjectId` (Read)

```sh
> db.users.findOne({ "_id": ObjectId("5dfd4feea9288f2e0d4d55c2") })
# {
#   "_id" : ObjectId("5dfd4feea9288f2e0d4d55c2"),
#   "id" : 1987,
#   "gen" : "H",
#   "edad" : 32,
#   "ocup" : 10,
#   "cp" : "44600"
# }
>
```

##### Find a document by property (Read)

```sh
> db.users.findOne({ "edad": 32 })
# {
#   "_id" : ObjectId("5dfd4feea9288f2e0d4d55c2"),
#   "id" : 1987,
#   "gen" : "H",
#   "edad" : 32,
#   "ocup" : 10,
#   "cp" : "44600"
# }
>
```

##### Find all documents

```sh
> db.users.find()
# { "_id" : ObjectId("5dfd4b44ebbfc47a4c1decc2"), "id" : 2, "gen" : "M", "edad" : 56, "ocup" : 16, "cp" : 70072 }
# { "_id" : ObjectId("5dfd4b44ebbfc47a4c1decc3"), "id" : 1, "gen" : "F", "edad" : 1, "ocup" : 10, "cp" : 48067 }
# ...
# Type "it" for more
> it
# { "_id" : ObjectId("5dfd4b44ebbfc47a4c1decd6"), "id" : 22, "gen" : "M", "edad" : 18, "ocup" : 15, "cp" : 53706 }
# { "_id" : ObjectId("5dfd4b44ebbfc47a4c1decd7"), "id" : 23, "gen" : "M", "edad" : 35, "ocup" : 0, "cp" : 90049 }
# ...
# Type "it" for more
>
```

##### Find all documents by searching criteria

```sh
> db.users.find({ "gen": "M", "ocup": 15 })
# { "_id" : ObjectId("5dfd4b44ebbfc47a4c1decc4"), "id" : 3, "gen" : "M", "edad" : 25, "ocup" : 15, "cp" : 55117 }
# { "_id" : ObjectId("5dfd4b44ebbfc47a4c1decd6"), "id" : 22, "gen" : "M", "edad" : 18, "ocup" : 15, "cp" : 53706 }
# ...
# Type "it" for more
>
```

##### Update a single document based on the filter (Update)

```sh
> db.users.updateOne({ "id": 6042 }, { "$set": { "movie_genders": ["drama", "action", "triller"] } })
# { "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
```

##### Update multiple documents based on the filter (Update)

```sh
> db.users.updateMany({ "gen": "F" }, { "$set": { "movie_genders": ["romantic", "horror"] } })
# { "acknowledged" : true, "matchedCount" : 1710, "modifiedCount" : 1710 }
```

##### Delete a single document based on the filter (Remove)

```sh
> db.users.deleteOne({ "id": 6042 })
# { "acknowledged" : true, "deletedCount" : 1 }
```

##### Delete multiple documents based on the filter (Remove)

```sh
> db.users.deleteMany({ "edad": { "$lt": 10 } }) # less than 10 years
# { "acknowledged" : true, "deletedCount" : 222 }
```

:cat: _**xercise 3**: Perform all the **CRUD** operations but using MongoDB Compass._

### Resources

* [Mongo - Docker Hub](https://hub.docker.com/_/mongo)
* [Docker Commands - Cheat Sheet](/docs/docker-cheat-sheet.md)
* [Docker-Compose File - Cheat Sheet](/docs/docker-compose-cheat-sheet.md)
* [Mongo - Cheat Sheet](/docs/mongo-cheat-sheet.md)
