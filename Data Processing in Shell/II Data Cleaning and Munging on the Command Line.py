"""
 utilize the command line library csvkit to convert, preview, filter and manipulate files to prepare our data for further analyses.
"""

## THEO=======================
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
