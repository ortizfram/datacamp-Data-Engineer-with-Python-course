"""
ADD key CONSTRAINTs to the tables
Two of the tables in your database already have well-suited candidate keys consisting of one column each: organizations and universities with the organization and university_shortname columns, respectively.

In this exercise, you'll rename these columns to id using the RENAME COLUMN command and then specify primary key constraints for them. This is as straightforward as adding unique constraints (see the last exercise of Chapter 2):

ALTER TABLE table_name
ADD CONSTRAINT some_name PRIMARY KEY (column_name)
Note that you can also specify more than one column in the brackets.

Instructions 1/2

1
- Rename the organization column to id in organizations.
- Make id a primary key and name it organization_pk.
2
- Rename the university_shortname column to id in universities.
- Make id a primary key and name it university_pk.

"""
#-- Rename the organization column to id
ALTER TABLE organizations
RENAME COLUMN organization TO id;

#-- Make id a primary key
ALTER TABLE organizations
ADD CONSTRAINT organization_pk PRIMARY KEY (id);

#2
#-- Rename the university_shortname column to id
ALTER TABLE universities
RENAME COLUMN university_shortname TO id;

#-- Make id a primary key
ALTER TABLE universities
ADD CONSTRAINT university_pk PRIMARY KEY (id);
