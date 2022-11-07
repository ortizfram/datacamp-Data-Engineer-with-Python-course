"""
In this chapter, we will learn about how to structure your test suite well, how to effortlessly execute any subset of tests and how to mark problematic 
tests so that your test suite always stays green. The last lesson will even enable you to add the trust-inspiring build status and code coverage badges to 
your own project. Complete this chapter and become a unit testing wizard!
"""
"""
\*** How to organize a growing set of tests?
  _\project structure/_
  -------------------
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
