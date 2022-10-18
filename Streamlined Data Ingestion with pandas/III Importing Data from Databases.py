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
           engine = create_engine("sqlite:///"data.db")
           
           # Load entire table 2 ways (just table_name, or SELECT)
           weather = pd.read_sql("weather", engine)
           weather = pd.read_sql("SELECT * FROM weather", engine)
****************************************************************************************************"""
                  
