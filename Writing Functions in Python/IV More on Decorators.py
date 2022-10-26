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
==========================="""
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

