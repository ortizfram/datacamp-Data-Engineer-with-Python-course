#Dictionaries for data science
"""Create a zip object by calling zip() and passing to it feature_names and row_vals. Assign the result to zipped_lists.
Create a dictionary from the zipped_lists zip object by calling dict() with zipped_lists. Assign the resulting dictionary to rs_dict."""

# Zip lists: zipped_lists
zipped_lists = zip(feature_names, row_vals)

# Create a dictionary: rs_dict
rs_dict = dict(zipped_lists)

# Print the dictionary
print(rs_dict)
#-----------------------------------------------------------------------------------#
#Writing a function to help you
"""In this exercise, you will create a function to house the code you wrote earlier to make things easier and much more concise. Why? This way, you only need to call the function and supply the appropriate lists to create your dictionaries! Again, the lists feature_names and row_vals are preloaded and these contain the header names of the dataset and actual values of a row from the dataset, respectively.

--Instructions
100 XP
Define the function lists2dict() with two parameters: first is list1 and second is list2.
Return the resulting dictionary rs_dict in lists2dict().
Call the lists2dict() function with the arguments feature_names and row_vals. Assign the result of the function call to rs_fxn."""

# Define lists2dict()
def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""

    # Zip lists: zipped_lists
    zipped_lists = zip(list1, list2)

    # Create a dictionary: rs_dict
    rs_dict = dict(zipped_lists)

    # Return the dictionary
    return rs_dict

# Call lists2dict: rs_fxn
rs_fxn = lists2dict(feature_names, row_vals)

# Print rs_fxn
print(rs_fxn)

""" output
{'CountryName': 'Arab World', 'CountryCode': 'ARB', 'IndicatorName': 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'IndicatorCode': 'SP.ADO.TFRT', 'Year': '1960', 'Value': '133.56090740552298'}
"""
#-----------------------------------------------------------------------------------#
#Using a list comprehension
"""
This time, you're going to use the lists2dict() function you defined in the last exercise to turn a bunch of lists into a list of dictionaries with the help of a list comprehension.

The lists2dict() function has already been preloaded, together with a couple of lists, feature_names and row_lists. feature_names contains the header names of the World Bank dataset and row_lists is a list of lists, where each sublist is a list of actual values of a row from the dataset.

Your goal is to use a list comprehension to generate a list of dicts, where the keys are the header names and the values are the row entries.

--Instructions
100 XP
Inspect the contents of row_lists by printing the first two lists in row_lists.
Create a list comprehension that generates a dictionary using lists2dict() for each sublist in row_lists. The keys are from the feature_names list and the values are the row entries in row_lists. Use sublist as your iterator variable and assign the resulting list of dictionaries to list_of_dicts.
Look at the first two dictionaries in list_of_dicts by printing them out."""

# Print the first two lists in row_lists
print(row_lists[0])
print(row_lists[1])

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Print the first two dictionaries in list_of_dicts
print(list_of_dicts[0])
print(list_of_dicts[1])
#-----------------------------------------------------------------------------------#
#Turning this all into a DataFrame
"""You've zipped lists together, created a function to house your code, and even used the function in a list comprehension to generate a list of dictionaries. That was a lot of work and you did a great job!

You will now use all of these to convert the list of dictionaries into a pandas DataFrame. You will see how convenient it is to generate a DataFrame from dictionaries with the DataFrame() function from the pandas package.

The lists2dict() function, feature_names list, and row_lists list have been preloaded for this exercise.

Go for it!

--Instructions
100 XP
To use the DataFrame() function you need, first import the pandas package with the alias pd.
Create a DataFrame from the list of dictionaries in list_of_dicts by calling pd.DataFrame(). Assign the resulting DataFrame to df.
Inspect the contents of df printing the head of the DataFrame. Head of the DataFrame df can be accessed by calling df.head()."""
# Import the pandas package
import pandas as pd

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Turn list of dicts into a DataFrame: df
df = pd.DataFrame(list_of_dicts)

