"""**************************************************************************************************************************************************************
goal of this course is to transform you into a Python expert, and so the first chapter starts off with best practices when writing functions.
You'll cover docstrings and why they matter and how to know when you need to turn a chunk of code into a function. You will also learn the details of how Python passes 

Docstrings
==========
- makes your code easier to use, read, maintain

    @ anatomy of docstring
    -----------------------
      def func_name(arguments):
        '''
         Description of what it does 
         Description of argument(s) if any
         Description of return value(s) if any
         Description of errors raised if any
         Optional extra notes or examples
         '''
    @ docstring Formats
    -----------------------     
    - Google style (pupular)  - NumpyDoc (popular)  - reStructuredText    - EpyText
    
      ----Google style === straight to the point eg. '''Stack the columns''' and just Arg:, Raises: , Returns: , Notes:
      ----NumpyDoc     === more vertical with line tittles, takes more space
      
    @ Review Documentation
    -----------------------
    >>>>>>>> func_name.__doc__ ====review documentation
    >>>>>>>> .getdoc(dunc_name) (inspect module)
    
        ++
            import inspect
            print(inspect.getdoc(func_name))
**************************************************************************************************************************************************************"""
## Crafting a docstring

# Add a docstring to count_letter()
def count_letter(content, letter):
  """Count the number of times `letter` appears in `content`.
  
  # Add a Google style arguments section
  Args:
    content (str): The string to search.
    letter (str): The letter to search for.
    
  # Add a returns section
  Returns:
    int
    
  # Add a section detailing what errors might be raised
  Raises:
    ValuError: If `letter` is not a one-character string
  """
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('`letter` must be a single character string.')
  return len([char for char in content if char == letter])
#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## Retrieving docstrings

# Get the "count_letter" docstring by using an attribute of the function
docstring = count_letter.__doc__

border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))

## Retrieving docstrings 2

import inspect

# Inspect the count_letter() function to get its docstring
docstring = inspect.getdoc(count_letter)

"""add borders"""
border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))

## Retrieving docstrings 3

import inspect

def build_tooltip(function):
  """Create a tooltip for any function that shows the
  function's docstring.

  Args:
    function (callable): The function we want a tooltip for.

  Returns:
    str
  """
  # Get the docstring for the "function" argument by using inspect
  docstring = inspect.getdoc(function)
  border = '#' * 28
  return '{}\n{}\n{}'.format(border, docstring, border)

print(build_tooltip(count_letter))
print(build_tooltip(range))
print(build_tooltip(print))
"""!!!
. But when we want to print the docstring, removing those leading spaces with inspect.getdoc() will look much better."""
#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## Docstrings to the rescue!

"""---Examine each of these functions' docstrings in the IPython shell to determine which of them is actually numpy.histogram()."""
"""     numpy.leyud(),  numpy.uqka(),   numpy.fywdkxa(),    numpy.jinzyxq()     """
import inspect
inspect.getdoc(numpy.fywdkxa)
'''Compute the histogram of a set of data.'''

# numpy.fywdkxa()
"""**************************************************************************************************************************************************************
DRY and "Do One Thing"
=====================
    - Dry: Don't repeat yourself
    - Do one thing: funtion for doing 1 thing
            / more flexible     / easily undertood      / simpler to test        / simpler to debug     / easier to change       
    / Use functions to avoid repetition
    - Refactor: improving code by changing it a little bit at a time
**************************************************************************************************************************************************************"""
