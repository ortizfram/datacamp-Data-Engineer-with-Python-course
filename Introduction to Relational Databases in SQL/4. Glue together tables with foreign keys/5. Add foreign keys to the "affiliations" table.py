"""
Add foreign keys to the "affiliations" table
At the moment, the affiliations table has the structure {firstname, lastname, function, organization}, as you can see in the preview at the bottom right. In the next three exercises, you're going to turn this table into the form {professor_id, organization_id, function}, with professor_id and organization_id being foreign keys that point to the respective tables.

You're going to transform the affiliations table in-place, i.e., without creating a temporary table to cache your intermediate results.

Instructions 3/3
- Add a professor_id column with integer data type to affiliations, and declare it to be a foreign key that references the id column in professors.
- Rename the organization column in affiliations to organization_id.
- Add a foreign key constraint on organization_id so that it references the id column in organizations.

"""
#1
#-- Add a professor_id column to affiliations
ALTER TABLE affiliations
ADD COLUMN professor_id integer REFERENCES professors (id); 

#2
#-- Rename the organization column to organization_id
ALTER TABLE affiliations
RENAME organization TO organization_id;

#3
#-- Add a foreign key on organization_id
ALTER TABLE affiliations
ADD CONSTRAINT affiliations_organization_fkey FOREIGN KEY (organization_id) REFERENCES organizations (id);
