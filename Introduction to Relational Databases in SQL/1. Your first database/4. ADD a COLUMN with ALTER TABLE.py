"""
ADD a COLUMN with ALTER TABLE
Oops! We forgot to add the university_shortname column to the professors table. You've probably already noticed:

In chapter 4 of this course, you'll need this column for connecting the professors table with the universities table.

However, adding columns to existing tables is easy, especially if they're still empty.

To add columns you can use the following SQL query:

ALTER TABLE table_name
ADD COLUMN column_name data_type;
Instructions
100 XP
- Alter professors to add the text column university_shortname.

"""
-- Add the university_shortname column
ALTER TABLE professors
ADD COLUMN university_shortname text;

-- Print the contents of this table
SELECT * 
FROM professors
