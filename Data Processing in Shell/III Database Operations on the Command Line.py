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

#....................................................
