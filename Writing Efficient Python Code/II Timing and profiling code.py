"""*******************************************************************************************************************************
  You will learn how to gather and compare runtimes between different coding approaches. You'll practice using the line_profiler 
and memory_profiler packages to profile your code base and spot bottlenecks. Then, you'll put your learnings to practice by replacing
these bottlenecks with efficient Python code.

    @ Why timing code?
    
      # Allows to pick 'optimal' code approach
      # Faster == more 'efficient'
      
     How to time code?
     =================
    
      >>>>>>> %timeit ====calculate runtime with IPython 'magic command'
      >>>>>>> 'magic command' ===goes on 'top' of normal python syntax, prefixed by " % "
      >>>>>>> %lsmagic ===== see all magic commands
      
          import numpy as np 
          %timeit rand_nums = np.random.rand(1000)
          # provides AVG of timing statistics
          
     Specify number of runs and loops
     =================================
      >>>>>>> -r ===set number of runs
      >>>>>>> -n ===set number of loops
      # loop : how many times to execute per run 
      # run: how many runs 
      
          import numpy as np 
          %timeit -r2 -n10 rand_nums = np.random.rand(1000)
          
     Timing lines, Timing Blocks
     ===========================
     >>>>>>> %timeit === time Line
     >>>>>>> %%timeit === time Block
     
     Save Output into Variable (-o)
     ===========================
     times = %timeit -o rand_nums = np.random.rand(1000)
     
     ## to see ----- 'time for each run' 
     times.timing
     
     ## to see ----- 'best time for all runs'
     times.best
     
     ## to see ----- 'worst time for all runs'
     times.worst
     
     Comparing times
     ================
     f_time = %timeit -o formal_dict = dict()
     l_time = %timeit -o literal_dict = {}
     
     diff = (f_time.average - l_time.average) * (10**9)
     print('l_time better than f_time by {} ns'.format(diff))
     
     # l_time better than f_time by 51.9 ns
*******************************************************************************************************************************"""
