"""**********************************************************************************************************************
With ETL (Extract, Transform, Load), you will learn how to extract raw data from various sources, transform this raw data into 
actionable insights, and load it into relevant databases ready for consumption!
    1 Extract from: file/ database/ API
*************************************************************************************************************************"""

#---
#Data sources
"""Select the statement about these topics which is not true

      1 OLTP means the system is optimized for transactions.(OnLine Transaction Processing and is used to identify systems that are good at handling transactions.)
 OK   2 APIs mostly use raw text to transfer data.(mostly use a more structured form of data, for example JSON.)
      3 Row-oriented databases and OLTP go hand-in-hand.(add data row-wise, this means it's easier to do simple INSERT transactions)"""


#---
#////////////////////////EXTRACT///////////////////////////////
#Fetch from an API
"""Hacker News is a social news aggregation website, 
specifically for articles related to computer science or the tech world in general. 
Each post on the website has a JSON representation"""
import requests

# Fetch the Hackernews post
resp = requests.get("https://hacker-news.firebaseio.com/v0/item/16222426.json")

# Print the response parsed as JSON
print(resp.json())

# Assign the score of the test to post_score
post_score = resp.json()["score"]
print(post_score)


#---
#Read from a database
# Function to extract table to a pandas DataFrame
def extract_table_to_pandas(tablename, db_engine):
    query = "SELECT * FROM {}".format(tablename)
    return pd.read_sql(query, db_engine)

# Connect to the database using the connection URI
#example :   "postgresql://user:password@host:port/database" 
connection_uri = "postgresql://repl:password@localhost:5432/pagila" 
db_engine = sqlalchemy.create_engine(connection_uri)

# Extract the film table into a pandas DataFrame
extract_table_to_pandas("film", db_engine)

# Extract the customer table into a pandas DataFrame
extract_table_to_pandas("customer", db_engine)


#---
#///////////////////////TRANSFORM///////////////////////////

#Splitting the rental rate
# Get the rental_rate column as str
rental_rate_str = film_df.rental_rate.astype("str")

# Split up and expand the column
rental_rate_expanded = rental_rate_str.str.split(".", expand=True)

# Assign the columns to film_df
film_df = film_df.assign(
    rental_rate_dollar=rental_rate_expanded[0],
    rental_rate_cents=rental_rate_expanded[1],
)
print(film_df)



#---
# Transformations using PySpark
# option B
spark.read.jdbc("jdbc:postgresql://localhost:5432/pagila",
                "customer", 
                {"user":"repl","password":"password"})
"""****************
<- table name is the second argument and properties the third
*******************"""



#---
# Joining using Pyspark 
""" PySpark DataFrame with films, film_df and the PySpark DataFrame with ratings, rating_df"""
# Use groupBy and mean to aggregate the column
ratings_per_film_df = rating_df.groupBy('film_id').mean('rating')

# Join the tables using the film_id column
film_df_with_ratings = film_df.join(
    ratings_per_film_df,
    film_df.film_id==ratings_per_film_df.film_id
)
# Show the 5 first results
print(film_df_with_ratings.show(5))



#///////////////////LOADING///////////////////////////////////////////////
"""*********************************************************************
analytics DB: agregate queries, column oriented
app DB: lots of transactions, row oriented
MMP: massively pararell processing, split subtasks distributed among several nodes
*********************************************************************"""
""" OLAP: Online analytical processing, OLTP: Online transaction processing"""
# OLAP or OLTP 
""" find the most appropriate statement that is true

        1 Typically, analytical databases are column-oriented.
        2 Massively parallel processing (MPP) databases are usually column-oriented.
        3 Databases optimized for OLAP are usually not great at OLTP operations.
        4 Analytical and application databases have different use cases and should be separated if possible.
        5 None of the above.
  ok    6 All of the above."""


#---
#Writing to a file
""" Apache Parquet file format.
There's a PySpark DataFrame called film_sdf and a pandas DataFrame called film_pdf in your workspace."""
# Write the pandas DataFrame to parquet
film_pdf.to_parquet("films_pdf.parquet")

# Write the PySpark DataFrame to parquet
film_sdf.write.parquet("films_sdf.parquet")




#---
#Load into Postgres
# Finish the connection URI
"""write out some data to a PostgreSQL data warehouse"""
connection_uri = "postgresql://repl:password@localhost:5432/dwh"
db_engine_dwh = sqlalchemy.create_engine(connection_uri)

# Transformation step, join with recommendations data
film_pdf_joined = film_pdf.join(recommendations)

# Finish the .to_sql() call to write to store.film
film_pdf_joined.to_sql("film", db_engine_dwh, schema="store", if_exists="replace")

# Run the query to fetch the data
pd.read_sql("SELECT film_id, recommended_film_ids FROM store.film", db_engine_dwh)



#///////////////////PUT ALL TOGETHER///////////////////////////////////////////////
#--- Defining a DAG
# Define the ETL function
def etl():
    film_df = extract_film_to_pandas()
    film_df = transform_rental_rate(film_df)
    load_dataframe_to_film(film_df)

# Define the ETL task using PythonOperator
etl_task = PythonOperator(task_id='etl_film',
                          python_callable=etl,
                          dag=dag)

# Set the upstream to wait_for_table and sample run etl()
etl_task.set_upstream(wait_for_table)
etl()


#--- Setting up Airflow dag"
"""CONSOLE :
repl:~$ echo $AIRFLOW_HOME
#~/airflow
repl:~$ ls
# airflow  config  datasets   requirements.txt  startup
# chown    dag.py  repl:repl  start.sh          workspace
repl:~$ cd airflow/
repl:~/airflow$ ls
# airflow.cfg      airflow.db             dags  unittests.cfg
# airflow.cfg.bak  airflow-webserver.pid  logs
repl:~/airflow$ head airflow.cfg
[core]
# The home folder for airflow, default is ~/airflow
airflow_home = /home/repl/airflow

# The folder where your airflow pipelines live, most likely a
# subfolder in a code repository
# This path must be absolute
dags_folder = /home/repl/airflow/dags

# The folder where airflow should store its log files
repl:~/airflow$ cd

#find the folder and move the dag.py file there: mv ./dag.py <dags_folder>.
mv ./dag.py /home/repl/airflow/dags

cd airflow/dags/

ls
# dag.py  dag_recommendations.py  __pycache__
    """
# >>>
"""Which files does the DAGs folder have after you moved the file?

        1 It has one DAG file: dag.py.
 ok     2 It has two DAG files: dag.py and dag_recommendations.py.
        3 It has three DAG files: dag.py, you_wont_guess_this_dag.py, and super_secret_dag.py."""



#--- Interpreting the DAG
"""can you find the scheduled interval of the sample DAG?  
recommendations	0 0 * * *		
sample	0 0 * * *	

     ok 1 Daily at midnight.
        2 Hourly at 0 minutes and 0 seconds.
        3 It runs once at midnight."""
