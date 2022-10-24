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
