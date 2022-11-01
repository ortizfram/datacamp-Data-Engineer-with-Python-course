"""
 utilize the command line library csvkit to convert, preview, filter and manipulate files to prepare our data for further analyses.
"""

## THEO============================================
## Getting started with csvkit
## ---------------------------
"""   ** CSVKIT : suit of command-line tools
                  offers data cleaning/priocessing on CSV files
                  Rival with SQL      """
## Installation of csvkit
"""             using pip : pip install csvkit    // pip  install --upgrade csvkit """

##  Convert files into csv  csvkit
""" files into csv :  >>>>>> in2csv
    eg:   in2csv SpotifyData.xlsl > SpotifyData.csv   """
##  Convert files into CSV xpages
""" other pages into csv : >>>>>> --names or --n
                           >>>>>> --sheet
    cat but from csvkit package : >>>>>> csvlook
    descriptive stats oin csv file : >>>>>> csvstat 
    
   eg :  in2csv SpotifyData.xlsx --sheet "worksheet1_Popularity" > SpotifyData.csv
   eg2 : csvlook Spotify_Popularity.csv
   eg3 : csvstat Spotify_Popularity   """
#..................................................


## EXECISES===================
## Installation and documentation for csvkit
""" Upgrade csvkit using pip  """
# pip install --upgrade csvkit 
""" Upgrade csvkit using pip  """
# pip install --upgrade csvkit
""" Print manual for in2csv """
# in2csv -h
""" Print manual for csvlook """
# csvlook -h



## Converting and previewing data with csvkit
""" Use ls to find the name of the zipped file """
 # ls
""" Use Linux's built in unzip tool to unpack the zipped file """
 # unzip SpotifyData.zip
""" Check to confirm name and location of unzipped file """
 # ls
""" Convert SpotifyData.xlsx to csv"""
 # in2csv SpotifyData.xlsx > SpotifyData.csv
""" Print a preview in console using a csvkit suite command """
 # csvlook SpotifyData.csv 
 
 
 
## File conversion and summary statistics with csvkit
""" Check to confirm name and location of the Excel data file """
 # ls
""" Convert sheet "Worksheet1_Popularity" to CSV """
 # in2csv SpotifyData.xlsx --sheet "Worksheet1_Popularity" > Spotify_Popularity.csv
""" Print high level summary statistics for each column """
 # csvstat Spotify_Popularity.csv 
#-------
""" Check to confirm name and location of the Excel data file """
 # ls
""" Convert sheet "Worksheet2_MusicAttributes" to CSV """
 # in2csv SpotifyData.xlsx --sheet "Worksheet2_MusicAttributes" > Spotify_MusicAttributes.csv
""" Check to confirm name and location of the Excel data file """
 # ls
""" Convert sheet "Worksheet2_MusicAttributes" to CSV """
 # in2csv SpotifyData.xlsx --sheet "Worksheet2_MusicAttributes" > Spotify_MusicAttributes.csv
""" Check to confirm name and location of the new CSV file """
 # ls
""" Print preview of Spotify_MusicAttributes """
 # csvlook Spotify_MusicAttributes.csv
 #..............................................................
 
 
 ## THEO=======================
 ## Filtering data using csvkit
 ## ---------------------------
 """  return names of all columns  :  >>>>>> --names or -n
      view documentation  :  >>>>>> -h
      
      filter data CSVKIT using [column name/position] :  >>>>>> csvcut
                                                  -n :  return all names
                                                  -c :  filter by position:  [-c 2,3] or [-c "column_name","asd"]
                                                  
                                                  ---eg  :  # Return all names of file :
                                                            csvcut -n Spotify_MusicAttributes.csv    
                                                            
      filter data by row value CSVKIT  :  >>>>>> csvgrep
                                         -m :   exact row value to filter
                                         -r :   regex patten 
                                         -f :   path to a file      
                                         
                                         ---eg : # Filter for row(s) where track_id = 118GQ70Sp6pMqn6w1oKuki
                                                 csvgrep -c "track_id" -m 118GQ70Sp6pMqn6w1oKuki Spotify_MusicAttributes.csv  """
## EXERCISES=======================
### Printing column headers with csvkit
""" Check to confirm name and location of data file"""
 # ls
""" Print a list of column headers in data file """
 # csvcut -n Spotify_MusicAttributes.csv
"""output | potify_MusicAttributes.csv  backup  bin
  1: track_id
  2: danceability
  3: duration_ms
  4: instrumentalness
  5: loudness
  6: tempo
  7: time_signature"""



### Filtering data by column with csvkit
""" Print a list of column headers in the data """
# csvcut -n Spotify_MusicAttributes.csv
""" Print the first column, by position """
# csvcut -c 1 Spotify_MusicAttributes.csv
""" Print the first, third, and fifth column, by position """
# csvcut -c 1,3,5 Spotify_MusicAttributes.csv        
""" Print the first column, by name """
# csvcut -c "track_id" Spotify_MusicAttributes.csv  
""" Print the track id, song duration, and loudness, by name """
# csvcut -c "track_id","duration_ms","loudness" Spotify_MusicAttributes.csv



### Filtering data by row with csvkit
""" ** filtering data by exact row values using [-m]. Whether it's text or numeric, [csvgrep] can help us filter by these values. """

""" Filter for row(s) where track_id = 118GQ70Sp6pMqn6w1oKuki """
# csvgrep -c "track_id" -m 118GQ70Sp6pMqn6w1oKuki Spotify_MusicAttributes.csv
""" Filter for row(s) where danceability = 0.812 """
# csvgrep -c "danceability" -m 0.812 Spotify_MusicAttributes.csv
