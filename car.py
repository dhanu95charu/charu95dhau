import pandas as pd
data=pd.read_csv("C:/Users/SPTIT-22/Desktop/tested.csv")
print(data)
a=data[data['Pclass']==1]['Survived'].sum()
print(a)
b=(data[data['Pclass']==2]['Survived']>2).value_counts()
print(b)
