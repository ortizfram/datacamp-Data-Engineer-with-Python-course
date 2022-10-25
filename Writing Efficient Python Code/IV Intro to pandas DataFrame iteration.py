"""******************************************************************************************************************************************************
   Brief introduction on how to efficiently work with pandas DataFrames.
You'll learn the various options you have for iterating over a DataFrame. Then, you'll learn how to efficiently apply functions to data stored in a DataFrame.

$$$$ PANDAS: library used for data analysis $$$$ 
- DataFrame (tabular data structure)

-----Best practices for iterating over a DataFrame

  ++ Calculating Win percentage
   
      import numpy as np
      def calc_win_perc(wins, games_played):
          win_perc = wins / games_played
          return np.round(win_perc,2)
      win_perc = calc_win_perc(50, 100)
      print(win_perc)
      # 0.5
      
  iterating with .iterrows()  (Pandas)    +efficient
  ====================================
  
  >>>>>>>>> iterrrows() ==== returns index + each row as a tuple 
  $$$$ .iterrrows() takes half the time that takes iloc() $$$$
  
  ++
  
     win_perc_list = []
     
     for i,row in baseball_df.iterrows():
            wins = row['W']
            games_played = row['G']
            win_perc = calc_win_perc(wins,games_played)
            win_perc_list.append(win_perc)
     baseball_df['WP'] = win_perc_list
********************************************************************************************************************************************************"""
#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## Iterating with .iterrows() 1

# Iterate over pit_df and print each row
for i,row in pit_df.iterrows():
    print(row)
"""Team         PIT
League        NL
Year        2012
RS           651
RA           674
W             79
G            162
Playoffs       0
....prints same for other teams"""

## Iterating with .iterrows() 2
 
# Iterate over pit_df and print each index variable and then each row
for i,row in pit_df.iterrows():
    print(i)
    print(row)
    print(type(row))
"""0
Team         PIT
League        NL
Year        2012
RS           651
RA           674
W             79
G            162
Playoffs       0
Name: 0, dtype: object
<class 'pandas.core.series.Series'>
..... prints same for other teams"""

## Iterating with .iterrows() 3

# Use one variable instead of two to store the result of .iterrows()
for row_tuple in pit_df.iterrows():
    print(row_tuple)
      
## Iterating with .iterrows() 4
      
# Print the row and type of each row
for row_tuple in pit_df.iterrows():
    print(row_tuple)
    print(type(row_tuple)) 
"""(0, Team         PIT
League        NL
Year        2012
RS           651
RA           674
W             79
G            162
Playoffs       0
Name: 0, dtype: object)
<class 'tuple'>"""
"""!!!
If using i,row, you can access things from the row using square brackets (i.e., row['Team']). 
If using row_tuple, you would have to specify which element of the tuple you'd like to access before grabbing the team name (i.e., row_tuple[1]['Team'])."""
#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## Run differentials with .iterrows()

""" 'RS' means runs scored and 'RA' means runs allowed."""
# Create an empty list to store run differentials
run_diffs = []

# Write a for loop and **collect runs allowed and runs scored for each row
for i,row in giants_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']
    
    # Use the provided function to calculate run_diff for each row
   """def calc_run_diff(runs_scored, runs_allowed):
          run_diff = runs_scored - runs_allowed
          return run_diff"""
    run_diff = calc_run_diff(runs_scored, runs_allowed)
    
    # Append each run differential to the output list
    run_diffs.append(run_diff)

giants_df['RD'] = run_diffs
"""calculate a metric called the run differential for each season from the year 2008 to 2012."""
print(giants_df)

"""!!!
In fact, in both of these seasons (2010 and 2012), the San Francisco Giants not only made the playoffs but also won the World Series!"""

"""********************************************************************************************************************************************************
Another iterator method: .itertuples()
=======================================
$$$$ Remember, using .itertuples() is just like using .iterrows()
except it tends to be faster. You also have to use a dot reference when looking up attributes with .itertuples(). $$$$

>>>>>>>>> .itertuples() ====== returns each DataFrame row as a -----special data type called a namedtuple
<<>>>>>>> indexing syntax ===== uses points to select rows, unlike iterrows(), that uses [][]

A pandas DataFrame has been loaded into your session called rangers_df. This DataFrame contains the stats 
('Team', 'League', 'Year', 'RS', 'RA', 'W', 'G', and 'Playoffs')
for the Major League baseball team named the Texas Rangers (abbreviated as 'TEX').
********************************************************************************************************************************************************"""
## Iterating with .itertuples()

# Loop over the DataFrame and print each row
"""print each row"""
for row in rangers_df.itertuples():
  print(row)
