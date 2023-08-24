import pandas as pd
data=pd.read_csv("C:/Users/SPTIT-22/Desktop/tested.csv")
print(data)
stats=data.describe()
print(stats)
a=data['Pclass'].min()
print(a)
a=data['Pclass'].max()
print(a)
a=[data['Pclass']==1],['Survived']
print(a)
year=data.groupby('Pclass')['Survived'].value_counts()
print(year)
