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