# Print the head of the DataFrame
print(df.head())
"""output
CountryName CountryCode                                      IndicatorName   IndicatorCode  Year               Value
0  Arab World         ARB  Adolescent fertility rate (births per 1,000 wo...     SP.ADO.TFRT  1960  133.56090740552298
1  Arab World         ARB  Age dependency ratio (% of working-age populat...     SP.POP.DPND  1960    87.7976011532547
2  Arab World         ARB  Age dependency ratio, old (% of working-age po...  SP.POP.DPND.OL  1960   6.634579191565161
3  Arab World         ARB  Age dependency ratio, young (% of working-age ...  SP.POP.DPND.YG  1960   81.02332950839141
4  Arab World         ARB        Arms exports (SIPRI trend indicator values)  MS.MIL.XPRT.KD  1960           3000000.0"""
#------------------------------------------------------------------------------------------------------------------------#
#Processing data in chunks (1)
"""Sometimes, data sources can be so large in size that storing the entire dataset in memory becomes too resource-intensive. In this exercise, you will process the first 1000 rows of a file line by line, to create a dictionary of the counts of how many times each country appears in a column in the dataset.

The csv file 'world_dev_ind.csv' is in your current directory for your use. To begin, you need to open a connection to this file using what is known as a context manager. For example, the command with open('datacamp.csv') as datacamp binds the csv file 'datacamp.csv' as datacamp in the context manager. Here, the with statement is the context manager, and its purpose is to ensure that resources are efficiently allocated when opening a connection to a file.

If you'd like to learn more about context managers, refer to the DataCamp course on Importing Data in Python.

--Instructions
100 XP
Use open() to bind the csv file 'world_dev_ind.csv' as file in the context manager.
Complete the for loop so that it iterates 1000 times to perform the loop body and process only the first 1000 rows of data of the file."""
# Open a connection to the file
with open("world_dev_ind.csv") as file:

    # Skip the column names
    file.readline()

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Process only the first 1000 rows
    for j in range(1000):

        # Split the current line into a list: line
        line = file.readline().split(',')

        # Get the value for the first column: first_col
        first_col = line[0]

        # If the column value is in the dict, increment its value
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1

        # Else, add to the dict and set value to 1
        else:
            counts_dict[first_col] = 1

# Print the resulting dictionary
print(counts_dict)
"""output:
{'Arab World': 80, 'Caribbean small states': 77, 'Central Europe and the Baltics': 71, 
'East Asia & Pacific (all income levels)': 122, 'East Asia & Pacific (developing only)': 123, 'Euro area': 119, 
'Europe & Central Asia (all income levels)': 109, 'Europe & Central Asia (developing only)': 89, 'European Union': 116,
'Fragile and conflict affected situations': 76, 'Heavily indebted poor countries (HIPC)': 18}"""
#------------------------------------------------------------------------------------------------------#
#Writing a generator to load data in chunks (2)
"""In the previous exercise, you processed a file line by line for a given number of lines. What if, however, you want to do this for the entire file?

In this case, it would be useful to use generators. Generators allow users to lazily evaluate data. This concept of lazy evaluation is useful when you have to deal with very large datasets because it lets you generate values in an efficient manner by yielding only chunks of data at a time instead of the whole thing at once.

In this exercise, you will define a generator function read_large_file() that produces a generator object which yields a single line from a file each time next() is called on it. The csv file 'world_dev_ind.csv' is in your current directory for your use.

Note that when you open a connection to a file, the resulting file object is already a generator! So out in the wild, you won't have to explicitly create generator objects in cases such as this. However, for pedagogical reasons, we are having you practice how to do this here with the read_large_file() function. Go for it!

Instructions
100 XP
In the function read_large_file(), read a line from file_object by using the method readline(). Assign the result to data.
In the function read_large_file(), yield the line read from the file data.
In the context manager, create a generator object gen_file by calling your generator function read_large_file() and passing file to it.
Print the first three lines produced by the generator object gen_file using next()."""
# Define read_large_file()
def read_large_file(file_object):
    """A generator function to read a large file lazily."""

    # Loop indefinitely until the end of the file
    while True:

        # Read a line from the file: data
        data = file_object.readline()

        # Break if this is the end of the file
        if not data:
            break

        # Yield the line of data
        yield data
        
# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Create a generator object for the file: gen_file
    gen_file = read_large_file(file)

    # Print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))
    """output:
    CountryName,CountryCode,IndicatorName,IndicatorCode,Year,Value
    
    Arab World,ARB,"Adolescent fertility rate (births per 1,000 women ages 15-19)",SP.ADO.TFRT,1960,133.56090740552298
    
    Arab World,ARB,Age dependency ratio (% of working-age population),SP.POP.DPND,1960,87.7976011532"""
#-------------------------------------------------------------------------------------------------------#
#Writing a generator to load data in chunks (3)
"""Great! You've just created a generator function that you can use to help you process large files.

Now let's use your generator function to process the World Bank dataset like you did previously. You will process the file line by line, 
to create a dictionary of the counts of how many times each country appears in a column in the dataset. For this exercise, 
however, you won't process just 1000 rows of data, you'll process the entire dataset!

The generator function read_large_file() and the csv file 'world_dev_ind.csv' are preloaded and ready for your use. Go for it!

--Instructions
100 XP
Bind the file 'world_dev_ind.csv' to file in the context manager with open().
Complete the for loop so that it iterates over the generator from the call to read_large_file() to process all the rows of the file."""
# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Open a connection to the file
with open("world_dev_ind.csv") as file:

    # Iterate over the generator from read_large_file()
    for line in read_large_file(file):

        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

# Print            
print(counts_dict)
#-------------------------------------------------------------------------------#
#Writing an iterator to load data in chunks (1) pandas
"""Another way to read data too large to store in memory in chunks is to read the file in as DataFrames of a certain length, say, 100. For example, with the pandas package (imported as pd), you can do pd.read_csv(filename, chunksize=100). This creates an iterable reader object, which means that you can use next() on it.

In this exercise, you will read a file in small DataFrame chunks with read_csv(). You're going to use the World Bank Indicators data 'ind_pop.csv', available in your current directory, to look at the urban population indicator for numerous countries and years.

--Instructions
100 XP
Use pd.read_csv() to read in 'ind_pop.csv' in chunks of size 10. Assign the result to df_reader.
Print the first two chunks from df_reader."""
# Import the pandas package
import pandas as pd

# Initialize reader object: df_reader
df_reader = pd.read_csv("ind_pop.csv", chunksize= 10)

# Print two chunks
print(next(df_reader))
print(next(df_reader))
"""output:
                                 CountryName CountryCode                  IndicatorName      IndicatorCode  Year   Value
0                                 Arab World         ARB  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  31.285
1                     Caribbean small states         CSS  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  31.597
2             Central Europe and the Baltics         CEB  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  44.508
3    East Asia & Pacific (all income levels)         EAS  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  22.471
4      East Asia & Pacific (developing only)         EAP  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  16.918
5                                  Euro area         EMU  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  62.097
6  Europe & Central Asia (all income levels)         ECS  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  55.379
7    Europe & Central Asia (developing only)         ECA  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  38.066
8                             European Union         EUU  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  61.213
9   Fragile and conflict affected situations         FCS  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  17.892
                                      CountryName CountryCode                  IndicatorName      IndicatorCode  Year   Value
10         Heavily indebted poor countries (HIPC)         HPC  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  12.236
11                                    High income         HIC  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  62.680
12                           High income: nonOECD         NOC  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  56.108
13                              High income: OECD         OEC  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  64.285
14  Latin America & Caribbean (all income levels)         LCN  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  49.285
15    Latin America & Caribbean (developing only)         LAC  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  44.863
16   Least developed countries: UN classification         LDC  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960   9.616
17                            Low & middle income         LMY  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  21.273
18                                     Low income         LIC  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  11.498
19                            Lower middle income         LMC  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  19.811"""
#---------------------------------------------------------------------------------------------------------------------------#
#Writing an iterator to load data in chunks (2)
"""
In the previous exercise, you used read_csv() to read in DataFrame chunks from a large dataset. In this exercise, you will read in a file using a bigger DataFrame chunk size and then process the data from the first chunk.

To process the data, you will create another DataFrame composed of only the rows from a specific country. You will then zip together two of the columns from the new DataFrame, 'Total Population' and 'Urban population (% of total)'. Finally, you will create a list of tuples from the zip object, where each tuple is composed of a value from each of the two columns mentioned.

You're going to use the data from 'ind_pop_data.csv', available in your current directory. pandas has been imported as pd.

Instructions
100 XP
Use pd.read_csv() to read in the file in 'ind_pop_data.csv' in chunks of size 1000. Assign the result to urb_pop_reader.
Get the first DataFrame chunk from the iterable urb_pop_reader and assign this to df_urb_pop.
Select only the rows of df_urb_pop that have a 'CountryCode' of 'CEB'. To do this, compare whether df_urb_pop['CountryCode'] is equal to 'CEB' within the square brackets in df_urb_pop[____].
Using zip(), zip together the 'Total Population' and 'Urban population (% of total)' columns of df_pop_ceb. Assign the resulting zip object to pops."""
# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv("ind_pop_data.csv", chunksize= 1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out the head of the DataFrame
print(df_urb_pop.head())

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

# Zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Total Population'], 
            df_pop_ceb['Urban population (% of total)'])
            
# Turn zip object into list: pops_list
pops_list = list(pops)

# Print pops_list
print(pops_list)
#----------------------------------------------------------------------------------------------------#
#Writing an iterator to load data in chunks (3)
"""
adding a column to a DataFrame.

Starting from the code of the previous exercise, you will be using a list comprehension to create the values for a new column 'Total Urban Population'
from the list of tuples that you generated earlier. Recall from the previous exercise that the first and second elements of each tuple consist of,
respectively, values from the columns 'Total Population' and 'Urban population (% of total)'. The values in this new column 'Total Urban Population', 
therefore, are the product of the first and second element in each tuple. Furthermore, because the 2nd element is a percentage, you need to divide the 
entire result by 100, or alternatively, multiply it by 0.01.

You will also plot the data from this new column to create a visualization of the urban population data.

The packages pandas and matplotlib.pyplot have been imported as pd and plt respectively for your use.

Instructions
100 XP
Write a list comprehension to generate a list of values from pops_list for the new column 'Total Urban Population'. The output expression should be the product of the first and second element in each tuple in pops_list. Because the 2nd element is a percentage, you also need to either multiply the result by 0.01 or divide it by 100. In addition, note that the column 'Total Urban Population' should only be able to take on integer values. To ensure this, make sure you cast the output expression to an integer with int().
Create a scatter plot where the x-axis are values from the 'Year' column and the y-axis are values from the 'Total Urban Population' column."""
# Code from previous exercise
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)
df_urb_pop = next(urb_pop_reader)
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
pops = zip(df_pop_ceb['Total Population'], 
           df_pop_ceb['Urban population (% of total)'])
pops_list = list(pops)

# Use list comprehension to create new DataFrame column 'Total Urban Population'
df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]

# Plot urban population data
df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()
#----------------------------------------------------------------------------------------#
## Writing an iterator to load data in chunks (5)

# Define plot_pop()
def plot_pop(filename, country_code):

    # Initialize reader object: urb_pop_reader
    urb_pop_reader = pd.read_csv(filename, chunksize=1000)

    # Initialize empty DataFrame: data
    data = pd.DataFrame()
    
    # Iterate over each DataFrame chunk
    for df_urb_pop in urb_pop_reader:
        # Check out specific country: df_pop_ceb
        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]

        # Zip DataFrame columns of interest: pops
        pops = zip(df_pop_ceb['Total Population'],
                    df_pop_ceb['Urban population (% of total)'])

        # Turn zip object into list: pops_list
        pops_list = list(pops)

        # Use list comprehension to create new DataFrame column 'Total Urban Population'
        df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
    
        # Append DataFrame chunk to data: data
        data = data.append(df_pop_ceb)

    # Plot urban population data
    data.plot(kind='scatter', x='Year', y='Total Urban Population')
    plt.show()

# Set the filename: fn
fn = 'ind_pop_data.csv'

# Call plot_pop for country code 'CEB'
plot_pop("ind_pop_data.csv", 'CEB')

# Call plot_pop for country code 'ARB'
plot_pop("ind_pop_data.csv", 'ARB')

