import pandas as pd
import numpy as np
import matplotlib.pyplot as p
data=pd.read_csv("C:/Users/SPTIT-22/Desktop/tested.csv")
print(data)
a=p.scatter(data['PassengerId'],data['Age'])
print(a)
data[data['Cabin']=='NaN'].value_counts().plot(kind='bar')
a=p.plot(data['PassengerId'])
print(a)
a=p.bar(data['PassengerId'],data['Age'])
print(a)
a=p.hist(data['PassengerId'])
print(a)
