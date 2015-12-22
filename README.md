# kaggle-homesite
project for kaggle homesite

mappings.txt 枚举了所有非numeric的特征与其位置。

normalize_train.py 做了几件事情：
* 忽略第一个特征"QuoteNumber"
* 特征 Original_Quote_Date 转换为 "week of the year" [1-52]
* "QuoteConversion_Flag" 变为最后一个feature
* 将所有非numeric特征按位置映射为[0,1]的一组特征。
  比如一个例子的特征是 'XY', 而所有例子有这个特征一共有"XX,XY,XZ"
  那么这个特征将被变换为 "0 1 0" (XY为1)，以此类推

用法:
    
    normailize_train.py mappings.txt train.csv
    
test.csv 同样用normailize_test.py处理 （test.csv没有 "QuoteConversion_Flag")
