"""
JOIN tables linked by a foreign key
Let's join these two tables to analyze the data further!

You might already know how SQL joins work from the Intro to SQL for Data Science course (last exercise) or from Joining Data in PostgreSQL.

Here's a quick recap on how joins generally work:

SELECT ...
FROM table_a
JOIN table_b
ON ...
WHERE ...
While foreign keys and primary keys are not strictly necessary for join queries, they greatly help by telling you what to expect. For instance, you can be sure that records referenced from table A will always be present in table B – so a join from table A will always find something in table B. If not, the foreign key constraint would be violated.

Instructions
100 XP
- JOIN professors with universities on professors.university_id = universities.id, i.e., retain all records where the foreign key of professors is equal to the primary key of universities.
- Filter for university_city = 'Zurich'.

"""
#-- Select all professors working for universities in the city of Zurich
SELECT professors.lastname, universities.id, universities.university_city
FROM universities 
INNER JOIN professors 
ON professors.university_id = universities.id
WHERE universities.university_city = 'Zurich';
