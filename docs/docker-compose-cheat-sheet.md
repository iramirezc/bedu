# Docker-Compose Cheat Sheet

## The `docker-compose.yaml` file

**1. Create a `docker-compose.yaml` file:**

Make sure to create a `docker-compose.yaml` file in your working directory.

Example:

```sh
$ touch docker-compose.yaml
# Creates a file in your current directory
```

**2. Edit your `docker-compose.yaml` file:**

After creating your `docker-compose.yaml` file, copy one of the _templates_ below and paste it into the file.

**3. Run `docker-compose`:**

Once you have a `docker-compose.yaml` file with a template, run the `docker-compose` command.

Usage:

```sh
docker-compose COMMAND [OPTIONS] [SERVICE]
```

Options:

> `-d` Run containers in the background

Example:

```sh
$ docker-compose up -d mariadb
# Creating mariadb_server ... done
```

**4. Inspect Container is running:**

Example:

```sh
$ docker ps
# CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                    NAMES
# ae09d18a8a5a   mariadb:10.3   "docker-entrypoint.s…"   18 seconds ago   Up 17 seconds   0.0.0.0:3306->3306/tcp   mariadb_server
```

You are all set!

## Templates

### MariaDB Server

This configuration file runs a MariaDB server into a container named `mariadb_server` using a volume `mariadb_data` to store the data and exposes container's port `3306` to host's port `3306`.

The MariaDB root password is set to `secret`.

```yml
version: '3'

services:
  mariadb:
    image: mariadb:10.3
    container_name: mariadb_server
    volumes:
      - mariadb_data:/var/lib/mysql
    ports:
      - 3306:3306
    environment:
      - MYSQL_ROOT_PASSWORD=secret

volumes:
  mariadb_data:
    external: true
```

Usage:

```sh
docker-compose up -d mariadb
```

### MongoDB Server

This configuration file runs a MongoDB server into a container named `mongodb_server` using a volume `mongodb_data` to store the data and exposes container's port `27017` to host's port `27107`.

```yml
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

Usage:

```sh
docker-compose up -d mongodb
```
