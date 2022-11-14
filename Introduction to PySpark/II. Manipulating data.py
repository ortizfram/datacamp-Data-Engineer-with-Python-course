"""
pyspark.sql module, which provides optimized data queries to your Spark session.

| Pyspark attributes : manipulation |

      -  .withColumn()  ->    create new column .  <takes> ('new_column', old_col + 1)
      -  df.colName()   ->    extract column name
      
| pyspark methods : manipulation |

      -  spark.table()  ->  create df containing values of table in the .catalog
      -  .filter()      ->  like a cut for SQL   
                     > flights.filter("air_time > 120").show()              # return values cut  #(SQL string)
                     > flights.filter(flights.air_time > 120).show()        # return bool
                     
      -  .select()    ->  returns only the columns you specify
        |            > selectNoStr = flights.select(flights.origin, flights.dest, flights.carrier)
        |            > selectStr = flights.select("tailnum", "origin", "dest")
        |            > flights.selectExpr("origin", "dest", "tailnum", "distance/(air_time/60) as avg_speed")
      -  .withColumn()  ->   returns all columns in addition to the defined.
                        ->   create new df column
            -  .withColumnRenamed
                        -> rename columns
      
      -  GroupedData 
      |
      -  .agg()        -> pass an aggregate column expression that uses any of the aggregate functions from the pyspark.sql.functions submodule.
                        # Import pyspark.sql.functions as F
                        > import pyspark.sql.functions as F
            - F.stddev  -> estandard deviation
            
      -  .join()       -> takes three arguments. 1.the second DataFrame to join, 2. on == key column(s) as a string, 3. how == specifies kind of join how="leftouter"
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
# Filter flights by passing a string
long_flights1 = flights.filter("distance > 1000")   # sql string

# Filter flights by passing a column of boolean values
long_flights2 = flights.filter(flights.distance > 1000)

# Print the data to check they're equal
long_flights1.show()
long_flights2.show()
#- same result
#|
#|
### Selecting
# Select the first set of columns
selected1 = flights.select("tailnum", "origin", "dest")

# Select the second set of columns
temp = flights.select(flights.origin, flights.dest, flights.carrier)

# Define first filter
filterA = flights.origin == "SEA"

# Define second filter
filterB = flights.dest == "PDX"

# Filter the data, first by filterA then by filterB
selected2 = temp.filter(filterA).filter(filterB)
#|
#|
### Selecting II
# Define avg_speed
avg_speed = (flights.distance/(flights.air_time/60)).alias("avg_speed")

# Select the correct columns
speed1 = flights.select("origin", "dest", "tailnum", avg_speed)

# Create the same table using a SQL expression
speed2 = flights.selectExpr(
    "origin", "dest", "tailnum", "distance/(air_time/60) as avg_speed")
#|
#|
### Aggregating
# Find the shortest flight from PDX in terms of distance
#  Perform the filtering by referencing the column directly, not passing a SQL string.
flights.filter(flights.origin == "PDX").groupBy().min('distance').show()

# Find the longest flight from SEA in terms of air time
flights.filter(flights.origin == 'SEA').groupBy().max('air_time').show()
#|
#|
### Aggregating II
# Average duration of Delta flights
flights.filter(flights.carrier == "DL").filter(flights.origin == "SEA").groupBy().avg("air_time").show()

# Total hours in the air
flights.withColumn("duration_hrs", flights.air_time/60).groupBy().sum("duration_hrs").show()
#|
#|
### Grouping and Aggregating I
# Group by tailnum
by_plane = flights.groupBy("tailnum")

# Number of flights each plane made
by_plane.count().show()

# Group by origin
by_origin = flights.groupBy("origin")

# Average duration of flights from PDX and SEA
by_origin.avg("air_time").show()
#|
#|
### Grouping and Aggregating II
# Import pyspark.sql.functions as F
import pyspark.sql.functions as F

# Group by month and dest
by_month_dest = flights.groupBy('month','dest')

# Average departure delay by month and destination
by_month_dest.avg('dep_delay').show()

# Standard deviation of departure delay
by_month_dest.agg(F.stddev('dep_delay')).show() # stddev = standard deviation
#|
#|
### joining
"""Which of the following is not true?

Joins combine tables.
Joins add information to a table.
Storing information in separate tables can reduce repetition.
There is only one kind of join."""
# ANSW: There is only one kind of join.
#|
#|
### Joining II
# Examine the data
print(airports.show())

# Rename the faa column
airports = airports.withColumnRenamed('faa', 'dest')

# Join the DataFrames
flights_with_airports = flights.join(airports, on='dest', how='leftouter')

# Examine the new DataFrame
print(flights_with_airports.show())
