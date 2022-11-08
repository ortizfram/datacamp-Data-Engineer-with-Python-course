"""
In this chapter, we will learn about how to structure your test suite well, how to effortlessly execute any subset of tests and how to mark problematic 
tests so that your test suite always stays green. The last lesson will even enable you to add the trust-inspiring build status and code coverage badges to 
your own project. Complete this chapter and become a unit testing wizard!
"""
"""
\*** How to organize a growing set of tests?
  \project structure/
  
     |src/  # all app code lives here
     |  |--data/  # package for data pre-processing
     |  |---__init__.py
     |  |---preprocessing_helpers.py   # contains functions(); like row_to_list()
     |--features/               # package for feature generation  from preprocessed data
     |  |--__init__.py
     |  |--as_numpy.py           # get_data_as_np_array()
     |--models/                 # package for linear regression model
     |  |--__init__.py
     |  |--train.py
     |tests/              # Test suite: all tests live here
        |--data/  # package for data pre-processing
        |   |---__init__.py
        |   |---preprocessing_helpers.py   # contains functions(); like row_to_list()
        |--features/               # package for feature generation  from preprocessed data
        |   |--__init__.py
        |   |--as_numpy.py           # get_data_as_np_array()
        |--models/                 # package for linear regression model
            |--__init__.py
            |--train.py
          
  \Python module---to test_module correspondence/
  
      # module must have it's test module
      >>>>>> x_module.py------test_x_module.py (inside test data)

      @ test class:
        > is a container for single unit tests  
        |eg: 
             class TestRowToList(object):                 # Always put arg object  # Use CamelCase
                  def test_on_no_tab_missing_value(self):   #Always put self arg
                  ...
                  def test_on_two_tab_missing_value(self):  #Always put self arg 
"""
#|
### Place test modules at the correct location
"""In the package, there is a Python module plots.py, which contain functions related to plotting. These functions should be tested in a test module test_plots.py.
-According to pytest guidelines, where should you place this test module within the project structure?"""
tests/visualization/test_plots.py.
#|
#|
### Create a test class
""" Instructions
- Declare the test class for the function split_into_training_and_testing_sets(), making sure to give it a name that follows the standard naming convention.
- Fill in the mandatory argument in the test test_on_one_row()."""
import pytest
import numpy as np

from models.train import split_into_training_and_testing_sets

# Declare the test class
class TestSplitIntoTrainingAndTestingSets(object):
    # Fill in with the correct mandatory argument
    def test_on_one_row(self):
        test_argument = np.array([[1382.0, 390167.0]])
        with pytest.raises(ValueError) as exc_info:
            split_into_training_and_testing_sets(test_argument)
        expected_error_msg = "Argument data_array must have at least 2 rows, it actually has just 1"
        assert exc_info.match(expected_error_msg)
"""
  \Mastering test execution/
      -> runing all tests together
      |eg: 
          cd tests
          pytest
      # we might do this: after commit is pushed to code-base
      
      -> flag to stop after first failing test
      >>>>>> pytest -x
      
      -> runing tests in a test module
      >>>>>> pytest data/test_preprocessing_helpers.py
      
      -> runing only particular test class 
      # node ID (of a test class)
      >>>>>> <path to test module>::<test class name>
      # node ID (of an unit test)
      >>>>>> <path to test module>::<test class name>::<unit test name>
      
        --> run test class using Node ID
        # runs all class tests
        >>>>>> !pytest data/test_preprocessing_helpers.py::TestRowToList
        
        --> run unit test using Node ID
        # only runs a single test 
        >>>>>> !pytest data/test_preprocessing_helpers.py::TestRowToList::test_on_one_tab_with_missing_value  

      ---> runing using keyword expressions
      ## fastest way of runing
      # (-k) runs all test whose Node ID matches 'pattern' 
      -k >>>>>> pytest -k "TestSplitIntoTrainingAndTestingSets" 
      ## we can also write a part-name of the class as long as is unique
      
      .---> Supports Logical Operators
      # do all testSplit except 'test_on_one_row'
      >>>>>> pytest -k "TestSplit and not test_on_one_row"
"""
