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
#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## Using %timeit: specifying number of runs and loops

"""analyze the runtime for converting this heroes list into a set. Instead of relying on the default settings for %timeit,
you'd like to only use 5 runs and 25 loops per each run.

--What is the correct syntax when using %timeit and only using 5 runs with 25 loops per each run?
    
    # %timeit -r5 -n25 set(heroes)"""
#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## Using %timeit: formal name or literal syntax

# Create a list using the formal name
formal_list = list()
print(formal_list)

# Create a list using the literal syntax
literal_list = []
print(literal_list)

## formal name or literal syntax 2

# Create a list using the formal name
formal_list = list()
print(formal_list)

# Create a list using the literal syntax
literal_list = []
print(literal_list)

# Print out the type of formal_list
print(type(formal_list))

# Print out the type of literal_list
print(type(literal_list))

## formal name or literal syntax 3

"""Question
Use %timeit in your IPython console to compare runtimes between creating a list using the formal name (list()) and the literal syntax ([]).
Don't include the print() statements when timing.

      # Using the literal syntax ([]) to create a list is faster."""
#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## Using cell magic mode (%%timeit)

%%timeit
wts_np = np.array(wts)
hero_wts_lbs_np = wts_np * 2.20462
#33.7 us +- 3.68 us per loop

%%timeit
hero_wts_lbs = []
for wt in wts:
    hero_wts_lbs.append(wt * 2.20462)
#1.59 ms +- 125 us per loop

    # The numpy technique was faster.
"""*******************************************************************************************************************************
Code profiling .calculate runtime for big pieces of code
===============
    - Detailed stats on freq. and duration of function calls
    - Line-by-line analyses
    $~ line_profiler ---- (package not standard library) 
    
      >>>>>>> pip install line_profiler
      >>>>>>> %load_ext line_profiler =====load package
      >>>>>>> %lprun -f function_name function_name(include_args)======== line by line times----provides a table of stats
                                                             # hits= ntimes executed, % = time function takes, line_content 
              
    
    
    

*******************************************************************************************************************************"""
## Pop quiz: steps for using %lprun


"""What are the necessary steps you need to take in order to profile the convert_units() function acting on your superheroes data 
if you'd like to see line-by-line runtimes?

Use %load_ext line_profiler to load the line_profiler within your IPython session
Use %lprun -f convert_units convert_units(heroes, hts, wts) to get line-by-line runtimes.

     # The first and second options from above are necessary."""
#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````     
## Using %lprun: spot bottlenecks

def convert_units(heroes, heights, weights):

    new_hts = [ht * 0.39370  for ht in heights]
    new_wts = [wt * 2.20462  for wt in weights]

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data
 """Load the line_profiler package into your IPython session. Then, use %lprun to profile the convert_units()
 function acting on your superheroes data. Remember to use the special syntax for working with %lprun (you'll have to provide a 
 -f flag specifying the function you'd like to profile)."""
          
          pip install line_profiler
          %load_ext line_profiler
          %lprun -f convert_units convert_units(heroes,hts,wts)
"""output:
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def convert_units(heroes, heights, weights):
     2                                           
     3         1        171.0    171.0     16.3      new_hts = [ht * 0.39370  for ht in heights]
     4         1        151.0    151.0     14.4      new_wts = [wt * 2.20462  for wt in weights]
     5                                           
     6         1          1.0      1.0      0.1      hero_data = {}
     7                                           
     8       481        375.0      0.8     35.8      for i,hero in enumerate(heroes):
     9       480        349.0      0.7     33.3          hero_data[hero] = (new_hts[i], new_wts[i])
    10                                                   
    11         1          1.0      1.0      0.1      return hero_data"""

# 11% - 20%
#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## Using %lprun: fix the bottleneck 2
"""What percentage of time is spent on the new_hts array broadcasting line of code relative to the total amount 
of time spent in the convert_units_broadcast() function?"""

      %load_ext line_profiler
      %lprun -f convert_units_broadcast convert_units_broadcast(heroes,hts,wts)
"""Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def convert_units_broadcast(heroes, heights, weights):
     2                                           
     3                                               # Array broadcasting instead of list comprehension
     4         1         31.0     31.0      4.0      new_hts = heights * 0.39370
     5         1          4.0      4.0      0.5      new_wts = weights * 2.20462
     6                                           
     7         1          1.0      1.0      0.1      hero_data = {}
     8                                           
     9       481        333.0      0.7     43.4      for i,hero in enumerate(heroes):
    10       480        397.0      0.8     51.8          hero_data[hero] = (new_hts[i], new_wts[i])
    11                                                   
    12         1          1.0      1.0      0.1      return hero_data"""
    
    #0% - 10%
"""*******************************************************************************************************************************
Code profiling : memory
========================
  
    $$$$ CAN'T BE USED IN IPYTHON session, just in PHYSICAL FILES
    
# individual object
        >>>>>>>>> import sys ----(built-in)====== Inspect memory conpsumption
        >>>>>>>>> sys.getsizeof() ===== returns Individual object size in bytes
# line-by-line (%mprun)
        >>>>>>>>> pip install memory_profiler
        >>>>>>>>> load_ext memory_profiler
        >>>>>>>>> %mprun -f convert_units_broadcast convert_units_broadcast(heroes,hts,wts)
*******************************************************************************************************************************"""
