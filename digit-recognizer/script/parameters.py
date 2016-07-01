#!/usr/bin/env python
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from operator import itemgetter
from sklearn.grid_search import GridSearchCV, RandomizedSearchCV
from time import time
from scipy.stats import randint as sp_randint

f = open("data/train.csv", "r")
data = np.loadtxt(f, delimiter=',', skiprows=1)
f.close()
X = data[:, 1:]
y = data[:, 0]
print "load train x y finish"

clf = RandomForestClassifier()
# Utility function to report best scores
def report(grid_scores, n_top=10):
	top_scores = sorted(grid_scores, key=itemgetter(1), reverse=True)[:n_top]
	for i, score in enumerate(top_scores):
		print("Model with rank: {0}".format(i + 1))
		print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
			score.mean_validation_score,
			np.std(score.cv_validation_scores)))
		print("Parameters: {0}".format(score.parameters))
		print("")


# use a full grid over all parameters
param_grid = {"max_depth": [64, 128, 256, 512],
				"n_estimators": [128, 256],
				"bootstrap": [False],
				"criterion": ["gini", "entropy"]}

# run grid search
print "start grid search"
grid_search = GridSearchCV(clf, param_grid=param_grid, cv=10, verbose=100, n_jobs=8)
start = time()
grid_search.fit(X, y)

print("GridSearchCV took %.2f seconds for %d candidate parameter settings."
		% (time() - start, len(grid_search.grid_scores_)))
report(grid_search.grid_scores_)

