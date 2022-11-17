"""
Migrate data with INSERT INTO SELECT DISTINCT
Now it's finally time to migrate the data into the new tables. You'll use the following pattern:

INSERT INTO ... 
SELECT DISTINCT ... 
FROM ...;
It can be broken up into two parts:

First part:

SELECT DISTINCT column_name1, column_name2, ... 
FROM table_a;
This selects all distinct values in table table_a – nothing new for you.

Second part:

INSERT INTO table_b ...;
Take this part and append it to the first, so it inserts all distinct rows from table_a into table_b.

One last thing: It is important that you run all of the code at the same time once you have filled out the blanks.

Instructions 2/2

- Insert all DISTINCT professors from university_professors into professors.
- Print all the rows in professors.

- Insert all DISTINCT affiliations into affiliations from university_professors.
"""
#-- Insert unique professors into the new table
INSERT INTO professors 
SELECT DISTINCT firstname, lastname, university_shortname 
FROM university_professors;

#-- Doublecheck the contents of professors
SELECT * 
FROM professors;

#2
#-- Insert unique affiliations into the new table
INSERT INTO affiliations 
SELECT DISTINCT firstname, lastname, function, organization 
FROM university_professors;

#-- Doublecheck the contents of affiliations
SELECT * 
FROM affiliations;
