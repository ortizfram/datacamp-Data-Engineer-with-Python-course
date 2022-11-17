"""
Make your columns UNIQUE with ADD CONSTRAINT
As seen in the video, you add the UNIQUE keyword after the column_name that should be unique. This, of course, only works for new tables:

CREATE TABLE table_name (
 column_name UNIQUE
);
If you want to add a unique constraint to an existing table, you do it like that:

ALTER TABLE table_name
ADD CONSTRAINT some_name UNIQUE(column_name);
Note that this is different from the ALTER COLUMN syntax for the not-null constraint. Also, you have to give the constraint a name some_name.

Instructions 2/2
- Add a unique constraint to the university_shortname column in universities. Give it the name university_shortname_unq.
- Add a unique constraint to the organization column in organizations. Give it the name organization_unq.

"""
#-- Make universities.university_shortname unique
ALTER TABLE universities
ADD CONSTRAINT university_shortname_unq UNIQUE(university_shortname);

#-- Make organizations.organization unique
ALTER TABLE organizations
ADD CONSTRAINT organization_unq UNIQUE(organization);
