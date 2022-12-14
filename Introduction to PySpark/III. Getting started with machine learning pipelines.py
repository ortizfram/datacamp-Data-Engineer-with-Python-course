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
### Making a Boolean
# Create is_late bool
model_data = model_data.withColumn("is_late", model_data.arr_delay >0)

# Convert to an integer w/ .cast()
model_data = model_data.withColumn("label", model_data.is_late.cast('integer'))

# Remove missing values w/ SQL string
model_data = model_data.filter("arr_delay is not NULL and dep_delay is not NULL and air_time is not NULL and plane_year is not NULL")
#|
#|
"""
\  Strings and Factors  /

   > pyspark.ml.features submodule
    'one-hot vectors'      -> all elements are zero except for at most one element, which has a value of one (1).
    
    1 > create a 'StringIndexer'.
            carr_indexer = StringIndexer(inputCol='carrier',outputCol='carrier_index')
    2 > encode w/ 'OneHotEncoder'.
            carr_encoder = OneHotEncoder(inputCol='carrier_index',outputCol='carrier_fact')
    3 > 'Pipeline' will take care of the rest.
            # Fit and transform the data
            piped_data = flights_pipe.fit(model_data).transform(model_data)
    -----------------------
      > 'VectorAssembler'  -> combine all of the columns containing our features into a single column
                          inputCol= ['column_name1','c2','c3']
                          outputCol= 'features'
"""
#|
#|
###
"""Why do you have to encode a categorical feature as a one-hot vector?"""
# ANSW: Spark can only model numeric features.
#|
#|
### Carrier
# Create a StringIndexer
carr_indexer = StringIndexer(imputCol='carrier',outputCol='carrier_index')

# Create a OneHotEncoder
carr_encoder = OneHotEncoder(imputCol='carrier_index',outputCol='carrier_fact')
#|
#|
### Destination
# Create a StringIndexer
dest_indexer = StringIndexer(inputCol='dest',outputCol='dest_index')

# Create a OneHotEncoder
dest_encoder = OneHotEncoder(inputCol='dest_index',outputCol='dest_fact')
#|
#|
### Assemble a vector
# Make a VectorAssembler
vec_assembler = VectorAssembler(inputCols=["month", "air_time", "carrier_fact", "dest_fact", "plane_age"], outputCol='features')
#|
#|
""" \ create pipelines  /
      
      > Import Pipeline
         from pyspark.ml import pipeline
      > stages
         
"""
#|
#|
### Create the pipeline
# Import Pipeline
from pyspark.ml import Pipeline

# Make the pipeline
flights_pipe = Pipeline(stages=[dest_indexer, dest_encoder, carr_indexer, carr_encoder, vec_assembler])
#|
#|
### Test vs. Train
""" why important to set 'model evaluation'?"""
# ANSW: By evaluating your model with a test set you can get a good idea of performance on new data.
#|
#|
### Transform the data
# Fit and transform the data
piped_data = flights_pipe.fit(model_data).transform(model_data)
#|
#|
### Split the data
# Split the data into training and test sets
# training with 60% of the data, and test with 40%
training, test = piped_data.randomSplit([.6, .4])
