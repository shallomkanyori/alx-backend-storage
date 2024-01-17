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

### Task 3
Write a SQL script that lists all bands with `Glam rock` as their main style, ranked by their longevity
Requirements:
- Column names must be: `band_name` and `lifespan` (in years until 2022 - please use `2022` instead of `YEAR(CURDATE())`)
- You should use attributes `formed` and `split` for computing the `lifespan`
- Your script can be executed on any database

### Task 4
Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
Quantity in the table `items` can be negative.

### Task 5
Write a SQL script that creates a trigger that resets the attribute `valid_email` only when the `email` has been changed.
