"""
RENAME and DROP COLUMNs in affiliations
As mentioned in the video, the still empty affiliations table has some flaws. In this exercise, you'll correct them as outlined in the video.

You'll use the following queries:

To rename columns:
ALTER TABLE table_name
RENAME COLUMN old_name TO new_name;
To delete columns:
ALTER TABLE table_name
DROP COLUMN column_name;

Instructions 2/2
- Rename the organisation column to organization in affiliations
- Delete the university_shortname column in affiliations.

"""
#-- Rename the organisation column
ALTER TABLE affiliations
RENAME COLUMN organisation TO organization;

#2
#-- Delete the university_shortname column
ALTER TABLE affiliations
DROP COLUMN university_shortname;
