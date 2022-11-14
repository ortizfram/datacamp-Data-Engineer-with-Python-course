"""
\  Evaluate the model  /
Remember the test data that you set aside waaaaaay back in chapter 3? It's finally time to test your model on it! You can use the same evaluator you made to fit the
model.

Instructions
100 XP
- Use your model to generate predictions by applying best_lr.transform() to the test data. Save this as test_results.
- Call evaluator.evaluate() on test_results to compute the AUC. Print the output.

"""
# Use the model to predict the test set
test_results = best_lr.transform(test)

# Evaluate the predictions
print(evaluator.evaluate(test_results))

# 0.7
