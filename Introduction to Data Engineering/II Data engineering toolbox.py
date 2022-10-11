"""***********************************************************************************************************
explore the data engineer's toolbox! Learn in detail about different types of databases data engineers use,
how parallel computing is a cornerstone of the data engineer's toolkit, and how to schedule data processing
jobs using scheduling frameworks.
**************************************************************************************************************"""
#---
#SQL vs NoSQL
"""Classify the cards into the correct bucket 
- SQL
      MySQL
      PostgreSQL
      Has a DB Schema
      Customer's data stores in a data-base
- NoSQL
      MongoDB
      Schemaless
      Caching layer in distributed web server  
      """
#---
#The database schema
# Complete the SELECT statement
data = pd.read_sql("""
SELECT first_name, last_name FROM "Customer" 
ORDER BY last_name, first_name
""", db_engine) #add db name

# Show the first 3 rows of the DataFrame
print(data.head(3))

# Show the info of the DataFrame
print(data.info())

#---
#Joining on relations
# Complete the SELECT statement
data = pd.read_sql("""
SELECT * FROM "Customer"
INNER JOIN "Order"
ON "Order"."id"="Customer"."id"
""", db_engine)

# Show the id column of data
print(data.info())

#---
#Joining on relations, joins the "Customer" with the "Order" table.
# Complete the SELECT statement
data = pd.read_sql("""
SELECT * FROM "Customer"
INNER JOIN "Order"
ON "Order"."customer_id"="Customer"."id"
""", db_engine)

# Show the id column of data
print(data.id)

#---
#
