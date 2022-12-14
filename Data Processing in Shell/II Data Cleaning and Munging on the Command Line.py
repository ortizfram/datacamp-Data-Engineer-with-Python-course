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
 pip install --upgrade csvkit 
""" Upgrade csvkit using pip  """
 pip install --upgrade csvkit
""" Print manual for in2csv """
 in2csv -h
""" Print manual for csvlook """
csvlook -h



## Converting and previewing data with csvkit
""" Use ls to find the name of the zipped file """
 ls
""" Use Linux's built in unzip tool to unpack the zipped file """
 unzip SpotifyData.zip
""" Check to confirm name and location of unzipped file """
ls
""" Convert SpotifyData.xlsx to csv"""
 in2csv SpotifyData.xlsx > SpotifyData.csv
""" Print a preview in console using a csvkit suite command """
csvlook SpotifyData.csv 
 
 
 
## File conversion and summary statistics with csvkit
""" Check to confirm name and location of the Excel data file """
ls
""" Convert sheet "Worksheet1_Popularity" to CSV """
in2csv SpotifyData.xlsx --sheet "Worksheet1_Popularity" > Spotify_Popularity.csv
""" Print high level summary statistics for each column """
csvstat Spotify_Popularity.csv 
#-------
""" Check to confirm name and location of the Excel data file """
ls
""" Convert sheet "Worksheet2_MusicAttributes" to CSV """
in2csv SpotifyData.xlsx --sheet "Worksheet2_MusicAttributes" > Spotify_MusicAttributes.csv
""" Check to confirm name and location of the Excel data file """
ls
""" Convert sheet "Worksheet2_MusicAttributes" to CSV """
 in2csv SpotifyData.xlsx --sheet "Worksheet2_MusicAttributes" > Spotify_MusicAttributes.csv
""" Check to confirm name and location of the new CSV file """
ls
""" Print preview of Spotify_MusicAttributes """
csvlook Spotify_MusicAttributes.csv
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
#.................................................

## EXERCISES=======================
### Printing column headers with csvkit
""" Check to confirm name and location of data file"""
ls
""" Print a list of column headers in data file """
csvcut -n Spotify_MusicAttributes.csv
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
csvcut -n Spotify_MusicAttributes.csv
""" Print the first column, by position """
csvcut -c 1 Spotify_MusicAttributes.csv
""" Print the first, third, and fifth column, by position """
csvcut -c 1,3,5 Spotify_MusicAttributes.csv        
""" Print the first column, by name """
csvcut -c "track_id" Spotify_MusicAttributes.csv  
""" Print the track id, song duration, and loudness, by name """
csvcut -c "track_id","duration_ms","loudness" Spotify_MusicAttributes.csv



### Filtering data by row with csvkit
""" ** filtering data by exact row values using [-m]. Whether it's text or numeric, [csvgrep] can help us filter by these values. """

""" Filter for row(s) where track_id = 118GQ70Sp6pMqn6w1oKuki """
csvgrep -c "track_id" -m 118GQ70Sp6pMqn6w1oKuki Spotify_MusicAttributes.csv
""" Filter for row(s) where danceability = 0.812 """
csvgrep -c "danceability" -m 0.812 Spotify_MusicAttributes.csv


## THEO ===========================================
### Stacking data and chaining commands with csvkit
"""  stack up rows from 2 or more files :  >>>>>> csvstack
                                            -g : ...\ group, will insert new columns with values you give (for categories)
                                            -n : name group 
                                             ; : link commands toghether  RUN SEQUENTIALLY
                                             && : link commands together  RUN IF FIRST SUCCEEDS
                                             | : uses the output of command
                                             > : redirects output to an x location
                                             
                                            eg:  csvstack rank6.csv rank7.csv > all_ranks.csv
                                            
                                            eg of -g : csvstack -g "rank6","rank7" -n "source"\
                                                       rank6.csv rank7.csv > all_ranks.csv    
                                            eg2 og -g : # While stacking the 2 files, create a data source column
                                                        csvstack -g "Sep2018","Oct2018" Spotify201809_subset.csv Spotify201810_subset.csv > Spotify_all_rankings.csv
"""
#........................................................................

## EXERCISES ===================================
### Stacking files with csvkit
""" Stack the two files and save results as a new file """
csvstack SpotifyData_PopularityRank6.csv SpotifyData_PopularityRank7.csv > SpotifyPopularity.csv
""" Preview the newly created file """
csvlook SpotifyPopularity.csv



### Chaining commands using operators
""" If csvlook succeeds, then run csvstat """
csvlook Spotify_Popularity.csv && csvstat Spotify_Popularity.csv
""" Use the output of csvsort as input to csvlook """
csvsort -c 2 Spotify_Popularity.csv | csvlook
""" Take top 15 rows from sorted output and save to new file """
csvsort -c 2 Spotify_Popularity.csv | head -n 15 > Spotify_Popularity_Top15.csv
""" Preview the new file """
csvlook Spotify_Popularity_Top15.csv



### Data processing with csvkit
# Convert the Spotify201809 sheet into its own csv file """
in2csv Spotify_201809_201810.xlsx --sheet "Spotify201809" > Spotify201809.csv
# Check to confirm name and location of data file """
ls
# Preview file preview using a csvkit function
csvlook Spotify201809.csv
# Create a new csv with 2 columns: track_id and popularity
csvcut -c "track_id","popularity" Spotify201809.csv > Spotify201809_subset.csv
# While stacking the 2 files, create a data source column
csvstack -g "Sep2018","Oct2018" Spotify201809_subset.csv Spotify201810_subset.csv > Spotify_all_rankings.csv
