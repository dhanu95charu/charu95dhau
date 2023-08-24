import pandas as pd
import numpy as np
import matplotlib.pyplot as p
data=pd.read_csv("C:/Users/SPTIT-22/Desktop/tested.csv")
print(data)
a=p.plot(data['PassengerId'])
print(a)
data[data['Cabin']=='NaN'].value_counts().plot(kind='bar')
p.xlabel('PassengerId')
p.ylabel('Age')
p.title('lone plot')
