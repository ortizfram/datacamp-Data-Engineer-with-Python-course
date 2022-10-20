"""DEFINING EFFICIENT
---------------------
    - Fast runtime(- time)
    - Minimal resource consumption(- memory)
\\"""## example
  # Non pythonic
  doubled_numbers= []
  for i in range(len(numbers)):
     doubled_numbers.append(numbers[i]*2)
  # Pythonic
  doubled_numbers= [x * 2 for x in numbers]
#``````````````````````````````````````````````````````````````````````````````````````````````````
"""
##Pop quiz: what is efficient

In the context of this course, what is meant by efficient Python code?

    # Code that executes quickly for the task at hand, minimizes the memory footprint and follows Python's coding style principles."""
#``````````````````````````````````````````````````````````````````````````````````````````````````
## A taste of things to come 1== Non-pythonic

 names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
    
# Print the list w/ Non-Pythonic approach
i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
print(new_list)
#``````````````````````````````````````````````````````````````````````````````````````````````````
## A taste of things to come 2== more Pythonic way

# Print the list created by looping over the contents of names
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)
#``````````````````````````````````````````````````````````````````````````````````````````````````
## A taste of things to come 3== The Pythoniest way

# Print the list created by using list comprehension
best_list = [name for name in names if len(name) >= 6]
print(best_list)
#``````````````````````````````````````````````````````````````````````````````````````````````````
### What is the 7th idiom of the Zen of Python?

import this
#The Zen of Python, by Tim Peters
        # Readability counts.
"""*********************************************************************************************************************
Built-in types
===============
    >>>>>> list, >>>>>> tuple, >>>>>> set, >>>>>> dict
    
Built-in functions
=================    
    >>>>>> print(), >>>>>> len(), >>>>>> range(), >>>>>> enumerate(), >>>>>> round(), >>>>>> map(), >>>>>> zip()
    
    map() === (returnedValue, toWhat)--- in iterables
    
Built-in modules
================= 
    >>>>>> os, >>>>>> sys, >>>>>> itertools, >>>>>> collections, >>>>>> math   
******************************************************************************************************************"""
### Built-in practice: range()

# Create a range object that goes from 0 to 5
nums = range(0,6)
print(type(nums))

# Convert nums to a list
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1,12,2)] # start , end(exclusive), step
print(nums_list2)

#$$$ unpacking a range object(*) same as using-----nums_list = list(nums) $$$
# <class 'range'>
# [0, 1, 2, 3, 4]
# [1, 3, 5, 7, 9, 11]
#``````````````````````````````````````````````````````````````````````````````````````````````````
### Built-in practice: enumerate()

# Non-Pythonic
# Rewrite the for loop to use enumerate
indexed_names = []
for i,name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)

# more Pythonic 
# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(indexed_names_comp)

# The Pythoniest
# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, 1)] 
print(indexed_names_unpack)
"""read as: list, unpack & enumerate(names, startingWithOne)"""
#``````````````````````````````````````````````````````````````````````````````````````````````````
### Built-in practice: map()

# names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# Use map to apply str.upper to each element in names
names_map  = map(str.upper, names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*names_map]

# Print the list created above
print(names_uppercase)
"""******************************************************************************************************************
NumPy arrays
=================
$$ Alternative to Python Lists

    - np is homogeneous.same type
    
                    import numpy as np
                    nums_np = ap.array(range(5))
            
    - np. array broadcasting (calculations for entire array)
            
                    nums_np = np.array([-2,-1,0,1,2])
                    nums_np ** 2
                    # array([4,2,0,1,4])
            
    - np 2D array best indexing
    
        -- basic python:
                    nums2= [[1,2,3],[4,5,6]]
                    nums2[0][1]
                    # 2

        -- np python is easier
                    nums2[0,1]
                    # 2

                    # get both list first item
                    nums2[:,0]
                    # array([1,4])
                    
     - np boolean indexing
                    
                    nums= [-2, -1, 0, 1, 2]
                    nums_np = np.array(nums)
                    # boolean indexing
                    nums_np > 0
                    
                    #. array([False,False,False,True,True])
                    
                    # indexing/returning this array <-
                    
                    nums_np[nums_np > 0]
                    #. [1,2]
******************************************************************************************************************"""
### Practice with NumPy arrays 1

# Print second row of nums
print(nums[1,:])
# [ 6  7  8  9 10]

# Print all elements of nums that are greater than six
print(nums[nums > 6])
# [ 7  8  9 10]

# Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)
# [[ 2  4  6  8 10]
# [12 14 16 18 20]]
    
# Replace the third column of nums, adding 1 to each item in original column
nums[:,2] = nums[:,2] + 1
print(nums)
# [[ 1  2  4  4  5]
# [ 6  7  9  9 10]]
#``````````````````````````````````````````````````````````````````````````````````````````````````
"""Question

When compared to a list object, what are two advantages of using a numpy array?
        
        #  A numpy array contains homogeneous data types (which reduces memory consumption) 
            and provides the ability to apply operations on all elements through broadcasting."""
#``````````````````````````````````````````````````````````````````````````````````````````````````
### Bringing it all together: Festivus!

# Create a list of arrival times, let them know how many minutes late they are to your party.
arrival_times = [*range(10,60,10)]

print(arrival_times)
# [10, 20, 30, 40, 50]
#``````````````````````````````````````````````````````````````````````````````````````````````````
## Festivus 2

# Create a list of arrival times
arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times. your clock is three minutes fast.
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

print(new_times)
# [ 7 17 27 37 47]
#``````````````````````````````````````````````````````````````````````````````````````````````````
## Festivus 3

# Create a list of arrival times
arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[name],time) for name,time in enumerate(new_times)]

print(guest_arrivals)
# [('Jerry', 7), ('Kramer', 17), ('Elaine', 27), ('George', 37), ('Newman', 47)]
