"""
Focus on database operations we can do on the command line, including table creation, data pull, and various ETL transformation.
"""
## THEO =================================
### Pulling data from database
"""  excecute a query, outputs result to csv file :  >>>>>> sql2csv

                                           syntax :  sql2csv --db "sqlite://SpotifyDatabase.db" \
                                                             --query "SELECT * FROM Spotify_Popularity" \
                                                             > Spotify_Popularity.csv
                                                             
                                          options: sqlite:// -----  end w/ .db
                                                   postgres:// or mysql:// -----   end w/ NO .db        """
#.................................................

## EXECISES ==================================
### Using sql2csv documentation
"""---Which optional argument in sql2csv will print detailed tracebacks and logs when errors occur while using sql2csv?"""
# -v or --verbose



### Understand sql2csv connectors
"""---what SQL database connections are currently NOT supported for sql2csv and for the rest of the csvkit suite?
   ** Pull up the documentation using csvsql -h   """
# MongoDB



### Practice pulling data from database
# Verify database name 
ls
# Pull the entire Spotify_Popularity table and print in log
sql2csv --db "sqlite:///SpotifyDatabase.db" \
        --query "SELECT * FROM Spotify_Popularity" \
#---
# Verify database name 
ls
# Query first 5 rows of Spotify_Popularity and print in log
sql2csv --db "sqlite:///SpotifyDatabase.db" \
        --query "SELECT * FROM Spotify_Popularity LIMIT 5" \
        | csvlook       
#---
# Verify database name 
ls
# Save query to new file Spotify_Popularity_5Rows.csv
sql2csv --db "sqlite:///SpotifyDatabase.db" \
        --query "SELECT * FROM Spotify_Popularity LIMIT 5" \
        > Spotify_Popularity_5Rows.csv
# Verify newly created file
ls
# Print preview of newly created file
csvlook Spotify_Popularity_5Rows.csv


## THEO ===============================
### Manipulating data using SQL syntax
"""  prettier prinout of csvsql :  >>>>>> csvsql

                                           how :  attatch pipe csvlook to the end   | csvlook
                                                             
                                           eg: csvsql --query "SELECT * FROM Spotify_MusicAttributes LIMIT 1" \
                                               data/Spotify_MusicAttributes.csv > OneSoneFile.csv                
                                               
      Cleaner scripting via shell variables : include variable >>>>>> '$variable_name'               """
#....................................................


## EXERCISES ===========================
### Applying SQL to a local CSV file
# Preview CSV file
ls
# Apply SQL query to Spotify_MusicAttributes.csv
csvsql --query "SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1" Spotify_MusicAttributes.csv 
#---2
# Reformat the output using csvlook 
csvsql --query "SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1" \
	Spotify_MusicAttributes.csv | csvlook
#---3
# Re-direct output to new file: ShortestSong.csv
csvsql --query "SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1" \
	Spotify_MusicAttributes.csv > ShortestSong.csv
# Preview newly created file 
csvlook ShortestSong.csv



### Cleaner scripting via shell variables
# Preview CSV file
ls
# Store SQL query as shell variable
sqlquery="SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1"
# Apply SQL query to Spotify_MusicAttributes.csv
csvsql --query "$sqlquery" Spotify_MusicAttributes.csv 



### Joining local CSV files using SQL
""" 1/2
.Question
Explore the data with the commands we have learned so far (e.g. csvstat, csvlook, etc). 
---What is the column that Spotify_MusicAttributes.csv and Spotify_Popularity.csv have in common that can be used as the JOIN key?

## command to see column names of db through shell
 $ csvcut -n Spotify_MusicAttributes.csv
 $ csvcut -n Spotify_Popularity.csv 
 
answer : track_id     
"""

""" 2/2
--Join Spotify_MusicAttributes.csv and Spotify_Popularity.csv together to form a new file Spotify_FullData.csv.
"""
# Store SQL query as shell variable
sql_query="SELECT ma.*, p.popularity FROM Spotify_MusicAttributes ma INNER JOIN Spotify_Popularity p ON ma.track_id = p.track_id"

