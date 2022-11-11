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
        |             
      -  .withColumn()  ->   returns all columns in addition to the defined.
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
