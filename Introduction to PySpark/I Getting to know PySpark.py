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

