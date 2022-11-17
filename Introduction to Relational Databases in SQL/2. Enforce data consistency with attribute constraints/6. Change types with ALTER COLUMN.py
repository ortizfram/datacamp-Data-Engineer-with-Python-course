"""
Change types with ALTER COLUMN
The syntax for changing the data type of a column is straightforward. The following code changes the data type of the column_name column in table_name to varchar(10):

ALTER TABLE table_name
ALTER COLUMN column_name
TYPE varchar(10)
Now it's time to start adding constraints to your database.

Instructions 3/3
- Have a look at the distinct university_shortname values in the professors table and take note of the length of the strings.
- Now specify a fixed-length character type with the correct length for university_shortname.
- Change the type of the firstname column to varchar(64).

"""
#-- Select the university_shortname column
SELECT DISTINCT(university_shortname) 
FROM professors;

#-- Specify the correct fixed-length character type
ALTER TABLE professors
ALTER COLUMN university_shortname
TYPE char(3);

#-- Change the type of firstname
ALTER TABLE professors
ALTER COLUMN firstname
TYPE varchar(64);

