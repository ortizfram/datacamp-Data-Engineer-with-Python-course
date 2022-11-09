"""
advanced unit testing skills like setup, teardown and mocking. You will also learn how to write sanity tests for your data science models and how 
to test matplotlib plots. By the end of this chapter, you will be ready to test real world data science projects!
"""
"""
\*** Beyond assertion: setup and teardown
      
      -> setup : prepare environment so testing can begin
                eg:|
                    def test_on_raw_data():
                        # Setup : create raw data file
                        # call funciton
                        preprocess(raw_data_fpath, clean_data_fpath)
                        with open(clean_data_fpath) as f:
                            lines = f.readlines()
                        first_line = lines[0]
                        assert first_line == "1081\t201411\n"
                        second_line = lines[1]
                        assert second_line == "2002\t333209\n"
                        # Teardown: remove raw, adn clean data file
                        ## bring environment to initial state
                
          --> new workflow : -setup -assert -teardown
          
    \ fixture /
        ## (function) where setup and teardown are placed; outside the test
        >>>>>> @pytest.fixture
              eg:|
                  import os
                  
                  @pytest.fixture
                  def my_fixture(tmpdir):
                      # Do Setup here
                      file_path="xxx"
                      yield data
                      # Do Teardown here  (happends when has finished executing)
                      # remove in teardown
                      # Use the appropriate method to create an empty file in the temporary directory
                      file_path = tmpdir.join("empty.txt")
                      
                      os.remove(file_path)
"""
#|
#|
### Use a fixture for a clean data file
"""Instructions
-Add the correct decorator that would turn clean_data_file() into a fixture.
-Pass an argument to the test test_on_clean_file() so that it uses the fixture.
-Pass the clean data file path yielded by the fixture as the first argument to the function get_data_as_numpy_array()."""
# Add a decorator to make this function a fixture
@pytest.fixture
def clean_data_file():
    file_path = "clean_data_file.txt"
    with open(file_path, "w") as f:
        f.write("201\t305671\n7892\t298140\n501\t738293\n")
    yield file_path
    os.remove(file_path)
    
# Pass the correct argument so that the test can use the fixture
def test_on_clean_file(clean_data_file):
    expected = np.array([[201.0, 305671.0], [7892.0, 298140.0], [501.0, 738293.0]])
    # Pass the clean data file path yielded by the fixture as the first argument
    actual = get_data_as_numpy_array(clean_data_file, 2)
    assert actual == pytest.approx(expected), "Expected: {0}, Actual: {1}".format(expected, actual) 
#|
#|
### Write a fixture for an empty data file
"""Instructions 1/2
-In the setup, assign the variable file_path to the correct string.
-After the setup, yield the variable file_path so that the test can use it.
-In the teardown, remove the file."""
import os
@pytest.fixture
def empty_file():
    # Assign the file path "empty.txt" to the variable
    file_path = "empty.txt"
    open(file_path, "w").close()
    # Yield the variable file_path
    yield file_path
    # Remove the file in the teardown
    os.remove(file_path)
    
def test_on_empty_file(self, empty_file):
    expected = np.empty((0, 2))
    actual = get_data_as_numpy_array(empty_file, 2)
    assert actual == pytest.approx(expected), "Expected: {0}, Actual: {1}".format(expected, actual)
#|
"""Instructions 2/2
Question
- run the test test_on_empty_file(). What is the outcome?"""
!pytest -k "TestGetDataAsNumpyArray"
# Answ: The test passes.
#|
#|
### Fixture chaining using tmpdir
""" instructions 1/2
-Add the correct argument to the fixture empty_file() so that it chains with the built-in fixture tmpdir.
-Use the appropriate method to create an empty file "empty.txt" inside the temporary directory created by tmpdir.
"""
import pytest

@pytest.fixture
# Add the correct argument so that this fixture can chain with the tmpdir fixture
def empty_file(tmpdir):
    # Use the appropriate method to create an empty file in the temporary directory
    file_path = tmpdir.join("empty.txt")
    open(file_path, "w").close()
    yield file_path
#|
"""Instructions 2/2
Question
-In what order will the setup and teardown of empty_file() and tmpdir be executed?"""
# Answ: setup of tmpdir -> setup of empty_file() -> teardown of empty_file() -> teardown of tmpdir.
#|
#|
"""
  \ Mocking /
     |      #-> replace bugged files w/ MagicMock() file only in testing
     L> test a function independently from dependencies
      (-1 install packages:  
            - pip install pytest-mock
            - pip install unittest.mock
      (-2 (inside test function) 
            - add mocker -as argument
            - add var _mock asigning mocker.path("<dependency with module name>")
            - add side_effect
"""
#|
#|
### Program a bug-free dependency
"""Instructions
-Define a function convert_to_int_bug_free() which takes one argument called comma_separated_integer_string.
-Assign return_values to the dictionary holding the correct return values in the context of the raw data file used in the test.
-Return the correct return value by looking up the dictionary return_values for the key comma_separated_integer_string."""
# Define a function convert_to_int_bug_free
def convert_to_int_bug_free(comma_separated_integer_string):
    # Assign to the dictionary holding the correct return values 
    return_values = {"1,801": 1801, "201,411": 201411, "2,002": 2002, "333,209": 333209, "1990": None, "782,911": 782911, "1,285": 1285, "389129": None}
    # Return the correct result using the dictionary return_values
    return return_values[comma_separated_integer_string]
