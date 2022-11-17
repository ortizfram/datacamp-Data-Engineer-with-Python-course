"""
Populate the "professor_id" column
Now it's time to also populate professors_id. You'll take the ID directly from professors.

Here's a way to update columns of a table based on values in another table:

UPDATE table_a
SET column_to_update = table_b.column_to_update_from
FROM table_b
WHERE condition1 AND condition2 AND ...;
This query does the following:

For each row in table_a, find the corresponding row in table_b where condition1, condition2, etc., are met.
Set the value of column_to_update to the value of column_to_update_from (from that corresponding row).
The conditions usually compare other columns of both tables, e.g. table_a.some_column = table_b.some_column. Of course, this query only makes sense if there is only one matching row in table_b.

Instructions 3/3
- First, have a look at the current state of affiliations by fetching 10 rows and all columns.
- Update the professor_id column with the corresponding value of the id column in professors.
  "Corresponding" means rows in professors where the firstname and lastname are identical to the ones in affiliations.
- Check out the first 10 rows and all columns of affiliations again. Have the professor_ids been correctly matched?

"""
#1
#-- Have a look at the 10 first rows of affiliations
SELECT *
FROM affiliations
LIMIT 10;

#2
#-- Set professor_id to professors.id where firstname, lastname correspond to rows in professors
UPDATE affiliations
SET professor_id = professors.id
FROM professors
WHERE affiliations.firstname = professors.firstname AND affiliations.lastname = professors.lastname;

#3
#-- Have a look at the 10 first rows of affiliations again
SELECT *
FROM affiliations
LIMIT 10;