"""Pandas(Index=0, Team='TEX', League='AL', Year=2012, RS=808, RA=707, W=93, G=162, Playoffs=1)
Pandas(Index=1, Team='TEX', League='AL', Year=2011, RS=855, RA=677, W=96, G=162, Playoffs=1)
Pandas(Index=2, Team='TEX', League='AL', Year=2010, RS=787, RA=687, W=90, G=162, Playoffs=1)
Pandas(Index=3, Team='TEX', League='AL', Year=2009, RS=784, RA=740, W=87, G=162, Playoffs=0)....."""

## Iterating with .itertuples() 2

# Loop over the DataFrame and print each row's Index, Year and Wins (W)
"""indexing some rows"""
for row in rangers_df.itertuples():
  i = row.Index
  year = row.Year
  wins = row.W
  print(i, year, wins)
"""0 2012 93
   1 2011 96
   2 2010 90
   3 2009 87
   4 2008 79
   5 2007 75
   6 2006 80
   7 2005 79
   8 2004 89
   9 2003 71
   10 2002 72"""

## Iterating with .itertuples() 3

# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
  i = row.Index
  year = row.Year
  wins = row.W
  
  # Check if rangers made Playoffs (1 means yes; 0 means no)
  """if Playoffs ==1 print values from for loop"""
  if row.Playoffs == 1:
    print(i, year, wins)
 """0 2012 93
   1 2011 96
   2 2010 90
   13 1999 95
   14 1998 88
   16 1996 90"""
"""!!!
.itertuples(). Remember, you need to use the dot syntax for referencing an attribute in a namedtuple."""
#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## Run differentials with .itertuples() 

run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
"""Collect row RS, RA from yankees_df"""
for row in yankees_df.itertuples():
    
    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = calc_run_diff(runs_scored, runs_allowed)
    
    run_diffs.append(run_diff)
   
# Append new column
yankees_df['RD'] = run_diffs
print(yankees_df)

"""----Question
In what year within your DataFrame did the New York Yankees have the highest run differential?"""

# In 1998 (with a Run Differential of 309)

"""********************************************************************************************************************************************************
pandas alternative to looping
================================
- .apply method allows you to apply a function to a DataFrame without the need to write a for loop.
- .apply method is much faster than using for loop

>>>>>>>>>>>> .apply() (pandas method) =====apply functions to all rows or columns of a DataFrame by specifying an axis.
      <<<<<<<<<< axis especifying ===== must specify axis to apply (0 columns; 1 for rows)
      <<<<<<<<< lambda funtions ==== can be used with anonymous lambda functions
      
  ++
      # Pandas For not use looping, adding RD column 
      run_diffs_apply = baseball_df.apply(
            lambda row: calc_run_diff(row['RS'],row['RA']),
            axis = 1)
      baseball_df['RD'] = run_diffs_apply
      print(baseball_df)
********************************************************************************************************************************************************"""
## Analyzing baseball stats with .apply()

# Gather sum of all columns
"""apply sum to all rays_df columns"""
stat_totals = rays_df.apply(sum, axis=0)
print(stat_totals)
""" RS          3783
    RA          3265
    W            458
    Playoffs       3
    dtype: int64"""

# Gather total runs scored in all games per year
total_runs_scored = rays_df[['RS', 'RA']].apply(sum, axis=1)
print(total_runs_scored)
"""2012    1274
2011    1321
2010    1451
2009    1557
2008    1445
dtype: int64"""

# Convert numeric playoffs to text by applying text_playoffs()
"""text_playoffs : if playoffs == 1 text = YES, else = no"""
textual_playoffs = rays_df.apply(lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)
"""2012     No
2011    Yes
2010    Yes
2009     No
2008    Yes"""
#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## Settle a debate with .apply()

# Display the first five rows of the DataFrame
"""return complete df"""
print(dbacks_df.head())

# Create a win percentage Series
"""apply this function to needed rows in the df"""
"""calc_win_perc : returns wins/games_played rounded with np"""
win_percs = dbacks_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

# Append a new column to dbacks_df
"""create new column called WP to store win_percs"""
dbacks_df['WP'] = win_percs
print(dbacks_df, '\n')

# Display dbacks_df where WP is greater than 0.50
"""return WP df greater/equal than 0.50"""
print(dbacks_df[dbacks_df['WP'] >= 0.50])

"""----Question
Which manager was correct in their claim?"""

# The manager who claimed the team has not made the playoffs every year they've had a win percentage of 0.50 or greater.
"""********************************************************************************************************************************************************
Optimal pandas iterating
========================
   ++
         # Get win values as np pandas
         wins_np = baseball_df['W'].values
         
power of Vectorizing (Broadcasting)
===================================
   ++
         # Calculations of all df values at once using broadcasting and adding new column to df
         run_diffs_np = baseball_df['RS'].values - baseball_df['RA'].values
         baseball_df['RD'] = run_diffs_np
         
********************************************************************************************************************************************************"""
