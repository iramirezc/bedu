# Mongo Cheat Sheet

## Helpers

### Show help

Usage:

```js
help
```

### Show help for Database methods

Usage:

```js
db.help()
```

### Show help on Collection methods

Usage:

```js
db.<collection>.help()
```

## Databases

### Show current selected Database

Usage:

```js
db
```

### List all Databases

Usage:

```js
show dbs
```

### Use a Database

Usage:

```js
use <db>
```

### Create a new Database

See [Create a new Collection](#Create-a-new-Collection)

### Remove a Database

Usage:

```js
db.dropDatabase()
```

## Collections

### Show all Collections

Usage:

```js
show collections
```

### Create a new Collection

Usage:

```js
db.createCollection('collection_name')
```

### Remove a Collection

Usage:

```js
db.<collection>.drop()
```

## Documents

### Import data from a CSV file with headers

> **NOTE:** The `mongoimport` command is not part of the `mongo` shell.

#### MongoDB Server running in the host computer

Usage:

```sh
mongoimport --db=DB_NAME --collection=COLLECTION_NAME --type=TYPE --headerline --file=PATH_TO_FILE
```

Example:

```sh
$ mongoimport --db=ramirez_isaac --collection=users --type=csv --headerline --file=/usr/src/data/users-h.csv
# 2019-12-20T08:59:51.063+0000 connected to: localhost
# 2019-12-20T08:59:51.194+0000 imported 6040 documents
```

#### MongoDB Server running in a remote computer

Usage:

```sh
mongoimport --host SERVER_IP --port SERVER_PORT --db=DB_NAME --collection=COLLECTION_NAME --type=TYPE --headerline --file=PATH_TO_FILE
```

Example:

```sh
$ mongoimport --host 127.0.0.1 --port 27017 --db=ramirez_isaac --collection=users --type=csv --headerline --file=users-h.csv
# 2019-12-20T03:09:49.915-0600 connected to: 127.0.0.1:27017
# 2019-12-20T03:09:50.112-0600 imported 6040 documents
```

#### MongoDB Server running inside a Docker Container

Usage:

```sh
docker exec CONTAINER mongoimport --db=DB_NAME --collection=COLLECTION_NAME --type=TYPE --headerline --file=PATH_TO_FILE
```

Example:

> NOTE: make sure the file exists (or is mounted) if running inside a Docker Container.

```sh
$ docker exec mongodb_server mongoimport --db=ramirez_isaac --collection=users --type=csv --headerline --file=/usr/src/data/users-h.csv
# 2019-12-20T08:59:51.063+0000 connected to: localhost
# 2019-12-20T08:59:51.194+0000 imported 6040 documents
```

### Find one document

Usage:

```js
db.<collection>.findOne()
```

### Find all documents

Usage:

```js
db.<collection>.find({})
```

### Find & format all documents

Usage:

```js
db.<collection>.find({}).pretty()
```

### Find only the first N documents

Usage:

```js
db.<collection>.find().limit(N)
```

### Find document by ObjectId

```js
db.<collection>.find({ _id: ObjectId('5dfc8fdd6497f22bd3a92407') })
```

### Find all documents that match the condition

Usage:

```js
// strings
db.<collection>.find({ prop: 'value' })
// numbers
db.<collection>.find({ prop: 100 })
// booleans
db.<collection>.find({ prop: true })
```

### Find all documents that match two conditions (AND)

Usage:

```js
// TODO
```

### Find all documents that match either condition (OR)

Usage:

```js
// TODO
```

### Find all documents that are similar to the condition (LIKE)

Usage:

```js
// TODO
```

### Delete all documents from a collection

Usage:

```js
db.<collection>.remove({})
```
