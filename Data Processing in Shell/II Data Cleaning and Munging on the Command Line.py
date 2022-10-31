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
 """  filter data using [column name/position] :  >>>>>> csvcut
                                                  -n :  return all names
                                                  -c :  filter by position:  [-c 2,3] or [-c "column_name"]
                                                  
      filter data using by row value  :  >>>>>> csvgrep
      return names of all columns  :  >>>>>> --names or -n

      eg  :  # Return all names of file :
             csvcut -n Spotify_MusicAttributes.csv
      
