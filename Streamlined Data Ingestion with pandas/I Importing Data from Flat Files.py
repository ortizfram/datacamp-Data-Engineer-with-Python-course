"""**************************************************************************************************
[] Flat files:
         - no format, 
         - separated by delimiter(,)
         - load them all >>>>>>>> read_csv()
Loading CSV : 
                  import pandas as pd

                  tax_data = read_csv("us_tax_data_2016.csv")
                  tax_data.head(4)
                  
Loading other file types:
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

#--- Get data from other flat files - \"t" - plot in bars

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

#--- 
