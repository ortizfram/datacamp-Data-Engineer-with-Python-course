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
           >>>>>>>> create_engine()  ===makes engine to handle db connections ==== takes string URL of db to connect to 
           >>>>>>>> sqlite:///filename.db ===SQLite URL Format 
                  ## Query db
           >>>>>>>> pd.read_sql(query, engine) ===to pull data/ load in data
           >>>>>>>> query->table name  ===to load whole table

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
            
            >>>>>>>>> describe()======= view summary statistics
            >>>>>>>>> (query) WHERE 
            >>>>>>>>> (query) OR 
            >>>>>>>>> (query) AND 
            
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

#--- Selecting rows == a graph of safety call per city 
# Create query to get hpd311calls records about safety
query = """
SELECT *
FROM hpd311calls
WHERE complaint_type=='SAFETY';
"""

# Query the database and assign result to safety_calls
safety_calls = pd.read_sql(query, engine)

# Graph the number of safety calls by borough(city)
call_counts = safety_calls.groupby('borough').unique_key.count()
call_counts.plot.barh()
plt.show()
#``````````````````````````````````````````````````````````````````````````````````````````````````````

#--- Filtering on multiple conditions
# Create query for records with max temps <= 32 or snow >= 1
query = """
SELECT *
  FROM weather
  WHERE tmax <= 32
  OR snow >= 1;
"""

# Query database and assign result to wintry_days
wintry_days = pd.read_sql(query, engine)

# View summary stats about the temperatures
print(wintry_days.describe())
"""***************************************************************************************************
more complex Queries
====================
            getting DISTINT Values
            =======================
            >>>>>>>>> SELECT DISTINCT ====remove duplicates
            SELECT DISTINCT [column_names] FROM [table];
            >>>>>>>> SELECT DISTINCT * FROM table;===== Remove duplicate records/ leave uniques
            
            # Get unique street addresess and boroughs
            SELECT DISTINCT incidents_address,
                            borough
                  FROM hpd311calls;
            
            Aggregate funcitons (query db for descriptive statistics)
            ===================
           >>>>>>>>> SUM,  >>>>>>>>>AVG,  >>>>>>>>>MAX,  >>>>>>>>>MIN, 
           >>>>>>>>>COUNT
             # get num of rows that meet query conditions
             SELECT COUNT(*) FROM [table_name]
             # get num of unique values in column 
             SELECT COUNT(DISTINCT [col_names] FROM [table_name];
             
           >>>>>>>>>GROUP BY
             ### Counting by groups
             # create engine to manage db connection
              engine = create_engine("sqlite:///data.db")
              
             # Counting by groups
              query= '''SELECT borough,
                       COUNT(*)
               FROM hpd311calls
               WHERE complaint_type = 'PLUMBING'
               GROUP BY borough;'''
               
             # Query db
              plumbing_call_counts = pd.read_sql(query, engine)
              print(plumbing_call_counts)
              
             #output:
                  borough   COUNT(*)
              0   BRONX     2016
              1   BROOKLYN  2702......
****************************************************************************************************"""

#--- Getting distinct values
# Create query for unique combinations of borough and complaint_type
"""hpd311calls contains data about housing issues, we would expect most records to have a borough(city) listed.
Let's test this assumption by querying unique complaint_type/borough combinations."""

query = """
SELECT DISTINCT borough, 
       complaint_type
  FROM hpd311calls;
"""

# Load results of query to a dataframe
issues_and_boros = pd.read_sql(query,engine)

# Check assumption about issues and boroughs
print(issues_and_boros)
"""output:
          borough    complaint_type
    0           BRONX    HEAT/HOT WATER
    1       MANHATTAN          PLUMBING
    2       MANHATTAN    HEAT/HOT WATER
    3        BROOKLYN    HEAT/HOT WATER"""
#``````````````````````````````````````````````````````````````````````````````````````````````````````

#--- Counting in groups == graph counting issues
# Create query to get call counts by complaint_type
query = """
SELECT complaint_type, 
     COUNT(*)
  FROM hpd311calls
  GROUP BY complaint_type;
"""

# Create dataframe of call counts by issue
calls_by_issue = pd.read_sql(query, engine)

# Graph the number of calls for each housing issue
calls_by_issue.plot.barh(x="complaint_type")
plt.show()
