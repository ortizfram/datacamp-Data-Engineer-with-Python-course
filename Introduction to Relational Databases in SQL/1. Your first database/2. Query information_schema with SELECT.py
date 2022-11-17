'''
Query information_schema with SELECT
information_schema is a meta-database that holds information about your current database. information_schema has multiple tables you can query with the known SELECT * FROM syntax:

tables: information about all tables in your current database
columns: information about all columns in all of the tables in your current database
…
In this exercise, you'll only need information from the 'public' schema, which is specified as the column table_schema of the tables and columns tables. The 'public' schema holds information about user-defined tables and databases. The other types of table_schema hold system information – for this course, you're only interested in user-defined stuff.

Instructions 4/4
25 XP
- Get information on all table names in the current database, while limiting your query to the 'public' table_schema.
- Now have a look at the columns in university_professors by selecting all entries in information_schema.columns that correspond to that table.
- How many columns does the table university_professors have?
- Finally, print the first five rows of the university_professors table.
'''
#1
#-- Query the right table in information_schema
SELECT table_name 
FROM information_schema.tables
#-- Specify the correct table_schema value
WHERE table_schema = 'public';

#2
#-- Query the right table in information_schema to get columns
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'university_professors' AND table_schema = 'public';

#3
#How many columns does the table university_professors have?
#8

# 4
-- Query the first five rows of our table
SELECT * 
FROM university_professors 
LIMIT 5;
