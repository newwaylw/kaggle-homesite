#! /usr/bin/env python3

import sys,re,csv
from datetime import datetime

def isnumeric(str1):
  try:
    float(str1)
    return True
  except ValueError:
    return False

m = dict()
record = list()
y = list()

#read mappings
with open(sys.argv[1]) as f:
  for line in f:
    cols = re.split('\s+', line.strip())
    m[int(cols[0])] = cols[1:]
'''
l = sorted(m)
for i in l:
  print (i, m[i])
'''
with open(sys.argv[2]) as f:
  header = f.readline()
  r = csv.reader(f,delimiter=',' ,skipinitialspace=True)
  for row in r:
    arow=list()
    weekofyear = datetime.strptime(row[1], '%Y-%m-%d').date().isocalendar()[1]
    row[1] = weekofyear
    row[7] = re.sub(',','',row[7])

    arow.extend(row[1:2])
    arow.extend(row[3:])
    record.append(arow)
    y.append(row[2])

absent_value = -1
no =0
for row in record:
  idx = 0
  norm_feature = list()
  for col in row:
    if idx in m:
      l = sorted(m[idx])
      for item in l:
        if col == item:
          norm_feature.append(1)
        else:
          norm_feature.append(0)

    elif len(str(col)) == 0 :
      norm_feature.append(absent_value)
    else:
      norm_feature.append(float(col))
    idx+=1
  print(' '.join(str(v) for v in norm_feature), y[no])
  no+=1


