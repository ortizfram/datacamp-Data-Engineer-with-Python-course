"""
CONCATenate columns to a surrogate key
Another strategy to add a surrogate key to an existing table is to concatenate existing columns with the CONCAT() function.

Let's think of the following example table:

CREATE TABLE cars (
 make varchar(64) NOT NULL,
 model varchar(64) NOT NULL,
 mpg integer NOT NULL
)
The table is populated with 10 rows of completely fictional data.

Unfortunately, the table doesn't have a primary key yet. None of the columns consists of only unique values, so some columns can be combined to form a key.

In the course of the following exercises, you will combine make and model into such a surrogate key.

Instructions 4/4

- Count the number of distinct rows with a combination of the make and model columns.
- Add a new column id with the data type varchar(128).
- Concatenate make and model into id using an UPDATE table_name SET column_name = ... query and the CONCAT() function.
- Make id a primary key and name it id_pk.

"""
#1
#-- Count the number of distinct rows with columns make, model
SELECT COUNT(DISTINCT(make, model))
FROM cars;

#2
#-- Add the id column
ALTER TABLE cars
ADD COLUMN id varchar(128);

#3
#-- Update id with make + model
-- UPDATE, SET x =
UPDATE cars
SET id = CONCAT(make, model);

#4
#-- Make id a primary key
ALTER TABLE cars
ADD CONSTRAINT id_pk PRIMARY KEY(id);

#-- Have a look at the table
SELECT * FROM cars;
