"""
Get to know SELECT COUNT DISTINCT
Your database doesn't have any defined keys so far, and you don't know which columns or combinations of columns are suited as keys.

There's a simple way of finding out whether a certain column (or a combination) contains only unique values – and thus identifies the records in the table.

You already know the SELECT DISTINCT query from the first chapter. Now you just have to wrap everything within the COUNT() function and PostgreSQL will return the number of unique rows for the given columns:

SELECT COUNT(DISTINCT(column_a, column_b, ...))
FROM table;
Instructions 2/2
- First, find out the number of rows in universities.
- Then, find out how many unique values there are in the university_city column.

"""
#-- Count the number of rows in universities
SELECT COUNT(*) 
FROM universities;

#-- Count the number of distinct values in the university_city column
SELECT COUNT(DISTINCT(university_city)) 
FROM universities;
