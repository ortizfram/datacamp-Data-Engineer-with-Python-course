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

  >>>>>>>>> global === to change x inside function, so when calling function and when calling x both are the same. local and non-local
  >>>>>>>>> nonlocal === same but from funciton outside
**********************************************************************************************************************************************************"""
## Understanding scope

"""---What four values does this script print?"""
 # ++  
      x = 50

      def one():
        x = 10

      def two():
        global x
        x = 30

      def three():
        x = 100
        print(x)

      for func in [one, two, three]:
        func()
        print(x)
# ++

# 50, 30, 100, 30
"""!!!
one() doesn't change the global x, so the first print() statement prints 50.

two() does change the global x so the second print() statement prints 30.

The print() statement inside the function three() is referencing the x value that is local to three(), so it prints 100.

But three() does not change the global x value so the last print() statement prints 30 again."""
#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## Modifying variables outside local scope

call_count = 0

def my_function():
  """Add a keyword that lets us update call_count from inside the function."""
  # Use a keyword that lets us update call_count 
  global call_count
  call_count += 1
  
  print("You've called my_function() {} times!".format(
    call_count
  ))
  
for _ in range(20):
  my_function()
"""<script.py> output:
    You've called my_function() 1 times!
    You've called my_function() 2 times!
    You've called my_function() 3 times!.....20"""

## Modifying variables outside local scope 2

def read_files():
  file_contents = None
  
  def save_contents(filename):
    """Add a keyword that lets us modify file_contents from inside save_contents()."""
    # Add a keyword that lets us modify file_contents
    nonlocal file_contents
    if file_contents is None:
      file_contents = []
    with open(filename) as fin:
      file_contents.append(fin.read())
      
  for filename in ['1984.txt', 'MobyDick.txt', 'CatsEye.txt']:
    save_contents(filename)
    
  return file_contents

print('\n'.join(read_files()))

## Modifying variables outside local scope 3

def wait_until_done():
  def check_is_done():
    # Add a keyword so that wait_until_done() 
    # doesn't run forever
    global done
    if random.random() < 0.1:
      done = True
      
  while not done:
    check_is_done()

done = False
wait_until_done()

print('Work done? {}'.format(done))

#  Work done? True

"""**********************************************************************************************************************************************************
Closures
========

>>>>>>>> my_func.__closure__ ===== a function object that remembers values in enclosing scopes even if they are not present in memory.
>>>>>>>>  closure_values = [ my_func.__closure__[i].cell_contents for i in range(2)] ===== get values for closure
**********************************************************************************************************************************************************"""
## Checking for closure

def return_a_func(arg1, arg2):
  def new_func():
    print('arg1 was {}'.format(arg1))
    print('arg2 was {}'.format(arg2))
  return new_func
    
my_func = return_a_func(2, 17)

# Show that my_func()'s closure is not None
print(my_func.__closure__ is not None)

# True

## Checking for closure 2
"""Show that there are two variables in the closure"""

def return_a_func(arg1, arg2):
  def new_func():
    print('arg1 was {}'.format(arg1))
    print('arg2 was {}'.format(arg2))
  return new_func
    
my_func = return_a_func(2, 17)

print(my_func.__closure__ is not None)

# Show that there are two variables in the closure
print(len(my_func.__closure__) == 2)

# True

## Checking for closure 3
"""Get the values of the variables in the closure"""

def return_a_func(arg1, arg2):
  def new_func():
    print('arg1 was {}'.format(arg1))
    print('arg2 was {}'.format(arg2))
  return new_func
    
my_func = return_a_func(2, 17)

print(my_func.__closure__ is not None)
print(len(my_func.__closure__) == 2)

# Get the values of the variables in the closure
closure_values = [
  my_func.__closure__[i].cell_contents for i in range(2)
]
print(closure_values)
print(closure_values == [2, 17])

"""True
  True
  [2, 17]
  True"""
#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## Closures keep your values safe

def my_special_function():
  print('You are running my_special_function()')
  
def get_new_func(func):
  def call_func():
    func()
  return call_func

new_func = get_new_func(my_special_function)

# Redefine my_special_function() to just print "hello"
def my_special_function():
  print("hello")

new_func()

# You are running my_special_function()

## Closures keep your values safe 2

def my_special_function():
  print('You are running my_special_function()')
  
def get_new_func(func):
  def call_func():
    func()
  return call_func

new_func = get_new_func(my_special_function)

# Delete my_special_function()
"""Show that even if you delete my_special_function(), you can still call new_func() without any problems."""
del(my_special_function)

new_func()

# You are running my_special_function()

## Closures keep your values safe 3

def my_special_function():
    print('You are running my_special_function()')


def get_new_func(func):
    def call_func():
        func()

    return call_func


# Overwrite `my_special_function` with the new function
"""you still get the original message even if you overwrite my_special_function() with the new function."""
my_special_function = get_new_func(my_special_function)

my_special_function()

#     You are running my_special_function()
"""**********************************************************************************************************************************************************
Decorators 
===========
  - modify behavior of functions
  
      @ decorator syntax
        ----------------
        ++
          
            def double_args(func):
                def wrapper(a,b):
                    return func(a*2 , b*2)
                return wrapper  
                
            @double_args
            def multiply(a,b):
                return a*b
                
            multiply(1,5)
            
            # 20
**********************************************************************************************************************************************************"""
## Using decorator syntax

"""You have written a decorator called print_args that prints out all of the arguments and their values any time a function that it is decorating gets called."""
def my_function(a, b, c):
  print(a + b + c)

# Decorate my_function() with the print_args() decorator by replacing my_fuction variable
my_function = print_args(my_function)

my_function(1, 2, 3)

# my_function was called with a=1, b=2, c=3
# 6

## Using decorator syntax 2

# Decorate my_function() with the print_args() decorator above
@print_args
def my_function(a, b, c):
  print(a + b + c)

my_function(1, 2, 3)

# my_function was called with a=1, b=2, c=3
# 6
#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## 
