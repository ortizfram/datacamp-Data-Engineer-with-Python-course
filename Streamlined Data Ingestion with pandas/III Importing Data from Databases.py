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
# Create the database engine
engine = create_engine("sqlite:///data.db")

# Create a SQL query to load the entire weather table
query = """
SELECT * 
  FROM weather;
"""

# Load weather with the SQL query
weather = pd.read_sql(query, engine)

# View the first few rows of data
print(weather.head())
"""output:
station                         name  latitude  longitude  elevation  ... prcp snow  tavg  tmax  tmin
0  USW00094728  NY CITY CENTRAL PARK, NY US    40.779    -73.969       42.7  ...  0.0  0.0          52    42
1  USW00094728  NY CITY CENTRAL PARK, NY US    40.779    -73.969       42.7  ...  0.0  0.0          48    39
2  USW00094728  NY CITY CENTRAL PARK, NY US    40.779    -73.969       42.7  ...  0.0  0.0          48    42"""

"""****************************************************************************************************
Refining imports with Queries
=============================
    WHERE, AND,OR filtering text, and filtering numbers
        
           # Load pandas  and alchemy's create_engine
           import pandas as pd
           from alchemy import create_engine
           
           # create engine to manage db connection
           engine = create_engine("sqlite:///data.db")
           # Write query to get records from brookling
           quey= """SELECT *
                    FROM hpd311calls
                    WHERE borough = 'BROOKLYN'; """
           
           # Query db
           brooklyn_calls = pd.read_sql(query, engine)
           print(brooklyn_calls.borough.unique())
           #````````````````````````````````````````````
     
           # Write query to get records from brookling
           and_query= """SELECT *
                    FROM hpd311calls
                    WHERE borough = 'BRONX'
                    AND complaint_type = 'PLUMBING'; """
           # Get calls about plumbing issues in the Bronx
           bx_plumbing_calls = pd.read_sql(and_query, engine)
           # Check redord count
           print(bx_plumbing_calls.shape)
           (2016, 8)
****************************************************************************************************""" 
          
# Create database engine for data.db
engine = create_engine("sqlite:///data.db")

# Write query to get date, tmax, and tmin from weather
query = """
SELECT date, 
       tmax, 
       tmin
  FROM weather;
"""
# Make a dataframe by passing query and engine to read_sql()
temperatures = pd.read_sql(query, engine)

# View the resulting dataframe
print(temperatures)
"""output:
       date  tmax  tmin
0  12/01/2017    52    42
1  12/02/2017    48    39
2  12/03/2017    48    427"""
#``````````````````````````````````````````````````````````````````````````````````````````````````````

#---
