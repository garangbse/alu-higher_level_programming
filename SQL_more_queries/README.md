# SQL More Queries Project

This directory contains SQL scripts demonstrating various MySQL query operations, user privileges, and table relationships.

## Script Descriptions

### 0-privileges.sql
* Lists all privileges of MySQL users `user_0d_1` and `user_0d_2`
* Uses `SHOW GRANTS` command

### 1-create_user.sql
* Creates MySQL user `user_0d_1` with all privileges
* Sets password for the user
* Uses `CREATE USER` and `GRANT` commands

### 2-create_read_user.sql
* Creates database `hbtn_0d_2`
* Creates user `user_0d_2`
* Grants SELECT privilege to `user_0d_2`

### 3-force_name.sql
* Creates table `force_name` with columns:
    * id (INT)
    * name (VARCHAR(256)) - cannot be null

### 4-never_empty.sql
* Creates table `id_not_null` with columns:
    * id (INT) - default value 1
    * name (VARCHAR(256))

### 5-unique_id.sql
* Creates table `unique_id` with columns:
    * id (INT) - default value 1, must be unique
    * name (VARCHAR(256))

### 6-states.sql
* Creates database `hbtn_0d_usa`
* Creates table `states` with columns:
    * id (INT) - primary key, auto-generated
    * name (VARCHAR(256)) - cannot be null

### 7-cities.sql
* Creates table `cities` with columns:
    * id (INT) - primary key, auto-generated
    * state_id (INT) - foreign key referencing states.id
    * name (VARCHAR(256)) - cannot be null

### 8-cities_of_california_subquery.sql
* Lists all cities of California found in `hbtn_0d_usa`
* Uses subquery to find state_id of California

### 9-cities_by_state_join.sql
* Lists all cities with their state names
* Uses JOIN to combine data from cities and states tables

### 10-genre_id_by_show.sql
* Lists shows that have at least one genre linked
* Displays tv_shows.title and tv_show_genres.genre_id
* Uses JOIN operation

### 11-genre_id_all_shows.sql
* Lists all shows with their genre IDs (including shows without genres)
* Uses LEFT JOIN operation

### 12-no_genre.sql
* Lists shows without a genre linked
* Uses LEFT JOIN and WHERE to filter results

### 13-count_shows_by_genre.sql
* Lists genres and number of shows linked to each
* Uses GROUP BY and COUNT operations

### 14-my_genres.sql
* Lists genres of the show "Dexter"
* Uses multiple JOINs to get the result

### 15-comedy_only.sql
* Lists all Comedy shows
* Uses multiple JOINs and WHERE clause

### 16-shows_by_genre.sql
* Lists all shows and their linked genres
* Uses LEFT JOIN to include shows without genres

Each script demonstrates different aspects of MySQL including:
* User management
* Privileges
* Table creation
* Primary and foreign keys
* JOINs
* Subqueries
* Aggregation functions
