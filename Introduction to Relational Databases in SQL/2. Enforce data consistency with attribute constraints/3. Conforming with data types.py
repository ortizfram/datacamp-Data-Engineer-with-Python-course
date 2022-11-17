"""
Conforming with data types
For demonstration purposes, I created a fictional database table that only holds three records. The columns have the data types date, integer, and text, respectively.

CREATE TABLE transactions (
 transaction_date date, 
 amount integer,
 fee text
);
Have a look at the contents of the transactions table.

The transaction_date accepts date values. According to the PostgreSQL documentation, it accepts values in the form of YYYY-MM-DD, DD/MM/YY, and so forth.

Both columns amount and fee appear to be numeric, however, the latter is modeled as text – which you will account for in the next exercise.

Instructions
100 XP
Execute the given sample code.
As it doesn't work, have a look at the error message and correct the statement accordingly – then execute it again.

"""
#-- Let's add a record to the table
INSERT INTO transactions (transaction_date, amount, fee) 
VALUES ('2018-09-24', 5454, '30');

#-- Doublecheck the contents
SELECT *
FROM transactions;
