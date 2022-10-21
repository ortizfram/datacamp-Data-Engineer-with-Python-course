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
      ------------------------------------------------------------------------------------------------------------------------------------...
    $$$$---CAN'T BE USED IN IPYTHON session, just in PHYSICAL FILES. So create another py file with the code you want to test memory of----$$$$
     $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    
# individual object
        >>>>>>>>> import sys ----(built-in)====== Inspect memory conpsumption
        >>>>>>>>> sys.getsizeof() ===== returns Individual object size in bytes
# line-by-line (%mprun)
..      ....... from hero_funcs import convert_units
        >>>>>>>>> pip install memory_profiler
        >>>>>>>>> load_ext memory_profiler
        >>>>>>>>> %mprun -f convert_units_broadcast convert_units_broadcast(heroes,hts,wts)
*******************************************************************************************************************************"""

## Pop quiz: steps for using %mprun
"""What are the necessary steps you need to take in order to profile the convert_units() function acting on your superheroes data if you'd like 
to see the line-by-line memory consumption of convert_units()?

   1   Use the command 'from hero_funcs import convert_units' to load the function you'd like to profile.
   2   Use '%load_ext memory_profiler' to load the memory_profiler within your IPython session.
   3   Use '%mprun -f convert_units convert_units(heroes, hts, wts)' to get line-by-line memory allocations.
   
   # all above
   
   $$$$$ %mprun requires one additional step compared to using %lprun (i.e., you need to import the function in order to use %mprun on it). $$$$$"""
#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## Using %mprun: Hero BMI

%load_ext memory_profiler
from bmi_lists import calc_bmi_lists
%mprun -f calc_bmi_lists calc_bmi_lists(sample_indices,hts,wts)
"""Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     1    110.6 MiB    110.6 MiB           1   def calc_bmi_lists(sample_indices, hts, wts):
     2                                         
     3                                             # Gather sample heights and weights as lists
     4    110.6 MiB      0.0 MiB       25003       s_hts = [hts[i] for i in sample_indices]
     5    110.6 MiB      0.0 MiB       25003       s_wts = [wts[i] for i in sample_indices]
     6                                         
     7                                             # Convert heights from cm to m and square with list comprehension
     8    110.6 MiB      0.0 MiB       25003       s_hts_m_sqr = [(ht / 100) ** 2 for ht in s_hts]
     9                                         
    10                                             # Calculate BMIs as a list with list comprehension
    11    110.6 MiB      0.0 MiB       25003       bmis = [s_wts[i] / s_hts_m_sqr[i] for i in range(len(sample_indices))]
    12                                         
    13    110.6 MiB      0.0 MiB           1       return bmis"""

"""------  answer the following question:
How much memory do the list comprehension lines of code consume in the calc_bmi_lists() function? 
(i.e., what is the total sum of the Increment column for these four lines of code?)"""
        
      # answer = 0.1 MiB - 2.0 MiB---------------> cause 110.6 MiB / 0.6
      # Correct! Using a list comprehension approach allocates anywhere from 0.1 MiB to 2 MiB of memory to calculate your BMIs.
#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## Using %mprun: Hero BMI 2.0

"""Each hero's height and weight is stored in a numpy array. That means you can use NumPy's handy array indexing capabilities and broadcasting to perform your
calculations.A function named calc_bmi_arrays has been created and saved to a file titled bmi_arrays.py"""

          %load_ext memory_profiler
          from bmi_arrays import calc_bmi_arrays
          %mprun -f calc_bmi_arrays calc_bmi_arrays(sample_indices,hts,wts)
"""Filename: /tmp/tmpxni4ho9v/bmi_arrays.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     1    109.5 MiB    109.5 MiB           1   def calc_bmi_arrays(sample_indices, hts, wts):
     2                                         
     3                                             # Gather sample heights and weights as arrays
     4    109.5 MiB      0.0 MiB           1       s_hts = hts[sample_indices]
     5    109.5 MiB      0.0 MiB           1       s_wts = wts[sample_indices]
     6                                         
     7                                             # Convert heights from cm to m and square with broadcasting
     8    109.5 MiB      0.0 MiB           1       s_hts_m_sqr = (s_hts / 100) ** 2
     9                                         
    10                                             # Calculate BMIs as an array using broadcasting
    11    109.5 MiB      0.0 MiB           1       bmis = s_wts / s_hts_m_sqr
    12                                         
    13    109.5 MiB      0.0 MiB           1       return bmis"""

"""--------After you've finished coding, answer the following question:
How much memory do the array indexing and broadcasting lines of code consume in the calc_bmi_array()
function? (i.e., what is the total sum of the Increment column for these four lines of code?)"""

      # answer: 0.1 MiB - 2.0 MiB-----> 9.5 MiB 
#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## Bringing it all together: Star Wars profiling

# Use get_publisher_heroes() to gather Star Wars heroes
star_wars_heroes = get_publisher_heroes(heroes, publishers, 'George Lucas')

print(star_wars_heroes)
print(type(star_wars_heroes))

# Use get_publisher_heroes_np() to gather Star Wars heroes
star_wars_heroes_np = get_publisher_heroes_np(heroes, publishers, 'George Lucas')

print(star_wars_heroes_np)
print(type(star_wars_heroes_np))

"""['Darth Vader', 'Han Solo', 'Luke Skywalker', 'Yoda']
<class 'list'>
['Darth Vader' 'Han Solo' 'Luke Skywalker' 'Yoda']
<class 'numpy.ndarray'>"""

## Bringing it all together: Star Wars profiling 2

"""Question
Within your IPython console, load the line_profiler and use %lprun to profile the two functions for line-by-line runtime. 
When using %lprun, use each function to gather the Star Wars heroes as you did in the previous step. After you've finished profiling, answer the following question:

          def get_publisher_heroes_np(heroes, publishers, desired_publisher):
              heroes_np = np.array(heroes)
              pubs_np = np.array(publishers)

              desired_heroes = heroes_np[pubs_np == desired_publisher]
              return desired_heroes"""


        %lprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, 'George Lucas')
  """Function: get_publisher_heroes at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def get_publisher_heroes(heroes, publishers, desired_publisher):
     2                                           
     3         1          2.0      2.0      0.4      desired_heroes = []
     4                                           
     5       481        283.0      0.6     50.8      for i,pub in enumerate(publishers):
     6       480        251.0      0.5     45.1          if pub == desired_publisher:
     7         4         20.0      5.0      3.6              desired_heroes.append(heroes[i])
     8                                           
     9         1          1.0      1.0      0.2      return desired_heroes"""
        %lprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes, publishers, 'George Lucas')
   """Function: get_publisher_heroes_np at line 12

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    12                                           def get_publisher_heroes_np(heroes, publishers, desired_publisher):
    13                                           
    14         1         87.0     87.0     36.1      heroes_np = np.array(heroes)
    15         1        133.0    133.0     55.2      pubs_np = np.array(publishers)
    16                                           
    17         1         21.0     21.0      8.7      desired_heroes = heroes_np[pubs_np == desired_publisher]
    18                                           
    19         1          0.0      0.0      0.0      return desired_heroes"""

       # get_publisher_heroes_np() is faster.
    
## Bringing it all together: Star Wars profiling 3

      %load_ext memory_profiler
      from hero_funcs import get_publisher_heroes, get_publisher_heroes_np
      %mprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, 'George Lucas')
      """Filename: /tmp/tmpt9jis3af/hero_funcs.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4    109.3 MiB    109.3 MiB           1   def get_publisher_heroes(heroes, publishers, desired_publisher):
     5                                         
     6    109.3 MiB      0.0 MiB           1       desired_heroes = []
     7                                         
     8    109.3 MiB      0.0 MiB         481       for i,pub in enumerate(publishers):
     9    109.3 MiB      0.0 MiB         480           if pub == desired_publisher:
    10    109.3 MiB      0.0 MiB           4               desired_heroes.append(heroes[i])
    11                                         
    12    109.3 MiB      0.0 MiB           1       return desired_heroes"""
      %mprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes, publishers, 'George Lucas')
      """Filename: /tmp/tmpt9jis3af/hero_funcs.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    15    109.3 MiB    109.3 MiB           1   def get_publisher_heroes_np(heroes, publishers, desired_publisher):
    16                                         
    17    109.3 MiB      0.0 MiB           1       heroes_np = np.array(heroes)
    18    109.3 MiB      0.0 MiB           1       pubs_np = np.array(publishers)
    19                                         
    20    109.3 MiB      0.0 MiB           1       desired_heroes = heroes_np[pubs_np == desired_publisher]
    21                                         
    22    109.3 MiB      0.0 MiB           1       return desired_heroes"""

    """----- Which function uses the least amount of memory?...."""
    # Both functions have the same memory consumption.

## Bringing it all together: Star Wars profiling 4

    """----- Based on your runtime profiling and memory allocation profiling, which function would you choose to gather Star Wars heroes?...."""
    # I could use either function since their runtimes, and memory usage were identical.


