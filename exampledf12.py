import pandas as pd
import numpy as np
import matplotlib.pyplot as p
data=pd.read_csv("C:/Users/SPTIT-22/Desktop/tested.csv")
print(data)
a=data.head(10)
print(a)
b=p.hist(data['Age'])
print(b)
a=(data['Sex']).value_counts().plot(kind='bar')
print(a)
a=p.scatter(data['Age'],data['Fare'])
print(a)
a=data[data['Pclass']==3]
d=a[a['Sex']=='female']
d['Survived'].value_counts().plot(kind='bar')
print(d['Survived'].value_counts())
import seaborn as sns
a=sns.boxplot(data['Survived'])
print(a)

