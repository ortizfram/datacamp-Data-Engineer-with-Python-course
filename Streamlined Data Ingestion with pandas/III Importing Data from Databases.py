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
#``````````````````````````````````````````````````````````````````````````````````````````````````````

#--- Working with aggregate functions 1
# Create a query to get month and max tmax by month
query = """
SELECT month, 
       MAX(tmax)
  FROM weather 
  GROUP BY month;"""

# Get dataframe of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)
"""output:
     month  MAX(tmax)
0  December         61
1  February         78
2   January         61
3     March         62"""
#``````````````````````````````````````````````````````````````````````````````````````````````````````
#--- Working with aggregate functions 2
# Create a query to get month, max tmax, and min tmin by month
query = """
SELECT month, 
	      MAX(tmax), 
        MIN(tmin)
FROM weather 
GROUP BY month;
"""

# Get dataframe of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)
"""output:
   month  MAX(tmax)  MIN(tmin)
0  December         61          9
1  February         78         16
2   January         61          5
3     March         62         27"""
#``````````````````````````````````````````````````````````````````````````````````````````````````````

#--- Working with aggregate functions 3
# Create query to get temperature and precipitation by month
query = """
SELECT month, 
        MAX(tmax), 
        MIN(tmin),
        SUM(prcp)
  FROM weather 
 GROUP BY month;
"""

# Get dataframe of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)
"""output:
	month     MAX(tmax)  MIN(tmin)  SUM(prcp)
    0  December         61          9       2.21
    1  February         78         16       5.83
    2   January         61          5       2.18
    3     March         62         27       5.17"""
"""****************************************************************************************************
Loading multiple tables with joins
==================================
	>>>>>>>>(query) JOIN ====== on table.table_name
	
	# joining weather and filtering complaints
	SELECT *
	FROM hdp311calls
		JOIN weather
		ON hdp311calls.created_date = weather.date;
	WHERE hdp311calls.complaint_type = 'HEAT/HOT WATER';
	
	joining and aggregating
	========================
	# Get call counts by borough and join population and housing counts
	SELECT  hdp311calls.borough,
		COUNT(*),
		boro_census.total_pupulation,
		boro_census.housing_units
	FROM 	hdp311calls
		JOIN 	boro_census
		ON hdp311calls.borough = boro_census_borough	
	GROUP BY  hdp311calls.borough;
	
		
		SQL Order of Keywords
		=====================
		>>>>>>>>> SELECT,  >>>>>>>>>FROM,  >>>>>>>>>JOIN,  >>>>>>>>>WHERE, >>>>>>>>>GROUP BY
****************************************************************************************************"""

#---Joining tables
# Query to join weather to call records by date columns
query = """
SELECT * 
  FROM hpd311calls
  JOIN weather 
  ON hpd311calls.created_date = weather.date;
"""

# Create dataframe of joined tables
calls_with_weather = pd.read_sql(query, engine)

# View the dataframe to make sure all columns were joined
print(calls_with_weather.head())
"""output:
unique_key created_date agency  complaint_type incident_zip  ... prcp snow tavg tmax tmin
0   38070822   01/01/2018    HPD  HEAT/HOT WATER        10468  ...  0.0  0.0        19    7
1   38065299   01/01/2018    HPD        PLUMBING        10003  ...  0.0  0.0        19    7
2   38066653   01/01/2018    HPD  HEAT/HOT WATER        10452  ...  0.0  0.0        19    7
3   38070264   01/01/2018    HPD  HEAT/HOT WATER        10032  ...  0.0  0.0        19    7
4   38072466   01/01/2018    HPD  HEAT/HOT WATER        11213  ...  0.0  0.0        19    7"""
#``````````````````````````````````````````````````````````````````````````````````````````````````````

#---Joining and filtering 1
# Query to get hpd311calls and precipitation values
query = """
SELECT hpd311calls.*, weather.prcp
  FROM hpd311calls
  JOIN weather
  ON hpd311calls.created_date = weather.date;"""

# Load query results into the leak_calls dataframe
leak_calls = pd.read_sql(query,engine)

# View the dataframe
print(leak_calls.head())
#``````````````````````````````````````````````````````````````````````````````````````````````````````

#---Joining and filtering 2 === filter WHERE 'WATER LEAK
# Query to get water leak calls and daily precipitation
query = """
SELECT hpd311calls.*, weather.prcp
  FROM hpd311calls
  JOIN weather
    ON hpd311calls.created_date = weather.date
  WHERE hpd311calls.complaint_type = 'WATER LEAK';"""

# Load query results into the leak_calls dataframe
leak_calls = pd.read_sql(query, engine)

# View the dataframe
print(leak_calls.head())
#``````````````````````````````````````````````````````````````````````````````````````````````````````

#---Joining, filtering, and aggregating 1
# Query to get heat/hot water call counts by created_date
query = """
SELECT hpd311calls.created_date, 
       COUNT(*)
  FROM hpd311calls 
  WHERE hpd311calls.complaint_type == 'HEAT'
  GROUP BY hpd311calls.created_date;"""

# Query database and save results as df
df = pd.read_sql(query, engine)

# View first 5 records
print(df.head())
#``````````````````````````````````````````````````````````````````````````````````````````````````````

#---Joining, filtering, and aggregating 2
# Modify query to join tmax and tmin from weather by date
"""--count number of calls, saying temp max and min per day.
(There is only one record per date in weather, so we do not need SQL's MAX and MIN functions here.)"""

query = """
SELECT hpd311calls.created_date, 
	   COUNT(*), 
       weather.tmax,
       weather.tmin
  FROM hpd311calls 
       JOIN weather
       ON hpd311calls.created_date = weather.date
 WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER' 
 GROUP BY hpd311calls.created_date;
 """

# Query database and save results as df
df = pd.read_sql(query, engine)

# View first 5 records
print(df.head())
"""output:
 created_date  COUNT(*)  tmax  tmin
0   01/01/2018      4597    19     7
1   01/02/2018      4362    26    13
2   01/03/2018      3045    30    16
3   01/04/2018      3374    29    19
4   01/05/2018      4333    19     9"""
