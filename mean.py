import pandas as pd
import numpy as np
import matplotlib.pyplot as p
data=pd.read_csv("C:/Users/SPTIT-22/Desktop/tested.csv")
print(data)

d=(data[data['PassengerId'].mean()]).value_counts().plot(kind='bar')
print(d)
d=(data[data['Age'].median()]).value_counts().plot(kind='bar')
print(d)
d=(data[data['Pclass'].mode()]).value_counts().plot(kind='bar')
print(d)