#|
#|
### Mock a dependency
"""Instructions 1/4
-In the test test_on_raw_data(), add the correct argument that enables the use of the mocking fixture."""
# Add the correct argument to use the mocking fixture in this test
def test_on_raw_data(self, raw_and_clean_data_file, mocker):
    raw_path, clean_path = raw_and_clean_data_file
"""Instructions 2/4
-Replace the dependency "data.preprocessing_helpers.convert_to_int" with the bug-free version convert_to_int_bug_free() by using the correct method and side effect"""
# Add the correct argument to use the mocking fixture in this test
def test_on_raw_data(self, raw_and_clean_data_file, mocker):
    raw_path, clean_path = raw_and_clean_data_file
    # Replace the dependency with the bug-free mock
    convert_to_int_mock = mocker.patch("data.preprocessing_helpers.convert_to_int",
                                    side_effect = convert_to_int_bug_free)
#|
"""Instructions 3/4
-Use the correct attribute which returns the list of calls to the mock, and check if the mock was called with this sequence of
arguments: "1,801", "201,411", "2,002", "333,209", "1990", "782,911", "1,285", "389129"."""
# Add the correct argument to use the mocking fixture in this test
def test_on_raw_data(self, raw_and_clean_data_file, mocker):
    raw_path, clean_path = raw_and_clean_data_file
    # Replace the dependency with the bug-free mock
    convert_to_int_mock = mocker.patch("data.preprocessing_helpers.convert_to_int",
                                       side_effect=convert_to_int_bug_free)
    preprocess(raw_path, clean_path)
    # Check if preprocess() called the dependency correctly
    assert convert_to_int_mock.call_args_list == [call("1,801"), call("201,411"), call("2,002"), call("333,209"), call("1990"), call("782,911"), call("1,285"), call("389129")]
    with open(clean_path, "r") as f:
        lines = f.readlines()
    first_line = lines[0]
    assert first_line == "1801\\t201411\\n"
    second_line = lines[1]
    assert second_line == "2002\\t333209\\n" 
#|
"""instructions 4/4
-Run the tests in TestPreprocess and TestConvertToInt. Based on the test result report, which of the following is correct? """
!pytest -k "TestPreprocess"
!pytest -k "TestConvertToInt"
# Answ: Some tests for convert_to_int() fail but the test for preprocess() pass
#|
#|
"""
\ testing models /

     > Testing on linear data
            >>>>>> from scipy.stats import linregress
            >>>>>> slope
            >>>>>> intercept
            
     > Testing model performance
       # indicates how well model performs on unseen data
       # 1= perfect fit , 0= there's no fit
       eg:|
             def model_test(testing_set, slope, intercept):
                  '''return r2 of fit'''
            
"""
#|
#|
### Testing on linear data
"""in this special case, model_test() should return 1.0 if the model's slope and intercept match the testing set, because 1.0 is usually the highest 
possible value that r2 can take.
=Instructions
-Assign the variable test_argument to a NumPy array holding the perfectly linear testing data printed out in the IPython console.
-Assign the variable expected to the expected value of  in the special case of a perfect fit.
-Fill in with the model's slope and intercept that matches the testing set.
-Remembering that actual is a float, complete the assert statement to check if actual returned by model_test() is equal to the expected return value expected."""
import numpy as np
import pytest
from models.train import model_test

def test_on_perfect_fit():
    # Assign to a NumPy array containing a linear testing set
    test_argument = np.array([[1.0,	3.0], [2.0,	5.0], [3.0,	7.0]])
    # Fill in with the expected value of r^2 in the case of perfect fit
    expected = 1.0 
    # Fill in with the slope and intercept of the model
    actual = model_test(test_argument, slope=2.0, intercept=1.0)
    # Complete the assert statement
    assert actual == pytest.approx(expected), "Expected: {0}, Actual: {1}".format(expected, actual)
#|
#|
### Testing on circular data
"""case where it is easy to guess the value of r2 is when the model does not fit the testing dataset at all. In this case,  takes its lowest possible value 0.0. """
"""Your job is to write a test test_on_circular_data() for the function model_test() that performs this sanity check."""
"""Instructions 1/4
-Assign test_argument to a 8X2 NumPy array holding the circular testing data shown in the plot, starting with (1.0, 0.0) and moving anticlockwise."""
def test_on_circular_data(self):
    theta = pi/4.0
    # Complete the NumPy array holding the circular testing data
    test_argument = np.array([[1.0, 0.0], [cos(theta), sin(theta)],
                              [0.0, 1.0],
                              [cos(3 * theta), sin(3 * theta)],
                              [-1.0, 0.0],
                              [cos(5 * theta), sin(5 * theta)],
                              [0.0, -1.0],
                              [cos(7 * theta), sin(7 * theta)]]
                             )
