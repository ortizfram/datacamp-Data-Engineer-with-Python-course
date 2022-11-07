"""
you will get introduced to the pytest package and use it to write simple unit tests. You'll run the tests,
interpret the test result reports and fix bugs. Throughout the chapter, we will use examples exclusively from the data preprocessing module of a linear regression 
project, making sure you learn unit testing in the context of data science.
"""

"""
- how to test an implementation ?
  # test function on a few arg. to check whether return values is correct
  
*** life cycle of a function 
    - implement - test  
    - if pass: accepted impl.   - feature request/refactor
    - if fail: go bug-fix       - bug found/ bug fix
    
*** Unit test / manual test
    unit : automate repetitive testing process to save time
"""

"""
### How frequently is a function tested?
- Which of the following is true about testing?

Answer : 
A function is tested after the first implementation and then any time the function is modified, which happens mainly when new bugs are found, new features are
implemented or the code is refactored.
"""

"""
### Manual testing

Instructions 1/2
Question

- Call row_to_list() in the IPython console on the three arguments listed in the table. Do the actual return values match the expected return values listed in the table?
"""
In [3]:
row_to_list("2,081\t314,942\n")
Out[3]:
['2,081', '314,942']
In [4]:
row_to_list("\t293,410\n")
Out[4]:
['', '293,410']
In [5]:
row_to_list("1,463238,765\n")

# Answer: No. the function returns ["", "293,410"] for the argument "\t293,410\n" instead of the expected return value None.
"""
Instructions 2/2
Question

- We have implemented a corresponding bug fix in a new function row_to_list_bugfix(). Call row_to_list_bugfix() in the IPython console on the 
  three arguments listed in the table. Do the actual return values now match the expected return values listed in the table?
"""
In [6]:
row_to_list_bugfix("2,081\t314,942\n")
Out[6]:
['2,081', '314,942']
In [7]:
row_to_list_bugfix("\t293,410\n")
In [8]:
row_to_list_bugfix("1,463238,765\n")

# Answer: Yes, the implementation returns the expected value in each case.

"""
*** Write a simple unit test using pytest
    *** test librarys : PYTEST : easiest, most popular, all essential features
    - create a file: test_function_to_test.py (naming convention)/ test module
    - import : pytest ,and function name to test 
    - test function must contain assert
    eg: 
        # If assert = True >> pass
        # If assert = False >> Error and fail
        
        def test_for_clean_row():
            assert row_to_list("2,081\t314,942\n") == \
            ["2,081", "314,942"]
        
        def test_for_missing_area():
            assert row_to_list("\t293,410\n") is None
            
    - Runing unit tests : pytest test_filename.py
"""

"""
### Your first unit test using pytest

The convert_to_int() function takes a comma separated integer string as argument, and returns the integer. Therefore, 
the expected return value of convert_to_int("2,081") is the integer 2081.
This function is defined in the module preprocessing_helpers.py
"""
# Import the pytest package
import pytest

# Import the function convert_to_int()
from preprocessing_helpers import convert_to_int

# Complete the unit test name by adding a prefix
def test_on_string_with_one_comma():
  # Complete the assert statement
  assert convert_to_int("2,081") == 2081

"""
### Running unit tests
Tests that you wrote in the previous exercise have been written to a test module test_convert_to_int.py. Try running the tests in the IPython console.
-What is the correct IPython console command to run the tests in this test module?

Answer: !pytest test_convert_to_int.py
"""

"""
### What causes a unit test to fail?
In the test result report, the character ., as shown below, stands for a passing test. A passing test is good news as it means
that your function works as expected. The character F stands for a failing test. A failing test is bad news as this means that something is broken.

test_row_to_list.py .F.                                                  [100%]
-Which of the following describes best why a unit test fails?

Answer: An exception is raised when running the unit test. This could be an AssertionError raised by the assert statement
or another exception, e.g. NameError, which is raised before the assert statement can run.
"""

"""
### Spotting and fixing bugs
instructions 1/2
Question

-Run the unit test in the test module test_convert_to_int.py in the IPython console. Read the test result report and spot the bug.
-Which of the following describes the bug in the function convert_to_int(), if any?
Answer: convert_to_int("2,081") is expected to return the integer 2081, but it is actually returning the string "2081"
"""

"""
### Spotting and fixing bugs
-Fix the convert_to_int() function so that it returns the integer 2081 instead of the string "2081" for the argument "2,081"
"""
def convert_to_int(string_with_comma):
    # Fix this line so that it returns an int, not a str
    return int(string_with_comma.replace(",", ""))
  
"""
*** More benefits and test types
    - time saving
    - for guessing function purpose improving doc: !cat module_name.py
    - increase trust : verifying that function works
    - reduce downtime
    
    *** integration test : check if multiple units work well together when connected
    
    *** end-to-end test : checks whole software at once
"""

"""
### Benefits of unit testing
- The CEO is unsure, and asks you about the benefits that unit testing might bring. In your response, which of the following benefits should you include?
1@ Time savings, leading to faster development of new features.
2@ Better user experience due to faster code execution.
3@ Improved documentation, which will help new colleagues understand the code base better.
4@ More user trust in the software product.
5@ Better user experience due to improved visualizations.
6@ Better user experience due to reduced downtime.

Answer: 1, 3, 4 and 6.
"""

"""
### Unit tests as documentation
-Having read the unit tests, can you guess what mystery_function() does?
    !cat mystery_function.py
    
    Answer: It converts data in a data file into a NumPy array.
"""
