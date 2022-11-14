"""

\  Fit the model(s)  /

You're finally ready to fit the models and select the best one!

Unfortunately, cross validation is a very computationally intensive procedure. Fitting all the models would take too long on DataCamp.

To do this locally you would use the code:

        # Fit cross validation models
        models = cv.fit(training)

        # Extract the best model
        best_lr = models.bestModel
        Remember, the training data is called training and you're using lr to fit a logistic regression model. Cross validation selected the parameter values regParam=0 and elasticNetParam=0 as being the best. These are the default values, so you don't need to do anything else with lr before fitting the model.

Instructions
100 XP

- Create best_lr by calling lr.fit() on the training data.
- Print best_lr to verify that it's an object of the LogisticRegressionModel class.

"""
# Call lr.fit()
best_lr = lr.fit(training)

# Print best_lr
print(best_lr)
