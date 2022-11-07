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
