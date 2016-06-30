#!/usr/bin/env python
import numpy as np
from sklearn.ensemble import RandomForestClassifier
f = open("data/train.csv", "r")
data = np.loadtxt(f, delimiter=',', skiprows=1)
f.close()
X = data[:, 1:]
y = data[:, 0]
print "load train x y finish"

rf = RandomForestClassifier(max_depth=8, n_estimators=10)
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
