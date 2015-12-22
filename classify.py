#! /usr/bin/env python

import sys,re
import numpy as np
import pickle
from sklearn import svm

records = list()
label = list() 
with open(sys.argv[1], 'rb') as s:
  clf = pickle.load(s)

with open(sys.argv[2]) as f:
  for line in f:
    sample = re.split('\s',line.strip())
    records.append(sample[:-1])
    label.append(sample[-1])

X = np.asarray(records)
y = np.asarray(label)

#clf.fit(X,y)
print(clf.predict(X))
print(y)
