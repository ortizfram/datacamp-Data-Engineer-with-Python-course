"""
\  Cross validation  /

  estimates model's error on held out data

    -> k-fold  :  method of estimating the model's performance on unseen data
    
                  - split data in few partitions (3)
                  - partitions is set aside, and the model is fit to the others
                  - error is measured against the held out partition
                  - This is repeated for each of the partitions
                  - Then the error is averaged."""
#|
#|
### 
""" What does cross validation allow you to estimate?"""
# ANSW: The model's error on held out data.
#|
#|
### Create the evaluator
# Import the evaluation submodule
import pyspark.ml.evaluation as evals

# Create a BinaryClassificationEvaluator
evaluator = evals.BinaryClassificationEvaluator(metricName="areaUnderROC")
