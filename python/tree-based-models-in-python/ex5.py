"""
Set the tree's hyperparameter grid
In this exercise, you'll manually set the grid of hyperparameters
that will be used to tune the classification tree dt and find the optimal classifier in the next exercise.
"""


# Define params_dt
params_dt = {'max_depth' : [2, 3, 4], 'min_samples_leaf' : [0.12, 0.14, 0.16, 0.18]}


"""
Search for the optimal tree
In this exercise, you'll perform grid search using 5-fold cross validation 
to find dt's optimal hyperparameters. Note that because grid search is an exhaustive process, 
it may take a lot time to train the model. Here you'll only be instantiating the GridSearchCV 
object without fitting it to the training set. As discussed in the video, you can train such an
object similar to any scikit-learn estimator by using the .fit() method:
grid_object.fit(X_train, y_train)
An untuned classification tree dt as well as the dictionary params_dt that you defined in the previous exercise are available in your workspace.
"""


from sklearn.model_selection import GridSearchCV

# Instantiate grid_dt
grid_dt = GridSearchCV(estimator= dt,
                       param_grid= params_dt,
                       scoring='roc_auc',
                       cv= 5,
                       n_jobs=-1)



"""
Evaluate the optimal tree
In this exercise, you'll evaluate the test 
set ROC AUC score of grid_dt's optimal model.

The dataset is already loaded and processed 
for you (numerical features are standardized); 
it is split into 80% train and 20% test. X_test,
y_test are available in your workspace. In addition, 
we have also loaded the trained GridSearchCV object grid_dt 
that you instantiated in the previous exercise. Note that grid_dt was trained as follows:

grid_dt.fit(X_train, y_train)
"""


# Import roc_auc_score from sklearn.metrics
from sklearn.metrics import roc_auc_score

# Extract the best estimator
best_model = grid_dt.best_estimator_

# Predict the test set probabilities of the positive class
y_pred_proba = best_model.predict_proba(X_test)[:,1]

# Compute test_roc_auc
test_roc_auc = roc_auc_score(y_test, y_pred_proba)

# Print test_roc_auc
print('Test set ROC AUC score: {:.3f}'.format(test_roc_auc))


