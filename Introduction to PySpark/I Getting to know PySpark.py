"""
how Spark manages data and how can you read and write tables from Python.

\ What is Spark, anyway? /

  | parallel computation | ( split data in clusters )
  
   platform for cluster computing. Spark lets you spread data and computations over clusters with multiple nodes
   Splitting up your data makes it easier to work with very large datasets because each node only works with a small amount of data.
   parallel computation can make certain types of programming tasks much faster.
   
 | Using Spark in Python |
 
    -  cluster: <remote machine connects all nodes>
    -  master : ( main pc ) <manages splitting data and computations>
    -  worker : ( rest of computers in cluster ) <receives calculations, return results>
    
      .  create connection : <SparkContext> class <sc>  #creating an instance of the
      .  attributes : <SparkConf() constructor>
      
 | create SparkSession |
 
      # Import SparkSession 
        > from pyspark.sql import SparkSession

      # create SparkSession builder
        > my_spark = SparkSession.builder.getOrCreate()

      # print spark tables     
        > print(spark.catalog.listTables())

| SparkSession attributes |

     - catalog: extract and view table data
              . listTables() -> returns column names in cluster as list
                > spark.catalog.listTables()
                
| SparkSession methods |

     # always <SparkSessionName>.
    -  .show() ->   print
    -  .sql() ->  run a query ( <takes> queried 'string' <returns> DataFrame results )
    -  .toPandas() ->   returns corresponding 'pandas' DataFrame

"""
#|
#|
### How do you connect to a Spark cluster from PySpark?
# ANSW: Create an instance of the SparkContext class.
#|
#|
### Examining The SparkContext
# Verify SparkContext in environment
print(sc)

# Print Spark version
print(sc.version)
#- <SparkContext master=local[*] appName=pyspark-shell>
#-    3.2.0
#|
#|
"""
\ Using Spark DataFrames /

    . Spark structure : Resilient Distributed Dataset (RDD)
    . behaves :  like a SQL table 
    # DataFrames are more optimized for complicated operations than RDDs.
    
  - create Spark Dataframe: create a  object from your 
      <SparkSession> #interface <'spark'>
      <SparkContext> #connection <'sc'>
"""
#|
#|
### Which of the following is an advantage of Spark DataFrames over RDDs?
# ANSW: Operations using DataFrames are automatically optimized.
#|
#|
### Creating a SparkSession
# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession

# Create my_spark
my_spark = SparkSession.builder.getOrCreate()

# Print my_spark
print(my_spark)
#|
#|
### Viewing tables
# Print the tables in the catalog
print(spark.catalog.listTables())
#|
#|
### Are you query-ious?
# Don't change this query
query = "FROM flights SELECT * LIMIT 10"

# Get the first 10 rows of flights
flights10 = spark.sql(query)

# Show the results
flights10.show()
#|
#|
### Pandafy a Spark DataFrame
# Don't change this query
query = "SELECT origin, dest, COUNT(*) as N FROM flights GROUP BY origin, dest"

# Run the query
flight_counts = spark.sql(query)

# Convert the results to a pandas DataFrame
pd_counts = flight_counts.toPandas()

# Print the head of pd_counts
print(pd_counts.head())
#|
#|
### Put some Spark in your data
