"""
|||||
create a model that predicts which flights will be delayed.
|||||

\  Logistic regression model  /

    similar to a linear regression, but instead of predicting a numeric variable, 
   ->it 'predicts the probability (between 0 and 1) of an event.'
    
      - set 'cutoff' point
      - if prediction above cutoff == 'yes'
      - if it's below, you classify it as a 'no'!
      
      -> hyperparameter : just a value in the model that's is supplied by the user to maximize performance."""
#|
#|
""" Why do you supply hyperparameters?"""
# ANSW: They improve model performance.
#|
#|
### Create the modeler

# Import LogisticRegression # Estimator
from pyspark.ml.classification import LogisticRegression

# Create a LogisticRegression Estimator
lr = LogisticRegression()

