"""********************************************************************************************************************************************
If you've ever seen the "with" keyword in Python and wondered what its deal was, then this is the chapter for you! Context managers 
are a convenient way to provide connections in Python and guarantee that those connections get cleaned up when you are done using them.
This chapter will show you how to use context managers, as well as how to write your own.

Context manager
==============
- with open: when you were done reading the text, the context manager closed the file for you.

>>>>>>>>>> with  <context-manager>(<args>) as <variable-name>:
....            # Run code here, is inside context

--- sets up context   ---runs code    ---removes context

real world eg
=============

    ++  
      with open('my_text_file.txt') as my_file:
            text =  my_file.read()
            lenght = len(text)
      print('the file is {} chars long'.format(lenght))
      
      # print statement is outside so when task is done, it gets cleaned
********************************************************************************************************************************************"""
## The number of cats

# Open "alice.txt" and assign the file to "file"
""" Count the times word cat is used in the file"""
with open('alice.txt') as file:
  text = file.read()

n = 0
for word in text.split():
  if word.lower() in ['cat', 'cats']:
    n += 1

print('Lewis Carroll uses the word "cat" {} times'.format(n))
#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## The speed of cats

image = get_image_from_instagram()

# Time how long process_with_numpy(image) takes to run
with timer():
  print('Numpy version')
  process_with_numpy(image)

# Time how long process_with_pytorch(image) takes to run
with timer():
  print('Pytorch version')
  process_with_pytorch(image)
"""Numpy version
Processing..........done!
Elapsed: 1.53 seconds
Pytorch version
Processing..........done!
Elapsed: 0.33 seconds"""

"""!!!
pytorch version is faster,timer() is a context manager that does not return a value, so the as <variable name> at the end of the with statement isn't necessary"""

"""********************************************************************************************************************************************
Writing context managers
=========================

  @ Create context manager
    ----------------------
    ---define funtion    ---set up code   ---yield    ---optional:add teardown code   ---add decorator:@contextlib.contextmanager    
    
    yield: is like return
    
    ++
        @contextlib.contextmanager
        def my_context():
            print('hello')
            yield 42
            print('goodbye')
        
        with my_context() as foo:
            print('foo is {}'.format(foo))
        
        # hello
        # foos is 42
        # goodbye
     ++   
********************************************************************************************************************************************"""
## The timer() context manager

# Add a decorator that will make timer() a context manager
@contextlib.contextmanager
def timer():
  """Time the execution of a context block.

  Yields:
    None
  """
  start = time.time()
  # Send control back to the context block
  yield None
  end = time.time()
  print('Elapsed: {:.2f}s'.format(end - start))

with timer():
  print('This should take approximately 0.25 seconds')
  time.sleep(0.25)
 #``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````   
## A read-only open() context manager

@contextlib.contextmanager
def open_read_only(filename):
  """Open a file in read-only mode.

  Args:
    filename (str): The location of the file to read

  Yields:
    file object
  """
  read_only_file = open(filename, mode='r')
  # Yield read_only_file so it can be assigned to my_file
  yield read_only_file
  # Close read_only_file
  read_only_file.close()

with open_read_only('my_file.txt') as my_file:
  print(my_file.read())
"""********************************************************************************************************************************************
Advanced topics
===============
********************************************************************************************************************************************"""
## Context manager use cases
"""---Which of the following would NOT be a good opportunity to use a context manager?"""

# A function that prints all of the prime numbers between 2 and some value n.
#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## Scraping the NASDAQ

# Use the "stock('NVDA')" context manager
# and assign the result to the variable "nvda"
with stock('NVDA') as nvda:
  # Open "NVDA.txt" for writing as f_out
  with open('NVDA.txt', 'w') as f_out:
    for _ in range(10):
      value = nvda.price()
      print('Logging ${:.2f} for NVDA'.format(value))
      f_out.write('{:.2f}\n'.format(value))
"""Opening stock ticker for NVDA
    Logging $139.50 for NVDA
    Logging $139.54 for NVDA
    Logging $139.61 for NVDA....."""
"""!!!
 Nesting context managers like this allows you to connect to the stock market """

