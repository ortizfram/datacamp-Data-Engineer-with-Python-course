"""
Count affiliations per university
Now that your data is ready for analysis, let's run some exemplary SQL queries on the database. You'll now use already known concepts such as grouping by columns and joining tables.

In this exercise, you will find out which university has the most affiliations (through its professors). For that, you need both affiliations and professors tables, as the latter also holds the university_id.

As a quick repetition, remember that joins have the following structure:

SELECT table_a.column1, table_a.column2, table_b.column1, ... 
FROM table_a
JOIN table_b 
ON table_a.column = table_b.column
This results in a combination of table_a and table_b, but only with rows where table_a.column is equal to table_b.column.

  Instructions
  100 XP
- Count the number of total affiliations by university.
- Sort the result by that count, in descending order.

"""
#-- Count the total number of affiliations per university
SELECT COUNT(*), professors.university_id 
FROM professors
JOIN affiliations
ON affiliations.professor_id = professors.id
#-- Group by the university ids of professors
GROUP BY professors.id 
ORDER BY count DESC;

'''count	university_id
18	ETH
18	UGE
18	EPF'''
