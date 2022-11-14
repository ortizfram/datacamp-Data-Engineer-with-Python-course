"""
\  make a grid  /

- Import the submodule pyspark.ml.tuning under the alias tune.
- Call the class constructor ParamGridBuilder() with no arguments. Save this as grid.
- Call the .addGrid() method on grid with lr.regParam as the first argument and np.arange(0, .1, .01) as the second argument. This second call is a function from the numpy module (imported as np) that creates a list of numbers from 0 to .1, incrementing by .01. Overwrite grid with the result.
- Update grid again by calling the .addGrid() method a second time create a grid for lr.elasticNetParam that includes only the values [0, 1].
- Call the .build() method on grid and overwrite it with the output.
"""

# Import the tuning submodule
import pyspark.ml.tuning as tune

# Create the parameter grid
grid = tune.ParamGridBuilder()

# Add the hyperparameter
grid = grid.addGrid(lr.regParam, np.arange(0, .1, .01))
grid = grid.addGrid(lr.elasticNetParam,[0,1])

# Build the grid
grid = grid.build()
