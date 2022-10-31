""" 
how to download data files from web servers via the command line. In the process, we also learn about documentation manuals, option flags, and multi-file processing
"""
#====================================================
#           THEORY & EXAMPLES
#===================================================
## Downloading data using curl : 
""" ** CURL : short Client for URLs, 
              Unix CommandLine Tool 
              Tranfers Data To and From Servers
              Used to download data from HTTPs sites and FTP Servers"""             
## Checking CURL Installation :
    # >>>>>> man curl
""" if not installed follow link steps:  https://curl.se/download.html"""



## Curl Syntax : 
    # curl [option flags] [URL]
## Curl Supports : 
    # HTTP, HTTPS, FTP, SFTP

  
  
## Downloading single file  :
  """ # Download with same name : >>>>>> curl -0
      # eg : curl -0 https://websitename/datafilename.txt
      # Rename file : >>>>>> curl -0 renamedfile https://websitename/datafilename.txt     """
## Downloading multiple files w/ WILDCARDS :
  """ # Globing Parser :  >>>>>> curl -0  https://websitename/datafilename*.txt
      # indexing       : >>>>>> curl -0 https://websitename/datafilename[001-100:10].txt    """

  
  
  
## Flags in case of timeouts : 
  """ # Redirect HTTP URL if 300 error occurs   : >>>>>> -L
      # Resumes previous file transfer if timeout before completition   : >>>>>> -C   """
#---------------
## Using curl documentation
"""--- Based on the information in the curl manual, which of the following is NOT a supported file protocol ?  :"""
# OFTP



## Downloading single file using curl
# Use curl to download the file from the redirected URL
  # curl -L https://assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip
# # Download and rename the file in the same step
  # curl -o Spotify201812.zip -L https://assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip

## Downloading multiple files using curl
# Download all 100 data files
  # curl -L https://s3.amazonaws.com/assets.datacamp.com/production/repositories/4180/datasets/files/datafile[001-100].txt
# Print all downloaded files to directory
  # ls datafile*.txt

  
  
## Downloading data using Wget  :
  """ ** Wget : Derives from World Wide Web and Get
                compatible w/ all OS
                Used to download data from HTTPS and FTP
            $$$ BETER THAN USING CURL TO DOWNLOAD MULTIPLE FILES $$$      """
## Check Installation   : 
  # throws Wget location   : >>>>>> which wget 
  """ if not installed follow link steps :  https://www.gnu.org/software/wget/    """
  # check manual when installed :  >>>>>> man Wget
  
  
## Basic Syntax Wget :  >>>>>> wget [option flags] [URL]


""" ** Option Flags unique to wget :
        -b : go background after startup
        -q : turn off wget output
        -c : resume broken download     
       -------- 
            eg. :  wget -bqc [URL]
       ------
    ** PID : unique ID for data download process in case of cancellation    """
#====================================================
#           EXERCICES
#===================================================
