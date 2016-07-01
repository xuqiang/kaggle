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

rf = RandomForestClassifier(max_depth=64, n_estimators=128, bootstrap=False, criterion='gini')
model = rf.fit(X, y)
print "train rf finish"

#predict test data
f = open("./data/test.csv", "r")
test_X = np.loadtxt(f, delimiter=',', skiprows=1)
f.close()
preds = model.predict(test_X)
fout = open("mysubmission.csv", "w")
fout.write("ImageId,Label\n")
idx = 1
for pred in preds:
	fout.write( "{},{}\n".format(idx, int(pred)) )
	idx += 1
fout.close()
