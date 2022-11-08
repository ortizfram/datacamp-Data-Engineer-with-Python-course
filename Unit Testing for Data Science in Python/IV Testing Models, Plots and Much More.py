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
