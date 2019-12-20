# SQL Cheat Sheet

## Databases

### List All Databases

Usage:

```sql
SHOW DATABASES;
```

### Create a new Database

Usage:

```sql
CREATE DATABASE [IF NOT EXISTS] db_name;
```

### Remove a Database

Usage:

```sql
DROP DATABASE [IF EXISTS] db_name;
```

### Use a Database

Usage:

```sql
USE db_name;
```

## Tables

### Show all Tables

Usage:

```sql
SHOW TABLES;
```

### Create a new Table

Usage:

```sql
CREATE TABLE [IF NOT EXISTS] table_name (column_1_name column_1_type [PRIMARY KEY] [AUTO_INCREMENT], [column_N_name column_N_type, ...]);`
```

### Check the structure of a Table

Usage:

```sql
DESCRIBE table_name;
```

### Remove a Table

Usage:

```sql
DROP TABLE [IF EXISTS] table_name;
```

## Data

### Load data from a CSV file

Usage:

```sql
LOAD DATA LOCAL INFILE "file_name.ext" INTO TABLE table_name FIELDS TERMINATED BY "the_csv_delimiter";
```

### Find all records from a table showing all the columns

Usage:

```sql
SELECT * FROM table_name;
```

### Find all records from a table showing only some columns

Usage:

```sql
SELECT column_1[, column_N, ...] FROM table_name;
```

### Find only the first N records

Usage:

```sql
SELECT [...] FROM [...] LIMIT n;
```

### Find all records that match the condition

Usage:

```sql
-- strings
SELECT [...] FROM [...] WHERE column_name = 'string_value';
-- numbers
SELECT [...] FROM [...] WHERE column_name = 100;
```

### Find all records that match two conditions

Usage:

```sql
SELECT [...] FROM [...] WHERE criteria_1 AND criteria_2;
```

### Find all records that match either condition

Usage:

```sql
SELECT [...] FROM [...] WHERE criteria_1 OR criteria_2;
```

### Find all records that are similar to the condition

Usage:

```sql
SELECT [...] FROM [...] WHERE column_name LIKE 'your_wildcard';
```

### Delete all records from a table

Usage:

```sql
TRUNCATE table_name;
```
