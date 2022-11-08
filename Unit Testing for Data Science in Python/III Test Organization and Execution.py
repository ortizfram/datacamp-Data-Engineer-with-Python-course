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
#|
#|
### One command to run them all
"""Instructions 1/4
Question
-In the IPython console, what is the correct command for running all tests contained in the tests folder?"""
# you are already in test folder 
!pytest
#|
"""Instructions 2/4
Question
-When you run all tests with the command !pytest, how many of them pass and how may fail?"""
!pytest
# Passing: 15, Failing: 1
#|
"""instructions 3/4
Question
-Assuming that you simply want to answer the binary question "Are all tests passing" without wasting time and resources, what is the correct command to 
 run all tests till the first failure is encountered?"""
!pytest -x
#|
"""Instructions 4/4
Question
-When you ran the tests using the !pytest -x command, how many tests ran in total before test execution stopped because of the first failing test?"""
#15
#|
#|
### Running test classes
"""Instructions 1/4
-Fill in with a float between 0 and 1 so that num_training is approximately 3/4
 of the number of rows in data_array."""
import numpy as np

def split_into_training_and_testing_sets(data_array):
    dim = data_array.ndim
    if dim != 2:
        raise ValueError("Argument data_array must be two dimensional. Got {0} dimensional array instead!".format(dim))
    num_rows = data_array.shape[0]
    if num_rows < 2:
        raise ValueError("Argument data_array must have at least 2 rows, it actually has just {0}".format(num_rows))
    # Fill in with the correct float
    num_training = int(0.5 * data_array.shape[0])
    permuted_indices = np.random.permutation(data_array.shape[0])
    return data_array[permuted_indices[:num_training], :], data_array[permuted_indices[num_training:], :]
#|
"""Instructions 2/4
Question
-What is the correct command to run all the tests in this test class using node IDs?"""
!pytest models/test_train.py::TestSplitIntoTrainingAndTestingSets
#|
"""instructions 3/4
Question
-What is the correct command to run only the previously failing test test_on_six_rows() using node IDs?"""
!pytest models/test_train.py::TestSplitIntoTrainingAndTestingSets::test_on_six_rows
#|
"""Instructions 4/4
Question
-What is the correct command to run the tests in TestSplitIntoTrainingAndTestingSets using keyword expressions?"""
!pytest -k "SplitInto"
#|
#|
"""
\*** Expected failures and conditional skipping/
    
      > marking tests a 'expected to fail' @
      >>>>>> xfail
      ## could happen when function is not implemented but has tests, it will give an error. but it's good
      # important! : test would be reported as failed, but it'll pass
      eg:|
           import pytest
           
           class TestTrainModel(object):
           @pytest.mark.xfail
           def test_on_linear_data(self):
         | ...
          ______
      
      > expected failures but CONDiTIONALLY
      # skip test conditionally
      >>>>>> skipif
      eg:|
            class TestConverToInt(object):
                @pytest.mark.skipif(reason="Using TDD, train model is not implemented")
                def test_with_no_comma(self):
                    '''only runs py 2.7 or lower'''
                    test_argument = "756"
                    expected = 756
                    actual = convert_to_int(test_argument)
                    message= unicode("Expected 2081, Actual: {0}".format(actual))
         |         assert actual == expected, message
          _______
       > show reason
       >>>>>> pytest -r  -rs : reason for skipping
       > reason for expected failures in the test result report
       >>>>>> pytest -rx
       > reason for both skipped tests and tests that are expected to fail 
       >>>>>> pytest -rsx 
"""
#|
#|
### Mark a test class as expected to fail
"""Instructions 1/3
Question
-Run the tests in the test class TestModelTest in the IPython console. What is the outcome?"""
!pytest models/test_train.py::TestModelTest
# Answer: The tests fail with NameError since the function model_test() has not yet been defined
#|
"""Instructions 2/3
-Mark the whole test class TestModelTest as "expected to fail"."""
# Mark the whole test class as "expected to fail"
@pytest.mark.xfail
class TestModelTest(object):
    def test_on_linear_data(self):
        test_input = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        expected = 1.0
        actual = model_test(test_input, 2.0, 1.0)
        message = "model_test({0}) should return {1}, but it actually returned {2}".format(test_input, expected, actual)
        assert actual == pytest.approx(expected), message
        
    def test_on_one_dimensional_array(self):
        test_input = np.array([1.0, 2.0, 3.0, 4.0])
        with pytest.raises(ValueError) as exc_info:
            model_test(test_input, 1.0, 1.0)
#|
"""Instructions 3/3
-Add the following reason for the expected failure: "Using TDD, model_test() has not yet been implemented"."""
# Add a reason for the expected failure
@pytest.mark.xfail(reason="Using TDD, model_test() has not yet been implemented")
class TestModelTest(object):
    def test_on_linear_data(self):
        test_input = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        expected = 1.0
        actual = model_test(test_input, 2.0, 1.0)
        message = "model_test({0}) should return {1}, but it actually returned {2}".format(test_input, expected, actual)
        assert actual == pytest.approx(expected), message
        
    def test_on_one_dimensional_array(self):
        test_input = np.array([1.0, 2.0, 3.0, 4.0])
        with pytest.raises(ValueError) as exc_info:
            model_test(test_input, 1.0, 1.0)
#|
#|
### Mark a test as conditionally skipped
"""Instructions 1/4
Question
-Run the tests in the test class TestGetDataAsNumpyArray in the IPython console. What is the outcome?"""
!pytest features/test_as_numpy.py::TestGetDataAsNumpyArray
# Answ: The test test_on_clean_file() fails with a NameError because Python 3 does not recognize the xrange() function.
#|
"""2/4
-Import the sys module."""
import sys
#|
"""3/4
-Mark the test test_on_clean_file() as skipped if the Python version is greater than 2.7."""
# Import the sys module
import sys

class TestGetDataAsNumpyArray(object):
    # Mark as skipped if Python version is greater than 2.7
    @pytest.mark.skipif(sys.version_info > (2, 7))
    def test_on_clean_file(self):
        expected = np.array([[2081.0, 314942.0],
                             [1059.0, 186606.0],
                             [1148.0, 206186.0]
                             ]
                            )
        actual = get_data_as_numpy_array("example_clean_data.txt", num_columns=2)
        message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
        assert actual == pytest.approx(expected), message
#|
"""4/4
-Add the following reason for skipping the test: "Works only on Python 2.7 or lower"."""
# Import the sys module
import sys

class TestGetDataAsNumpyArray(object):
    # Add a reason for skipping the test
    @pytest.mark.skipif(sys.version_info > (2, 7), reason="Works only on Python 2.7 or lower")
    def test_on_clean_file(self):
        expected = np.array([[2081.0, 314942.0],
                             [1059.0, 186606.0],
                             [1148.0, 206186.0]
                             ]
                            )
        actual = get_data_as_numpy_array("example_clean_data.txt", num_columns=2)
        message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
        assert actual == pytest.approx(expected), message
#|
#|
### Reasoning in the test result report
"""Instructions 1/3
Question
-What is the command that would only show the reason for expected failures in the test result report?"""
# Answ: !pytest -rx
#|
"""2/3
Question
-What is the command that would only show the reason for skipped tests in the test result report?"""
# Answ: !pytest -rs.
#|
"""3/3
Question
-What is the command that would show the reason for both skipped tests and tests that are expected to fail in the test result report?"""
# Answ: !pytest -rsx.
#|
#|
"""
\*** Continuous integration and code coverage
      
      
