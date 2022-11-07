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
"""