#|
"""Instructions 2/4
-Fill in with the slope and intercept of the straight line shown in the plot."""
def test_on_circular_data(self):
    theta = pi/4.0
    # Assign to a NumPy array holding the circular testing data
    test_argument = np.array([[1.0, 0.0], [cos(theta), sin(theta)],
                              [0.0, 1.0],
                              [cos(3 * theta), sin(3 * theta)],
                              [-1.0, 0.0],
                              [cos(5 * theta), sin(5 * theta)],
                              [0.0, -1.0],
                              [cos(7 * theta), sin(7 * theta)]]
                             )
    # Fill in with the slope and intercept of the straight line
    actual = model_test(test_argument, slope=0.0, intercept=0.0)
#|
"""Instructions 3/4
-Remembering that model_test() returns a float, complete the assert statement to check if model_test() returns the expected value of  in this special case."""
def test_on_circular_data(self):
    theta = pi/4.0
    # Assign to a NumPy array holding the circular testing data
    test_argument = np.array([[1.0, 0.0], [cos(theta), sin(theta)],
                              [0.0, 1.0],
                              [cos(3 * theta), sin(3 * theta)],
                              [-1.0, 0.0],
                              [cos(5 * theta), sin(5 * theta)],
                              [0.0, -1.0],
                              [cos(7 * theta), sin(7 * theta)]]
                             )
    # Fill in with the slope and intercept of the straight line
    actual = model_test(test_argument, slope=0.0, intercept=0.0)
    # Complete the assert statement
    assert actual == pytest.approx(0.0)
#|
"""Instructions 4/4
Question
-The tests test_on_perfect_fit() and test_on_circular_data() that you wrote in the last two exercises has been written to the test class
 TestModelTest in the test module models/test_train.py. Run the test class in the IPython console. What is the outcome?"""
!pytest -k "TestModelTest"
# Answ: The sanity checks are all passing.
#|
#|
"""
\ testing plots /
            
            # Using > matplotlib for visualizations
            
          -> plots.py : inside visualization/ inside src/
          
          -> testing strategy for plots
            - one-time baseline
                 > (pytest plugin) pytest-mpl 
                       # for image comparisons
                       # knows how to ignore OS related differences
                       # makes easy to generate baseline images
                         > pip install pytest-mpl
                                                  
            - testing
                 eg:|
                        import pytest
                        import numpy as np
                        from visualization import get_plot_for_best_fit
                        
                        @pytest.mark.mpl_image_compare  # baseline generation and comparison
                        def test_plot_for_linear_data():
                              slope= 2.0
                              intercept= 1.0
                              x_array= np.array([1.0, 2.0, 3.0]) # linear data set
                              y_array= np.array([3.0, 5.0, 7.0])
                              title= "Test plot for linear data"
                              return get_plot_for_best_fit_line(slope, intercept, x_array, y_array, title)
                      |_______
                      
                     > generate a baseline image
                        eg:| !pytest -k "test_plot_for_linear_data"
                                     --mpl-generate-path
                                     visualization/baseline
                     > run the test :
                        !pytest  -k "test_plot_for_linear_data" --mpl
                        ## if not identical , test will fail
"""
#|
#|
### Generate the baseline image
import pytest
import numpy as np

from visualization.plots import get_plot_for_best_fit_line

class TestGetPlotForBestFitLine(object):
    # Add the pytest marker which generates baselines and compares images
    @pytest.mark.mpl_image_compare
    def test_plot_for_almost_linear_data(self):
        slope = 5.0
        intercept = -2.0
        x_array = np.array([1.0, 2.0, 3.0])
        y_array = np.array([3.0, 8.0, 11.0])
        title = "Test plot for almost linear data"
        # Return the matplotlib figure returned by the function under test
        return get_plot_for_best_fit_line(slope, intercept, x_array, y_array, title)
-----
pytest --mpl-generate-path /home/repl/workspace/project/tests/visualization/baseline -k "test_plot_for_almost_linear_data"
#|
#|
### Run the tests for the plotting function
"""Instructions
-Run the tests in this test class in the console. Because it's a shell console and not an IPython one, you don't need to use the !
at the beginning of your command. You should see two failures."""
pytest -k "TestGetPlotForBestFitLine" --mpl
#|
#|
### Fix the plotting function
"""Instructions 1/2
Fill in the axis labels xlabel and ylabel so that they match the baseline plot (plot 1/2)."""
import matplotlib.pyplot as plt
import numpy as np

def get_plot_for_best_fit_line(slope, intercept, x_array, y_array, title):
    fig, ax = plt.subplots()
    ax.plot(x_array, y_array, ".")
    ax.plot([0, np.max(x_array)], [intercept, slope * np.max(x_array) + intercept], "-")
    # Fill in with axis labels so that they match the baseline
    ax.set(xlabel='area (square feet)', ylabel='price (dollars)', title=title)
    return fig
"""nstructions 2/2
Question
-Now that you have fixed the function, run all the tests in the tests directory, remembering that the current working directory in
 the IPython console is tests. What is the outcome?"""
!pytest
# Answ: All 25 tests pass.
