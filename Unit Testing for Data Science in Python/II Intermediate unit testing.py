"""
testing complicated data types like NumPy arrays to testing exception handling, you'll do it all. Once you have mastered the science of testing,
we will also focus on the arts. For example, we will learn how to find the balance between writing too many tests and too few tests. In the last lesson,
you will get introduced to a radically new programming methodology called Test Driven Development (TDD) and put it to practice. This might actually change
the way you code forever!
"""

"""
*** Mastering assert statements

    *** optional message argument
        >>>>> assert boolean_expression, message
            eg: 
                assert 1==2 , "One is not equal to two!"
                
                # this will not be printed since assert passed
                assert 1==1 , "this will not be printed since assert passed"
                
    *** Adding message to unit test
        import pytest
        
        def test_for_missing_area_with_message():
              actual = row_to_list("\t293,410\n")
              expected = None
              message = ("row_to_list('\t293,410\n')"
                         "returned {0} instead"
                         "of {1}".format(actual,expected)
                         )
             assert actual is expected, message
             
    *** with FLOATS we must use pytest.approx
        eg:
            assert np.array([0.1 + 0.1 + 0.1 ]) == pytest.approx(np.array([0.3]))
            
   *** MULTIPLE ASSERTIONS
      eg:
         import pytest
        
         def test_on_string_with_one_comma():
               return_value = convert_to_int("2,081")
               assert isinstance(return_value, int)
               assert return_value == 2081
"""

"""
### Write an informative test failure message
- Format the message string so that it shows the actual return value.
"""
import pytest
from preprocessing_helpers import convert_to_int

def test_on_string_with_one_comma():
    test_argument = "2,081"
    expected = 2081
    actual = convert_to_int(test_argument)
    # Format the string with the actual return value
    message = "convert_to_int('2,081') should return the int 2081, but it actually returned {0}".format(actual)
"""
- Write the assert statement that checks if actual is equal to expected and prints the message message if they are not equal.
"""
import pytest
from preprocessing_helpers import convert_to_int

def test_on_string_with_one_comma():
    test_argument = "2,081"
    expected = 2081
    actual = convert_to_int(test_argument)
    # Format the string with the actual return value
    message = "convert_to_int('2,081') should return the int 2081, but it actually returned {0}".format(actual)
    # Write the assert statement which prints message on failure
    assert (actual == expected), message
"""
Question
The test that you wrote was written to a test module called test_convert_to_int.py. Run the test in the IPython console and read the test result report.
- Which of the following is true?

@ The test passes.
@ The test fails because convert_to_int("2,081") returns the string "2081" and not the integer 2081.
@ The test fails because convert_to_int("2,081") returns None and not the integer 2081.
@ The test fails because of a SyntaxError in the test code.
Answer: 
The test fails because convert_to_int("2,081") returns None and not the integer 2081
"""

"""
### Testing float return values
-Complete the assert statement to check if get_data_as_numpy_array() returns expected, when called on example_clean_data_file.txt with num_columns set to 2.
"""
import numpy as np
import pytest
from as_numpy import get_data_as_numpy_array

def test_on_clean_file():
  expected = np.array([[2081.0, 314942.0],
                       [1059.0, 186606.0],
  					           [1148.0, 206186.0]
                       ]
                      )
  actual = get_data_as_numpy_array("example_clean_data.txt", num_columns=2)
  message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
  # Complete the assert statement
  assert actual == pytest.approx(expected), message

"""
### Testing with multiple assert statements
Instructions 1/4
- Calculate the expected number of rows of the training array using the formula int(0.75*n), where n is the number of rows in example_argument,
  and assign the variable expected_training_array_num_rows to this number.
- Calculate the expected number of rows of the testing array using the formula n - int(0.75*n), where n is the number of rows in example_argument,
  and assign the variable expected_testing_array_num_rows to this number.
- Write an assert statement that checks if training array has expected_training_array_num_rows rows.
- Write an assert statement that checks if testing array has expected_testing_array_num_rows rows.
"""
def test_on_six_rows():
    example_argument = np.array([[2081.0, 314942.0], [1059.0, 186606.0],
                                 [1148.0, 206186.0], [1506.0, 248419.0],
                                 [1210.0, 214114.0], [1697.0, 277794.0]]
                                )
    # Fill in with training array's expected number of rows
    expected_training_array_num_rows = 4
    # Fill in with testing array's expected number of rows
    expected_testing_array_num_rows = 2
    actual = split_into_training_and_testing_sets(example_argument)
    # Write the assert statement checking training array's number of rows
    assert actual[0].shape[0] == expected_training_array_num_rows, "The actual number of rows in the training array is not {}".format(expected_training_array_num_rows)
    # Write the assert statement checking testing array's number of rows
    assert actual[1].shape[1] == expected_testing_array_num_rows, "The actual number of rows in the testing array is not {}".format(expected_testing_array_num_rows)

"""
*** Testing for exceptions instead of return values

   *** with statement : is like a security guard
        - with    - .match  - as
   
       eg:    
             def test_Value_error_1d_array():
                  example_arg = np.array([22, 33, 44, 55, 55, 1])
                  with pytest.raises(ValueError) as exception_info: #store excepti0on
                        split_into_2d_array(example_arg)
                  # Check if ValueError contains message
                  assert exception_info.match("Argument data Array must be two dimentional."
                                              "Got 1D array instead!.")
"""

