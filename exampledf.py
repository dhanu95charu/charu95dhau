import pandas as pd
import numpy as np
import matplotlib.pyplot as p
data=pd.read_csv("C:/Users/SPTIT-22/Downloads/athlete_events (2).csv")                                             
print(data)
a=p.scatter(data['Height'],data['Weight'])
print(a)
s=p.hist(data['Age'])
print(s)
c=p.bar(data['Year']==2000)
print(c)
d=p.bar(data['Sex']=='M')
print(d)
