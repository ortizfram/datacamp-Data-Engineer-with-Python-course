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
                  @pytest.fixture
                  def my_fixture(tmpdir):
                      # Do Setup here
                      yield data
                      # Do Teardown here  (happends when has finished executing)
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
