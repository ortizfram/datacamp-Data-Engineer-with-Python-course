"""*******************************************************************************************************************************
  You will learn how to gather and compare runtimes between different coding approaches. You'll practice using the line_profiler 
and memory_profiler packages to profile your code base and spot bottlenecks. Then, you'll put your learnings to practice by replacing
these bottlenecks with efficient Python code.

--------------------------
ns	nanosecond	
µs (us)	microsecond	
ms	millisecond	
s	second	
--------------------------

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
## Using %timeit: your turn!

# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(0,51)]
print(nums_list_comp)

## your turn! 2 -----

# Create a list of integers (0-50) by unpacking range
nums_unpack = [*range(0,51)]
print(nums_unpack)

## your turn! 3 -----
"""Use %timeit within your IPython console (i.e. not within the script.py window) to compare the runtimes for creating 
a list of integers from 0 to 50 using list comprehension vs. unpacking the range object. Don't include the print() statements when timing.
      
      In [1]: %timeit [num for num in range(0,51)]
      In [2]: %timeit [*range(0,51)]
      
      out 1: 4.28 us +- 785 ns per loop 
      out 2: 678 ns +- 105 ns per loop 
      # Unpacking the range object was faster than list comprehension."""
