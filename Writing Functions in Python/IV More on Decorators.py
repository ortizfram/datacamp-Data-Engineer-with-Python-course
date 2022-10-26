"""
this chapter gives you a bunch of real-world examples of when and how you would write decorators in your own code. You will also learn advanced 
decorator concepts like how to preserve the metadata of your decorated functions and how to write decorators that take arguments.
"""
"""Real-world examples
======================"""
#  +++
        import time
        
        def timer(func):
            """ A decorator that prints how long func took to run."""
            # Define wrapper func to return 
            def wrapper(*args, **kwargs):
              # When wrapper is called start timer
              t_start = time.time()
              # Call decorated func and store result
              result = func(*args, **kwargs)
              # Get total time it took to run 
              t_total = time.time() - t_start
              print('{} took {}s'.format(func.__name__, t_total))
              return result       
            return wrapper
          
# Using timer()
          
        @timer
        def sleep_n_seconds(n):
            time.sleep(n)
        
        sleep_n_seconds(5)
        
        # sleep_n_seconds took 5.005s
#   +++
"""=========="""

## Print the return type

def print_return_type(func):
  """Prints out the type of the variable that gets returned from every call of any function it is decorating."""
  # Define wrapper(), the decorated function
  def wrapper(*args, **kwargs):
    # Call the function being decorated
    result = func(*args, **kwargs)
    print('{}() returned type {}'.format(
      func.__name__, type(result)
    ))
    return result
  # Return the decorated function
  return wrapper
  
@print_return_type
def foo(value):
  return value
  
print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))

"""foo() returned type <class 'int'>
  42
  foo() returned type <class 'list'>
  [1, 2, 3]
  foo() returned type <class 'dict'>
  {'a': 42}"""
#----
## Counter

def counter(func):
  """decorator that adds a counter to each function that you decorate."""
  def wrapper(*args, **kwargs):
    wrapper.count += 1
    # actual function itself
    return func(*args, **kwargs)
    #reset counter
  wrapper.count = 0
  # Return the new decorated function
  return wrapper

# Decorate foo() with the counter() decorator
@counter
def foo():
  print('calling foo()')
  
foo()
foo()

print('foo() was called {} times.'.format(foo.count))

# calling foo()
# calling foo()
# foo() was called 2 times.

"""Decorators and metadata
===========================
>>>>>>>> from functools import wraps ==== add the metadata from wrapper to the decorated version of print_sum().
>>>>>>>> @wraps         ==== Decorate wrapper() so that it keeps func()'s metadata"""
## Preserving docstrings when decorating functions


def add_hello(func):
  def wrapper(*args, **kwargs):
    print('Hello')
    return func(*args, **kwargs)
  return wrapper

# Decorate print_sum() with the add_hello() decorator
@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)
  
print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)

# Hello
# 30
# None

## Preserving docstrings when decorating functions 2


# you're printing wrapper docstring , not add hello docstring"""
def add_hello(func):
  # Add a docstring to wrapper
  def wrapper(*args, **kwargs):
    """Print 'hello' and then call the decorated function."""

    print('Hello')
    return func(*args, **kwargs)
  return wrapper

@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)
  
print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)

# Hello
# 30
# Print 'hello' and then call the decorated function.

## Preserving docstrings when decorating functions 3


# Import the function you need to fix the problem
# will allow you to add the metadata from print_sum() to the decorated version of print_sum().
from functools import wraps

def add_hello(func):
  def wrapper(*args, **kwargs):
    """Print 'hello' and then call the decorated function."""
    print('Hello')
    return func(*args, **kwargs)
  return wrapper
  
@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)
  
print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)

## Preserving docstrings when decorating functions 4


from functools import wraps

def add_hello(func):
  # Decorate wrapper() so that it keeps func()'s metadata
  @wraps(func)
  def wrapper(*args, **kwargs):
    """Print 'hello' and then call the decorated function."""
    print('Hello')
    return func(*args, **kwargs)
  return wrapper
  
@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)
  
print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)

# Hello
# 30
# Adds two numbers and prints the sum
#----

## Measuring decorator overhead


@check_everything
def duplicate(my_list):
  """Return a new list that repeats the input twice"""
  return my_list + my_list

t_start = time.time()
duplicated_list = duplicate(list(range(50)))
t_end = time.time()
decorated_time = t_end - t_start

t_start = time.time()
# Call the original function instead of the decorated one
duplicated_list = duplicate.__wrapped__(list(range(50)))
t_end = time.time()
undecorated_time = t_end - t_start

print('Decorated time: {:.5f}s'.format(decorated_time))
print('Undecorated time: {:.5f}s'.format(undecorated_time))

# Finished checking inputs
# Finished checking outputs
# Decorated time: 1.74689s
# Undecorated time: 0.00026s
#----

"""Decorators that take arguments
=================================
        >>>>>>>>>   ==== for using a decorator that prints n times eg."""
#       ++
                def run_n_times(n):
                     """define and Return decorator
                     Returns: function 3 times"""
                     def decorator(func):
                        # wrapper that takes a range and applys function in wich you used decorator
                        def wrapper(*args, **kwargs):
                                for i in range(n):
                                      func(*args, **kwargs)
                        return wrapper
                     return decorator
                
                @run_n_times(3)
                def print_sum(a,b):
                        print(a+b)
                        
                print_sum(3,5)
                
                # 8
                # 8
                # 8
#       ++
#----

## Run_n_times()


# Make print_sum() run 10 times with the run_n_times() decorator
@run_n_times(10)
def print_sum(a, b):
  print(a + b)
  
print_sum(15, 20)

# 35....10times

## Run_n_times() 2


# Use run_n_times() to create the run_five_times() decorator
run_five_times = run_n_times(5)

@run_five_times
def print_sum(a, b):
  print(a + b)
  
print_sum(4, 100)

# 104....5times

## Run_n_times() 3


# modify the built-in print()
# Modify the print() function to always run 20 times
print = run_n_times(20)(print)

print('What is happening?!?!')

# What is happening?!?! .... 20times
#----

## HTML Generator


def html(open_tag, close_tag):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      msg = func(*args, **kwargs)
      return '{}{}{}'.format(open_tag, msg, close_tag)
    # Return the decorated function
    return wrapper
  # Return the decorator
  return decorator

## HTML Generator 2 


# Make hello() return bolded text
@html('<b>', '</b>')
def hello(name):
  return 'Hello {}!'.format(name)
  
print(hello('Alice'))

# <script.py> output:
#    <b>Hello Alice!</b>

## HTML Generator 3


# Make goodbye() return italicized text
@html('<i>', '</i>')
def goodbye(name):
  return 'Goodbye {}.'.format(name)
  
print(goodbye('Alice'))

# <i>Goodbye Alice.</i>

## HTML Generator 4


# Wrap the result of hello_goodbye() in <div> and </div>
@html('<div>','</div>')
def hello_goodbye(name):
  return '\n{}\n{}\n'.format(hello(name), goodbye(name))
  
print(hello_goodbye('Alice'))

# <div>
# <b>Hello Alice!</b>
# <i>Goodbye Alice.</i>
# </div>

"""Timeout(): a real world example
================================="""
