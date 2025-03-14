# SQL Introduction Project

This repository contains SQL scripts for various database operations. Here's a description of each script and its functionality:

## 0-list_databases.sql
- Lists all databases on the MySQL server
- Uses `SHOW DATABASES` command

## 1-create_database_if_missing.sql
- Creates the database `hbtn_0c_0`
- Uses `CREATE DATABASE IF NOT EXISTS` to avoid errors if database exists

## 2-remove_database.sql
- Deletes the database `hbtn_0c_0`
- Uses `DROP DATABASE IF EXISTS` to safely remove database

## 3-list_tables.sql
- Lists all tables in a specified database
- Uses `SHOW TABLES` command

## 4-first_table.sql
- Creates a table called `first_table`
- Defines columns: `id` (INT) and `name` (VARCHAR(256))
- Uses `CREATE TABLE IF NOT EXISTS`

## 5-full_table.sql
- Prints full description of `first_table`
- Uses `SHOW CREATE TABLE` command

## 6-list_values.sql
- Lists all rows in `first_table`
- Uses `SELECT * FROM` statement

## 7-insert_value.sql
- Inserts new row into `first_table`
- Uses `INSERT INTO` statement

## 8-count_89.sql
- Displays number of records with id = 89
- Uses `SELECT COUNT(*)` with `WHERE` clause

## 9-full_creation.sql
- Creates `second_table` and adds multiple rows
- Uses `CREATE TABLE` and `INSERT INTO` statements

## 10-top_score.sql
- Lists records ordered by score
- Uses `SELECT` with `ORDER BY` clause

## 11-best_score.sql
- Lists records with score >= 10
- Uses `SELECT` with `WHERE` and `ORDER BY`

## 12-no_cheating.sql
- Updates score of Bob
- Uses `UPDATE` statement with `WHERE` clause

## 13-change_class.sql
- Removes records with score <= 5
- Uses `DELETE FROM` with `WHERE` clause

## 14-average.sql
- Computes score average
- Uses `SELECT AVG()` function

## 15-groups.sql
- Lists number of records with same score
- Uses `SELECT` with `GROUP BY` and `COUNT()`

## 16-no_link.sql
- Lists records with name value
- Uses `SELECT` with `WHERE name IS NOT NULL`

Each script demonstrates different SQL commands and features for database management and manipulation.
