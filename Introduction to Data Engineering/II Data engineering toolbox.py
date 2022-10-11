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
#Star schema diagram
"""Which of the following images is a star schema?
*option b """

#---
#Why parallel computing?
"""Which of these statements is not correct?

ok    1 Parallel computing can be used to speed up any task.
      2 computing can optimize the use of multiple processing units.
      3 Parallel computing can optimize the use of memory between several machines. 
      
(ome tasks might be too small to benefit from parallel computing due to the communication overhead.)"""

#---
#From task to subtasks 
"""multiprocessor.Pool API which allows you to distribute your workload over several processes. """
# to apply a function over multiple cores
@print_timing
def parallel_apply(apply_func, groups, nb_cores):
    with Pool(nb_cores) as p:
        results = p.map(apply_func, groups)
    return pd.concat(results)

# Parallel apply using 1 core
parallel_apply(take_mean_age, athlete_events.groupby('Year'), 1)

# Parallel apply using 2 cores
parallel_apply(take_mean_age, athlete_events.groupby('Year'), 2)

# Parallel apply using 4 cores
parallel_apply(take_mean_age, athlete_events.groupby('Year'), 4)

#---
#Using a DataFrame . dask from pandas
""" parallelize an apply over several groups, is using the dask framework and its abstraction of the pandas DataFrame"""
# import dask.dataframe 
import dask.dataframe as dd 

# Set the number of partitions
athlete_events_dask = dd.from_pandas(athlete_events, npartitions=4)

# Calculate the mean Age per Year .compute()
print(athlete_events_dask.groupby('Year').Age.mean().compute())

#---
#Spark, Hadoop and Hive
"""Classify the cards to the corresponding software project.
- Hadoop
      HDFS is part of it
      MapReduce is part of it
      Collection of Open-source packages for BigData
- PySpark
      Python interface for Spark Framework
      Uses Dataframe Abstraction
- Hive
      Built from need to use structures queries for pararell processing
      Initially used Hadoop MapReduce                                                        """                                                                                                                                                                                                                                                         
      
