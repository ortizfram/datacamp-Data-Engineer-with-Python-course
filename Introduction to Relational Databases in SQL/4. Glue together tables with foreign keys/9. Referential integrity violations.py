"""
Referential integrity violations
Given the current state of your database, what happens if you execute the following SQL statement?

      DELETE FROM universities WHERE id = 'EPF';

Instructions
50 XP
Possible Answers

        It throws an error because the university with ID "EPF" does not exist.
        The university with ID "EPF" is deleted.
        It fails because referential integrity from universities to professors is violated.
   OK   It fails because referential integrity from professors to universities is violated.

"""
SELECT * 
FROM universities 
WHERE id = 'EPF';

DELETE FROM universities WHERE id = 'EPF';

# ERROR : DETAIL:  Key (id)=(EPF) is still referenced from table "professors".
