"""
Explore foreign key constraints
Foreign key constraints help you to keep order in your database mini-world. In your database, for instance, only professors belonging to Swiss universities should 
be allowed, as only Swiss universities are part of the universities table.

The foreign key on professors referencing universities you just created thus makes sure that only existing universities can be specified when inserting new data.
Let's test this!

Instructions
100 XP
- Run the sample code and have a look at the error message.
- What's wrong? Correct the university_id so that it actually reflects where Albert Einstein wrote his dissertation and became a professor
      – at the University of Zurich (UZH)!

"""
#-- Try to insert a new professor
INSERT INTO professors (firstname, lastname, university_id)
VALUES ('Albert', 'Einstein', 'UZH');
# inserting a professor with non-existing university IDs violates the foreign key constraint
