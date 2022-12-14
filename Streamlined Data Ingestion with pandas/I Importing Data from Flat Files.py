"""**************************************************************************************************
[] Flat files:
         - no format, 
         - separated by delimiter(,)
         - load them all >>>>>>>> read_csv()
Loading CSV :
===========
                  import pandas as pd

                  tax_data = read_csv("us_tax_data_2016.csv")
                  tax_data.head(4)
                  
Loading other file types:
=========================
          - specify a delmiter >>>>>> sep = ""
****************************************************************************************************"""

#--- Get data from CSVs

# Import pandas as pd
import pandas as pd

# Read the CSV and assign it to the variable data
data = pd.read_csv("vt_tax_data_2016.csv")

# View the first few lines of data
print(data.head())
#```````````````````````````````````````````````````````````````````````````````````````````````

#--- Get data from other flat files - sep=\"t" - plot in bars

# Import pandas with the alias pd
import pandas as pd

# Load TSV using the sep keyword argument to set delimiter
"""default separator is comma"""
data = pd.read_csv("vt_tax_data_2016.tsv", sep="\t") #tab separated values

# Plot the total number of tax returns by income group. Plot in bars
counts = data.groupby("agi_stub").N1.sum() # N1 contains income range categories
counts.plot.bar()
plt.show()
#```````````````````````````````````````````````````````````````````````````````````````````````
"""****************************************************************************************************
Modifying flat file imports:
===========================
             - Limit columns >>>>>>>>> usecols
                           col_names = ['STATEFIPS', 'STATE', 'zipcode', 'agi_stub', 'N1']
                           col_nums = [0, 1, 2, 3, 4]
                           
                           # choose columns to load by name:
                           tax_data_v1 = pd.read_csv("us_tax_data_2016.csv", usecols=col_names)
             - Limit rows import IN CHUNKS 
                           >>>>>>>>> nrows -------- select how many rows
                           tax_data_first100 = pd.read_csv("us_tax_data_2016.csv", nrows=100)
                           >>>>>>>>> skiprows -----accepts a list of row n, funtion to filter rows 
                           >>>>>>>>> header=None ----------pandas knows there are no column names
                           tax_data_next500 = pd.read_csv("us_tax_data_2016.csv",
                                                            nrows=500,
                                                            skiprows=1000,
                                                            header= None)
            - Asigning column Names >>>>>>>>>>> names
                 $$$ do it after the import
                           col_names = list(taxt_data_first1000)
                           tax_data_next500 = pd.read_csv("us_tax_data_2016.csv",
                                                            nrows=500,
                                                            skiprows=1000,
                                                            header= None,
                                                            names= col_names)                                
****************************************************************************************************"""

#--- Import a subset of columns
"""columns to use: zipcode, agi_stub (income group), mars1 (number of single households),
MARS2 (number of households filing as married), and NUMDEP (number of dependents)."""

# Create list of columns to use
cols = ["zipcode","agi_stub","mars1","MARS2","NUMDEP"]

# Create dataframe from csv using only selected columns
data = pd.read_csv("vt_tax_data_2016.csv", usecols=cols)

# View counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())
#```````````````````````````````````````````````````````````````````````````````````````````````

#--- Import a file in chunks
# make a list of first 500 to get those column names
col_names = list(vt_data_first500)
# Create dataframe of next 500 rows with labeled columns
vt_data_next500 = pd.read_csv("vt_tax_data_2016.csv", 
                       		  nrows=500,
                       		  skiprows=500,
                       		  header=None,
                       		  names=col_names)

# View the Vermont dataframes to confirm they're different
print(vt_data_first500.head())
print(vt_data_next500.head())
"""****************************************************************************************************
Handling errors and missing data: 
================================
// Wrong Types, Missing Values, records Can't be Read by Pandas
              - Specify column DataTypes 
                           >>>>>>>>> dtype------ takes dictionary of columns names and data types
                           tax_data_first100 = pd.read_csv("us_tax_data_2016.csv", dtype={"zipcode": str})
                           # obj type is a Pandas str
              - See column Type
                           >>>>>>>>> dtypes--------- in print option, takes table name.dtypes
              - Customizing Miissing Data
                           # 0 in zipcode is invalid and missing
                           >>>>>>>>> na_values------- pass single value, list, dict of column and values 
                           tax_data_first100 = pd.read_csv("us_tax_data_2016.csv", na_values={"zipcode":0})
                           print(tax_data[tax_data.zipcode.isna()])
              - See Null values
                           >>>>>>>> isna()
              - Lines with Errors
                           >>>>>>>> error_bad_lines= False------ to skip unparseable records intead of error
                           >>>>>>>> warn_bad_lines= True------ see messages when records are skipped & why
                           tax_data_first100 = pd.read_csv("us_tax_data_2016.csv", error_bad_lines= False, warn_bad_lines= True)
****************************************************************************************************"""

#--- Specify data types - see all data types
# Load csv with no additional arguments
data = pd.read_csv("vt_tax_data_2016.csv")

# Print the data types
print(data.dtypes)
#```````````````````````````````````````````````````````````````````````````````````````````````

#--- Specify data types 2
# Create dict specifying data types for agi_stub and zipcode
data_types = {"zipcode":str,
	     "agi_stub":"category"}

# Load csv using dtype to set correct data types
data = pd.read_csv("vt_tax_data_2016.csv", dtype= data_types)

# Print data types of resulting frame
print(data.dtypes.head())
#```````````````````````````````````````````````````````````````````````````````````````````````
                  
#--- Set custom NA values
# Create dict specifying that 0s in zipcode are NA values
null_values = {"zipcode":0}

# Load csv using na_values keyword argument
data = pd.read_csv("vt_tax_data_2016.csv", 
                   na_values= null_values)

# View rows with NA ZIP codes
print(data[data.zipcode.isna()])
#```````````````````````````````````````````````````````````````````````````````````````````````

#--- Skip bad data 1
try:
  # Import the CSV without any keyword arguments
  data = pd.read_csv("vt_tax_data_2016_corrupt.csv")
  
  # View first 5 records
  print(data.head(5))
  # if corrupted print message
except pd.errors.ParserError:
    print("Your data contained rows that could not be parsed.")
    print("Your data contained rows that could not be parsed.")
#```````````````````````````````````````````````````````````````````````````````````````````````

#--- Skip bad data 2
try:
  # Import CSV with error_bad_lines set to skip bad records
  data = pd.read_csv("vt_tax_data_2016_corrupt.csv", 
                     error_bad_lines=False)
  
  # View first 5 records
  print(data.head())
  
except pd.errors.ParserError:
    print("Your data contained rows that could not be parsed.")
#```````````````````````````````````````````````````````````````````````````````````````````````

#--- Skip bad data 3
try:
  # Set warn_bad_lines to issue warnings about bad records
  data = pd.read_csv("vt_tax_data_2016_corrupt.csv", 
                     error_bad_lines=False, 
                     warn_bad_lines=True)
  
  # View first 5 records
  print(data.head())
  
except pd.errors.ParserError:
    print("Your data contained rows that could not be parsed.")
