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
