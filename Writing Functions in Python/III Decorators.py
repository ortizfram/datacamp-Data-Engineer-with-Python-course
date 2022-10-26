"""**********************************************************************************************************************************************************
Decorators are an extremely powerful concept in Python. They allow you to modify the behavior of a function without changing the code of the function 
itself. This chapter will lay the foundational concepts needed to thoroughly understand decorators (functions as objects, scope, and closures),
and give you a good introduction into how decorators are used and defined

Functions are objects
=====================

**********************************************************************************************************************************************************"""
## Building a command line data app

# Add the missing function references to the function map
function_map = {
  'mean': mean,
  'std': std,
  'minimum': minimum,
  'maximum': maximum
}

data = load_data()
print(data)

func_name = get_user_input()

# Call the chosen function and pass "data" as an argument
function_map[func_name](data)
"""!!!
By adding the functions to a dictionary, you can select the function based on the user's input."""
#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## Reviewing your co-worker's code

# Call has_docstring() on the load_and_plot_data() function
ok = has_docstring(load_and_plot_data)

"""if doesnt have doc string """
if not ok:
  print("load_and_plot_data() doesn't have a docstring!")
else:
  print("load_and_plot_data() looks ok")
  
#  load_and_plot_data() looks ok
  
## Reviewing your co-worker's code 2
  
# Call has_docstring() on the as_2D() function
"""check if 2D has docstring"""
ok = has_docstring(as_2D)

if not ok:
  print("as_2D() doesn't have a docstring!")
else:
  print("as_2D() looks ok")

#   as_2D() looks ok
  
## Reviewing your co-worker's code 3

# Call has_docstring() on the log_product() function
ok = has_docstring(log_product)

if not ok:
  print("log_product() doesn't have a docstring!")
else:
  print("log_product() looks ok")

# log_product() doesn't have a docstring!

"""!!!
co-worker forgot to write a docstring for log_product(),
To pass a function as an argument to another function, you had to determine which one you were calling and which one you were referencing."""
#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## Returning functions for a math game

def create_math_function(func_name):
  if func_name == 'add':
    def add(a, b):
      return a + b
    return add
  elif func_name == 'subtract':
    # Define the subtract() function
    def subtract(a,b):
      return a - b
    return subtract
  else:
    print("I don't know that one")
    
add = create_math_function('add')
print('5 + 2 = {}'.format(add(5, 2)))

subtract = create_math_function('subtract')
print('5 - 2 = {}'.format(subtract(5, 2)))
"""!!!
 Since create_math_function() returns a function, we can then call those variables as functions."""

"""**********************************************************************************************************************************************************
Scope
======

**********************************************************************************************************************************************************"""
