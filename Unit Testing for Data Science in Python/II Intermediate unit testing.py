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
