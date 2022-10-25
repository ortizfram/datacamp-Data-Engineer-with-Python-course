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
