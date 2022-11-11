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
### SQL in a nutshell
"""Which of the following queries returns a table of tail numbers and destinations for flights that lasted more than 10 hours?"""
# ANSW: SELECT dest, tail_num FROM flights WHERE air_time > 600;
#|
#|
### SQL in a nutshell (2)
"""What information would this query get?"""
"""         SELECT AVG(air_time) / 60 FROM flights
            GROUP BY origin, carrier;           """
# ANSW: The average length of each airline's flights from SEA and from PDX in hours.
#|
#|
### Filtering Data
