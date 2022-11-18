"""
Querying the dimensional model
Here it is! The schema reorganized using the dimensional model: 

Let's try to run a query based on this schema. How about we try to find the number of minutes we ran in July, 2019? We'll break this up in two steps. First, we'll get the total number of minutes recorded in the database. Second, we'll narrow down that query to week_id's from July, 2019.

Instructions 2/2

1- Calculate the sum of the duration_mins column.

2- Join week_dim and runs_fact.
2- Get all the week_id's from July, 2019.

"""
#1 
#-- Select the sum of the duration of all runs
SELECT SUM(duration_mins)
FROM runs_fact;
  
#2
#-- Get all the week_id's that are from July, 2019
INNER JOIN week_dim ON runs_fact.week_id = week_dim.week_id
WHERE month = 'July' and year = '2019';
