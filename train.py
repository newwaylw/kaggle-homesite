#! /usr/bin/env python

import sys,re
import numpy as np
import pickle
from sklearn import svm

records = list()
label = list() 
with open(sys.argv[1]) as f:
  for line in f:
    sample = re.split('\s',line.strip())
    records.append(sample[:-1])
    label.append(sample[-1])
    #print("sample:", sample[:-1], "label=",sample[-1])
print(len(records), " samples read.")

X = np.asarray(records)
y = np.asarray(label)

clf = svm.SVC(probability=True)
clf.fit(X,y)

with open('model_svm.pickle', 'wb') as handle:
  pickle.dump(clf, handle)

