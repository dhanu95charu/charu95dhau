import pandas as pd
import numpy as np
import matplotlib.pyplot as p
data=pd.read_csv("C:/Users/SPTIT-22/Downloads/athlete_events (2).csv")                                             
print(data)
a=p.scatter(data['Height'],data['Weight'])
print(a)
s=p.hist(data['Age'])
print(s)
b=(data[data['Sex']=='M'],data['Medal'].value_counts().plot(kind='bar'))
print(b)

c=(data[data['Year']==2000],data['Name'].value_counts().plot(kind='bar'))
print(c)
