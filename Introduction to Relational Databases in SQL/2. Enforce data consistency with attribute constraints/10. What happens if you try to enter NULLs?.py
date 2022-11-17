"""
What happens if you try to enter NULLs?
Execute the following statement:

INSERT INTO professors (firstname, lastname, university_shortname)
VALUES (NULL, 'Miller', 'ETH');
- Why does this throw an error?
. Possible Answers

        Professors without first names do not exist
 OK     Because a database constraint is violated.
        Error? This works just fine.
        NULL is not put in quotes.

"""
