import numpy as np
import pandas as pd

num=np.array([10,20,30])
s=pd.Series(num)
print(s)

b=np.array([10,20,30])
i=pd.Index(b)
print(i.value_counts())

ser1=pd.Series([10,1,3,6])
ser2=pd.Series([10,2,3,6])
print(ser1,ser2)
union=pd.Series(np.union1d(ser1,ser2))
intersect=pd.Series(np.intersect1d(ser1,ser2))
notcommon=union[union.isin(intersect)]
print(union)
print(intersect)
print(notcommon)
