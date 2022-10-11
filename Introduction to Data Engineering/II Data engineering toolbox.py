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
      
#---
#A PySpark groupby
"""The methods you're going to use in this exercise are:
            .printSchema(): helps print the schema of a Spark DataFrame.
            .groupBy(): grouping statement for an aggregation.
            .mean(): take the mean over each group.
            .show(): show the results."""
# Print the type of athlete_events_spark
print(type(athlete_events_spark))

# Print the schema of athlete_events_spark
print(athlete_events_spark.printSchema())

# Group by the Year, and find the mean Age
print(athlete_events_spark.groupBy('Year').mean('Age'))

# Group by the Year, and find the mean Age
print(athlete_events_spark.groupBy('Year').mean('Age').show())

#---
#Running PySpark files
"""spark-submit. This tool can help you submit your application to a spark cluster.

spark-submit \
  --master local[4] \
  /home/repl/spark-script.py
  
    
            1 An error.
      ok    2 A DataFrame with average Olympian heights by year.
            3 A DataFrame with Olympian ages.                                                                                                                                 """


#---
# Airflow, Luigi and cron
"""There's a lot of useful features in Airflow, but can you select the feature from the list below which is also provided by cron?

            1 You can program your workflow in Python.
            2 You can use a directed acyclic graph as a model for dependency resolving.                                                                    
     ok     3 You have exact control over the time at which jobs run.                                                                """                                                                                                                        


#---
#Airflow DAGs 1
"""{In Airflow, a pipeline} :
is represented as a Directed Acyclic Graph or DAG.
The nodes of the graph represent tasks that are executed. The directed connections
between nodes represent dependencies between the tasks.
*
First, the DAG needs to run on every hour at minute 0. Fill in the schedule_interval keyword
argument using the crontab notation. For example, every hour at minute N would be N * * * *. Remember, you need to run at minute 0."""
# Create the DAG object
dag = DAG(dag_id="car_factory_simulation",
          default_args={"owner": "airflow","start_date": airflow.utils.dates.days_ago(2)},
          #run at minute 0
          schedule_interval="0 * * * *")

#---
#Airflow DAGs 2
## Create the DAG object
dag = DAG(dag_id="car_factory_simulation",
          default_args={"owner": "airflow","start_date": airflow.utils.dates.days_ago(2)},
          schedule_interval="0 * * * *")

# Task definitions
assemble_frame = BashOperator(task_id="assemble_frame", bash_command='echo "Assembling frame"', dag=dag)
place_tires = BashOperator(task_id="place_tires", bash_command='echo "Placing tires"', dag=dag)
assemble_body = BashOperator(task_id="assemble_body", bash_command='echo "Assembling body"', dag=dag)
apply_paint = BashOperator(task_id="apply_paint", bash_command='echo "Applying paint"', dag=dag)

# Complete the downstream flow
assemble_frame.set_downstream(place_tires)
assemble_frame.set_downstream(assemble_body)
assemble_body.set_downstream(apply_paint)