"""
### Practice the context manager
Instructions 1/4
- Complete the with statement by filling in with a context manager that will silence the ValueError raised in the context.
"""
import pytest

# Fill in with a context manager that will silence the ValueError
with pytest.raises(ValueError):
    raise ValueError
""" 
Instructions 2/4
- Complete the with statement with a context manager that raises Failed if no OSError is raised in the context.
"""
import pytest

try:
    # Fill in with a context manager that raises Failed if no OSError is raised
    with pytest.raises(OSError):
        raise ValueError
except:
    print("pytest raised an exception because no OSError was raised in the context.")
""" 
Instructions 3/4
- Extend the with statement so that any raised ValueError is stored in the variable exc_info.
"""
import pytest

# Store the raised ValueError in the variable exc_info
with pytest.raises(ValueError) as exc_info:
    raise ValueError("Silence me!")
"""
 Instructions 4/4
- Write an assert statement to check if the raised ValueError contains the message "Silence me!".
"""
import pytest

with pytest.raises(ValueError) as exc_info:
    raise ValueError("Silence me!")
# Check if the raised ValueError contains the correct message
assert exc_info.match("Silence me!"")

"""
### Unit test a ValueError
1/4
-Fill in with the correct context manager that checks if split_into_training_and_testing_sets() raises a ValueError when called 
  on test_argument, which is a NumPy array with a single row
"""
import numpy as np
import pytest
from train import split_into_training_and_testing_sets

def test_on_one_row():
    test_argument = np.array([[1382.0, 390167.0]])
    # Fill in with a context manager for checking ValueError
    with pytest.raises(ValueError):
      split_into_training_and_testing_sets(test_argument)
"""
2/4
Complete the with statement so that information about any raised ValueError will be stored in the variable exc_info.
"""
import numpy as np
import pytest
from train import split_into_training_and_testing_sets

def test_on_one_row():
    test_argument = np.array([[1382.0, 390167.0]])
    # Store information about raised ValueError in exc_info
    with pytest.raises(ValueError) as exc_info:
      split_into_training_and_testing_sets(test_argument)
"""
3/3
Write an assert statement to check if the raised ValueError contains the correct message stored in the variable expected_error_msg.
"""
import numpy as np
import pytest
from train import split_into_training_and_testing_sets

def test_on_one_row():
    test_argument = np.array([[1382.0, 390167.0]])
    # Store information about raised ValueError in exc_info
    with pytest.raises(ValueError) as exc_info:
      split_into_training_and_testing_sets(test_argument)
    expected_error_msg = "Argument data_array must have at least 2 rows, it actually has just 1"
    # Check if the raised ValueError contains the correct message
    assert exc_info.match("Argument data_array must have at least 2 rows, it actually has just 1")
"""
4/4
The test test_on_one_row() was written to the test module test_split_into_training_and_testing_sets.py. 
- Run the test in the IPython console and read the test result report. Does the test pass or fail?
"""
In [1]:!pytest test_split_into_training_and_testing_sets.py
# The test passes.

"""
*** The well tested function
    Pick a few of each category to save time in tests...
    
    @ bad arguments : creating intentional ValueErrors; like not splitting in 2d arrays
    @ special arguments:
                        @ Boundary values: minus limits it can have. like no less than 2 rows
                        @ Argument Values
    @ normal arguments: if do what needs to be done
"""

"""
### Testing well: Boundary values
"""
# (0, 0), (2, 0) and (1, 1).
"""
2/4
-Assign actual to the return value of row_to_list() on the argument "123\n", which is an instance of the boundary value (0, 0).
"""
import pytest
from preprocessing_helpers import row_to_list

def test_on_no_tab_no_missing_value():    # (0, 0) boundary value
    # Assign actual to the return value for the argument "123\n"
    actual = row_to_list("123\n")
    assert actual is None, "Expected: None, Actual: {0}".format(actual)
"""
3/4
- Complete the assert statement to check if row_to_list() indeed returns None for the instance "123\t4,567\t89\n" of the boundary value (2, 0).
"""
import pytest
from preprocessing_helpers import row_to_list

def test_on_no_tab_no_missing_value():    # (0, 0) boundary value
    # Assign actual to the return value for the argument "123\n"
    actual = row_to_list("123\n")
    assert actual is None, "Expected: None, Actual: {0}".format(actual)
    
def test_on_two_tabs_no_missing_value():    # (2, 0) boundary value
    actual = row_to_list("123\t4,567\t89\n")
    # Complete the assert statement
    assert actual is None, "Expected: None, Actual: {0}".format(actual)
"""
4/4
- In the test test_on_one_tab_with_missing_value(), format the failure message with the actual return value.
"""
import pytest
from preprocessing_helpers import row_to_list

def test_on_no_tab_no_missing_value():    # (0, 0) boundary value
    # Assign actual to the return value for the argument "123\n"
    actual = row_to_list("123\n")
    assert actual is None, "Expected: None, Actual: {0}".format(actual)
    
def test_on_two_tabs_no_missing_value():    # (2, 0) boundary value
    actual = row_to_list("123\t4,567\t89\n")
    # Complete the assert statement
    assert actual is None, "Expected: None, Actual: {0}".format(actual)
    
def test_on_one_tab_with_missing_value():    # (1, 1) boundary value
    actual = row_to_list("\t4,567\n")
    # Format the failure message
    assert actual is None, "Expected: None, Actual: {0}".format(actual)                      
