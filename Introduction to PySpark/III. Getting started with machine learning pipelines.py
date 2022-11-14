"""
PySpark has built-in, cutting-edge machine learning routines, along with utilities to create full machine learning pipelines. You'll learn about them in this chapter.

\  Machine Learning Pipelines  /

   > summodule:  pyspark.ml 
    - Transformer class
    - Estimator class
    
| methods for ML |    

   # Transformer class
    -  .transform()  ->  takes a DataFrame and returns a new DataFrame +1 column
       -  Bucketizer    -> create discrete bins from a continuous feature
       
   # Estimator class
    - .fit()         -> they return a model object
"""
#|
#|
### Machine Learning Pipelines
""" Which of the following is not true about machine learning in Spark?"""
# ANSW: Spark's algorithms give better results than other algorithms.
#|
#|
### Join the DataFrames
# Rename year column to avoid duplicates
planes = planes.withColumnRenamed('year', 'plane_year')

# Join the DataFrames
model_data = flights.join(planes, on='tailnum', how="leftouter")
"""
|  Data types for ML  |
  
  > change types 
    .cast()   'integer','double'
"""
#|
#|
### Data Types
"""What kind of data does Spark need for modeling?"""
# ANSW: Numeric
#|
#|
### String to integer
# Cast the columns to integers # df.col notation
model_data = model_data.withColumn("arr_delay", model_data.arr_delay.cast('integer'))
model_data = model_data.withColumn("air_time", model_data.air_time.cast('integer'))
model_data = model_data.withColumn("month", model_data.month.cast('integer'))
model_data = model_data.withColumn("plane_year", model_data.plane_year.cast('integer'))
#|
#|
### Create a new column
# Create the column plane_age
# Create the column plane_age
model_data = model_data.withColumn(
    "plane_age", model_data.year - model_data.plane_year)
#|
#|
###
