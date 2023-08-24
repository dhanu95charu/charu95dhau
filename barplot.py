import pandas as pd
import numpy as np
import matplotlib.pyplot as p
data=pd.read_csv("C:/Users/SPTIT-22/Desktop/tested.csv")
print(data)
a=p.bar(data['PassengerId'],data['Age'])
print(a)
d=data['PassengerId'].max()
print(d)
e=data['PassengerId'].min()
print(e)

p.xlabel('PassengerId')
p.ylabel('Age')
p.title('bar plot')
