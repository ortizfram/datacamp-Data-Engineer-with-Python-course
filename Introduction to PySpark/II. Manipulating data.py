"""
pyspark.sql module, which provides optimized data queries to your Spark session.

| Pyspark attributes : manipulation |

      -  .withColumn()  ->    create new column .  <takes> ('new_column', old_col + 1)
      -  df.colName()   ->    extract column name
      
| pyspark methods : manipulation |

      -  spark.table()  ->  create df containing values of table in the .catalog
"""
#|
#|
### Creating columns
# Create the DataFrame flights
flights = spark.table('flights') # create table 'name'

# Show the head
flights.show() # head() is default

# Add duration_hrs from air_time
flights = flights.withColumn('duration_hrs', flights.air_time /60)
#|
#|
"""
\ SQL in a nutshell /
