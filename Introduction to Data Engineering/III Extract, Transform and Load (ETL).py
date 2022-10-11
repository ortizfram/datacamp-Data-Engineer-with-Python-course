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
