"""
Identify keys with SELECT COUNT DISTINCT
There's a very basic way of finding out what qualifies for a key in an existing, populated table:

Count the distinct records for all possible combinations of columns. If the resulting number x equals the number of all rows in the table for a combination, you have discovered a superkey.

Then remove one column after another until you can no longer remove columns without seeing the number x decrease. If that is the case, you have discovered a (candidate) key.

The table professors has 551 rows. It has only one possible candidate key, which is a combination of two attributes. You might want to try different combinations using the "Run code" button. Once you have found the solution, you can submit your answer.

Instructions
100 XP
- Using the above steps, identify the candidate key by trying out different combination of columns.

"""
#-- Try out different combinations 
#-- Identify keys w/ SELECT COUNT DISTINCT
SELECT COUNT(DISTINCT(firstname, lastname)) 
FROM professors;
'''
count
551
'''
