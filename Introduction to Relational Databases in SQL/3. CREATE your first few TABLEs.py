"""
CREATE your first few TABLEs
You'll now start implementing a better database model. For this, you'll create tables for the professors and universities entity types. The other tables will be created for you.

The syntax for creating simple tables is as follows:

CREATE TABLE table_name (
 column_a data_type,
 column_b data_type,
 column_c data_type
);
Attention: Table and columns names, as well as data types, don't need to be surrounded by quotation marks.

Instructions 1/2
- Create a table professors with two text columns: firstname and lastname.
- Create a table universities with three text columns: university_shortname, university, and university_city.

"""
-- Create a table for the professors entity type
CREATE TABLE professors (
 firstname text,
 lastname text
);

-- Print the contents of this table
SELECT * 
FROM professors

#2
-- Create a table for the universities entity type
CREATE TABLE universities (
    university_shortname text,
    university text,
    university_city text
);
-- Print the contents of this table
SELECT * 
FROM universities
