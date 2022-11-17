"""
Type CASTs
In the video, you saw that type casts are a possible solution for data type issues. If you know that a certain column stores numbers as text, you can cast the column to a numeric form, i.e. to integer.

SELECT CAST(some_column AS integer)
FROM table;
Now, the some_column column is temporarily represented as integer instead of text, meaning that you can perform numeric calculations on the column.

Instructions
100 XP
- Execute the given sample code.
- As it doesn't work, add an integer type cast at the right place and execute it again.

"""
#-- Calculate the net amount as amount + fee
#-- fee wasn't integer
#-- saw that w/     SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'transactions';
SELECT transaction_date, amount + CAST(fee AS integer) AS net_amount 
FROM transactions;
