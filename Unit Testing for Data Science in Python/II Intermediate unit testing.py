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

"""
### Testing well: Values triggering special logic
Instructions
- Assign the variable actual to the actual return value for "\n".
- Complete the assert statement for test_on_no_tab_with_missing_value(), making sure to format the failure message appropriately.
- Assign the variable actual to the actual return value for "123\t\t89\n".
- Complete the assert statement for test_on_two_tabs_with_missing_value(), making sure to format the failure message appropriately.
"""
import pytest
from preprocessing_helpers import row_to_list

def test_on_no_tab_with_missing_value():    # (0, 1) case
    # Assign to the actual return value for the argument "\n"
    actual = row_to_list("\n")
    # Write the assert statement with a failure message
    assert actual is None, "Expected: None, Actual: {0}".format(actual)
    
def test_on_two_tabs_with_missing_value():    # (2, 1) case
    # Assign to the actual return value for the argument "123\t\t89\n"
    actual = row_to_list("123\t\t89\n")
    # Write the assert statement with a failure message
    assert actual is None, "Expected: None, Actual: {0}".format(actual)
                      
"""
### Testing well: Normal arguments
- How many normal arguments is it recommended to test?
Answer 1: At least two or three.
"""
""" 2/4
- Assign the variable expected to the expected return value for the normal argument "123\t4,567\n".
"""
import pytest
from preprocessing_helpers import row_to_list

def test_on_normal_argument_1():
    actual = row_to_list("123\t4,567\n")
    # Fill in with the expected return value for the argument "123\t4,567\n"
    expected = row_to_list("123\t4,567\n")
    assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)
""" 3/4
- Complete the correct assert statement for test_on_normal_argument_2(), making sure to format the failure message appropriately.
"""
import pytest
from preprocessing_helpers import row_to_list

def test_on_normal_argument_1():
    actual = row_to_list("123\t4,567\n")
    # Fill in with the expected return value for the argument "123\t4,567\n"
    expected = ["123", "4,567"]
    assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)
    
def test_on_normal_argument_2():
    actual = row_to_list("1,059\t186,606\n")
    expected = ["1,059", "186,606"]
    # Write the assert statement along with a failure message
    assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)
""" 4/4
The tests for boundary values, values triggering special behavior and normal arguments have been written to a test module test_row_to_list.py.
-Run the tests in the IPython shell. Which bugs does the function have?
Answer : The function does not have any bugs.
"""
                      
"""
*** TDD (test driven development)
   *** Unit tests BEFORE IMPLEMENTATION
        - Can't be deprioritized
        - Requierements clearer, implementation easier
"""
                      
"""
### TDD: Tests for normal arguments
Instructions
- Complete the assert statement for test_with_no_comma() by inserting the correct boolean expression.
- Complete the assert statement for test_with_one_comma() by inserting the correct boolean expression.
- Complete the assert statement for test_with_two_commas() by inserting the correct boolean expression.
"""
def test_with_no_comma():
    actual = convert_to_int("756")
    # Complete the assert statement
    assert actual == 756, "Expected: 756, Actual: {0}".format(actual)
    
def test_with_one_comma():
    actual = convert_to_int("2,081")
    # Complete the assert statement
    assert actual == 2081, "Expected: 2081, Actual: {0}".format(actual)
    
def test_with_two_commas():
    actual = convert_to_int("1,034,891")
    # Complete the assert statement
    assert actual == 1034891, "Expected: 1034891, Actual: {0}".format(actual)
                      
"""
### TDD: Requirement collection
Instructions 1/2
- Give a name to the test by using the standard name prefix that pytest expects followed by on_string_with_missing_comma.
- Assign actual to the actual return value for the argument "12,72,891".
- Complete the assert statement.
"""
# Give a name to the test for an argument with missing comma
def test_on_string_with_missing_comma():
    actual = convert_to_int("178100,301")
    assert actual is None, "Expected: None, Actual: {0}".format(actual)
    
def test_on_string_with_incorrectly_placed_comma():
    # Assign to the actual return value for the argument "12,72,891"
    actual = convert_to_int("12,72,891") 
    assert actual is None, "Expected: None, Actual: {0}".format(actual)
    
def test_on_float_valued_string():
    actual = convert_to_int("23,816.92")
    # Complete the assert statement
    assert actual is None, "Expected: None, Actual: {0}".format(actual)
"""
2/2
-Run it in the IPython console and read the test result report. What happens?
@ All tests are passing.
@ The test test_on_string_with_two_commas() is failing because the convert_to_int("1,034,891") returns None instead of the correct integer 1034891.
@ All tests are failing with a NameError since convert_to_int() has not been implemented yet.
"""
In [1]: !pytest test_convert_to_int.py
# All tests are failing with a NameError since convert_to_int() has not been implemented yet
                      
"""
### TDD: Implement the function
Instructions 1/4
- Complete the if statement that checks if the i-th element of comma_separated_parts has length greater than 3.
"""
def convert_to_int(integer_string_with_commas):
    comma_separated_parts = integer_string_with_commas.split(",")
    for i in range(len(comma_separated_parts)):
        # Write an if statement for checking missing commas
        if len(comma_separated_parts[i]) > 3:
            return None
"""
2/4
-Complete the if statement that checks if any entry other than the 0-th entry of comma_separated_parts has a length not equal to 3.
"""
def convert_to_int(integer_string_with_commas):
    comma_separated_parts = integer_string_with_commas.split(",")
    for i in range(len(comma_separated_parts)):
        # Write an if statement for checking missing commas
        if len(comma_separated_parts[i]) > 3:
            return None
        # Write the if statement for incorrectly placed commas
        if i != 0 and len(comma_separated_parts[i]) != 3:
            return None
"""
3/4
- Fill in the except clause with a ValueError, which is raised when trying to convert float valued strings e.g. 23816.92 to an integer.
"""
def convert_to_int(integer_string_with_commas):
    comma_separated_parts = integer_string_with_commas.split(",")
    for i in range(len(comma_separated_parts)):
        # Write an if statement for checking missing commas
        if len(comma_separated_parts[i]) > 3:
            return None
        # Write the if statement for incorrectly placed commas
        if i != 0 and len(comma_separated_parts[i]) != 3:
            return None
    integer_string_without_commas = "".join(comma_separated_parts)
    try:
        return int(integer_string_without_commas)
    # Fill in with a ValueError, when trying to convert float valued string
    except ValueError:
        return None
"""
4/4
- Run it the IPython console and read the test result report. Did you implement the function correctly, or are there any bugs?
"""
In [1]: !pytest test_convert_to_int.py
# All tests are passing and the implementation does not have a bug.
