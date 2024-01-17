# MySQL Advanced

## Tasks

### Task 0
Write a SQL script that creates a table `users` following these requirements:
- With these attributes:
	- `id`, integer, never null, auto increment and primary key
	- `email`, string (255 characters), never null and unique
	- `name`, string (255 characters)
- If the table already exists, your script should not fail
- Your script can be executed on any database

### Task 1
Write a SQL script that creates a table users following these requirements:
- With these attributes:
	- `id`, integer, never null, auto increment and primary key
	- `email`, string (255 characters), never null and unique
	- `name`, string (255 characters)
	- `country`, enumeration of countries: `US`, `CO` and `TN`, never null (= default will be the first element of the enumeration, here `US`)
- If the table already exists, your script should not fail
- Your script can be executed on any database

### Task 2
Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
Requirements:
- Import [metal_bands.sql](metal_bands.sql) table dump
- Column names must be: `origin` and `nb_fans`
- Your script can be executed on any database
