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
             - Limit rows >>>>>>>>> nrows
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
