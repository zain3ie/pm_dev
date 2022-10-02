import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV

from src import params


def modelling(x, y):
    # Number of trees in random forest
    n_estimators = [int(x) for x in np.linspace(10, 80, 10)]
    # Number of features to consider at every split
    max_features = ['auto', 'sqrt']
    # Maximum number of levels in tree
    max_depth = [2, 4]
    # Minimum number of samples required to split a node
    min_samples_split = [2, 5]
    # Minimum number of samples required at each leaf node
    min_samples_leaf = [1, 2]
    # Method of selecting samples for training each tree
    bootstrap = [True, False]

    # Create the param grid
    param_grid = {'n_estimators': n_estimators,
                'max_features': max_features,
                'max_depth': max_depth,
                'min_samples_split': min_samples_split,
                'min_samples_leaf': min_samples_leaf,
                'bootstrap': bootstrap}

    rf_Model = RandomForestClassifier()

    rf_RandomGrid = RandomizedSearchCV(estimator=rf_Model, param_distributions=param_grid,
                                       scoring='f1_micro', cv=10, verbose=2, n_jobs=4)

    rf_RandomGrid.fit(x, y)

    # Dump model
    joblib.dump(rf_RandomGrid, f'./{params.model}')