# Join 2 local csvs into a new csv using the saved SQL
csvsql --query "$sql_query" Spotify_MusicAttributes.csv Spotify_Popularity.csv > Spotify_FullData.csv

# Preview newly created file
csvstat Spotify_FullData.csv


## THEO=============================
### Pushing data back to database.
"""                     --insert : creates table, inserts data into table only if --db is specified.
                        --no-inference : disable type inference when parsing input.(treats avery column as text)
                        --no-contraints : generates schemma w/o lenght limits or null checks.(no error when null data)

                        syntax : csvsql --db "sqlite:///SpotifyDatabase.db" \
                                        --insert Spotify_MusicAttributes.csv                """
#................................................


## EXERCISES========================
### Practice pushing data back to database
"""
Instructions
100 XP

-Upload Spotify_MusicAttributes.csv as its own table in the SQLite database SpotifyDatabase.
-Re-pull the data from the newly created table Spotify_MusicAttributes in the SQLite database SpotifyDatabase.

"""
# Preview file
ls

# Upload Spotify_MusicAttributes.csv to database
csvsql --db "sqlite:///SpotifyDatabase.db" --insert Spotify_MusicAttributes.csv

# Store SQL query as shell variable
sqlquery="SELECT * FROM Spotify_MusicAttributes"

# Apply SQL query to re-pull new table in database
sql2csv --db "sqlite:///SpotifyDatabase.db" --query "$sqlquery" 




### Database and SQL with csvkit
""" 1/3
-Download the entire table SpotifyMostRecentData from the SQLite database SpotifyDatabase and save it as a csv file locally as SpotifyMostRecentData.csv.
"""
# Store SQL for querying from SQLite database 
sqlquery_pull="SELECT * FROM SpotifyMostRecentData"

# Apply SQL to save table as local file 
sql2csv --db "sqlite:///SpotifyDatabase.db" --query "$sqlquery_pull" > SpotifyMostRecentData.csv

""" 2/3
-Manipulate the two local csv files SpotifyMostRecentData.csv and Spotify201812.csv by passing in the stored UNION ALL SQL 
 query into csvsql. Save the newly created file as UnionedSpotifyData.csv.
"""
# Store SQL for querying from SQLite database 
sqlquery_pull="SELECT * FROM SpotifyMostRecentData"

# Apply SQL to save table as local file 
sql2csv --db "sqlite:///SpotifyDatabase.db" --query "$sqlquery_pull" > SpotifyMostRecentData.csv

# Store SQL for UNION of the two local CSV files
sqlquery_union="SELECT * FROM SpotifyMostRecentData UNION ALL SELECT * FROM Spotify201812"

# Apply SQL to union the two local CSV files and save as local file
csvsql 	--query "$sqlquery_union" SpotifyMostRecentData.csv Spotify201812.csv > UnionedSpotifyData.csv

""" 3/3
-Push the newly created csv file UnionedSpotifyData.csv back to database SpotifyDatabase as its own table.
"""
# Store SQL for querying from SQLite database 
sqlquery_pull="SELECT * FROM SpotifyMostRecentData"

# Apply SQL to save table as local file 
sql2csv --db "sqlite:///SpotifyDatabase.db" --query "$sqlquery_pull" > SpotifyMostRecentData.csv

# Store SQL for UNION of the two local CSV files
sqlquery_union="SELECT * FROM SpotifyMostRecentData UNION ALL SELECT * FROM Spotify201812"

# Apply SQL to union the two local CSV files and save as local file
csvsql 	--query "$sqlquery_union" SpotifyMostRecentData.csv Spotify201812.csv > UnionedSpotifyData.csv

# Push UnionedSpotifyData.csv to database as a new table
csvsql --db "sqlite:///SpotifyDatabase.db" --insert UnionedSpotifyData.csv
