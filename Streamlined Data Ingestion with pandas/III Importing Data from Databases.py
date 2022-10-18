"""****************************************************************************************************
This chapter features introductory SQL topics like WHERE clauses, aggregate functions, and basic joins.

  @@@ RELATIONAL databases
      ====================
            - Organized into tables
            - Rows or records represents instance of an entity
            - Columns of attributes
            - Tables linked via Keys
            - Support more data, multiple simultaneous users and data quality controls
            - Data types specified/enforced for each column
            - Interact with them via SQL 
            
            SQL Lite
            ========
            SQL Lite databases stored as regular, self-contained computer files. Great for sharing data
  
            Reading data/ Connecting to databases     
            ====================================      
            - Create a way to connect to the db
            - Query
            
                  SQL Alchemy library
                  ====================
                  ## db connection with engine
                  create_engine()       >>>>>>>> makes engine to handle db connections ==== takes string URL of db to connect to 
                  sqlite:///filename.db >>>>>>>> SQLite URL Format 
                  ## Query db
                  pd.read_sql(query, engine) >>>>>>>> to pull data/ load in data
                  query->table name >>>>>>>> to load whole table
                  
                  SQL Syntax (Line ENds with ;)
                  ==========
                  ## Basic SQL Syntax
                  SELECT [column_names] FROM [table_name];
                  ## Get all data in table 
                  SELECT * FROM [table_name];
                  
           Getting data from a database
           ============================
           # Load pandas  and alchemy's create_engine
           import pandas as pd
           from alchemy import create_engine
           
           # create engine to manage db connection
           engine = create_engine("sqlite:///data.db")
           
           # Load entire table 2 ways (just table_name, or SELECT)
           weather = pd.read_sql("weather", engine)
           weather = pd.read_sql("SELECT * FROM weather", engine)
****************************************************************************************************"""

#--- Connect to a database 1
# Import sqlalchemy's create_engine() function
from sqlalchemy import create_engine      
#``````````````````````````````````````````````````````````````````````````````````````````````````````

#--- Connect to a database 2
# Import sqlalchemy's create_engine() function
from sqlalchemy import create_engine

# Create the database engine
engine = create_engine("sqlite:///data.db")

# View the tables in the database
print(engine.table_names())
"""output:
['boro_census', 'hpd311calls', 'weather']"""
#``````````````````````````````````````````````````````````````````````````````````````````````````````

#--- Load entire tables
# Load libraries
import pandas as pd
from sqlalchemy import create_engine

# Create the database engine
engine = create_engine('sqlite:///data.db')

# Load hpd311calls without any SQL
hpd_calls = pd.read_sql("hpd311calls", engine)

# View the first few rows of data
print(hpd_calls.head())
"""output:
unique_key created_date agency  complaint_type incident_zip      incident_address community_board    borough
0   38070822   01/01/2018    HPD  HEAT/HOT WATER        10468    2786 JEROME AVENUE        07 BRONX      BRONX
1   38065299   01/01/2018    HPD        PLUMBING        10003  323 EAST   12 STREET    03 MANHATTAN  MANHATTAN
2   38066653   01/01/2018    HPD  HEAT/HOT WATER        10452  1235 GRAND CONCOURSE        04 BRONX      BRONX"""
#``````````````````````````````````````````````````````````````````````````````````````````````````````

#--- Load entire tables 2 
