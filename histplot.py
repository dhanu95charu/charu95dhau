
import pandas as pd
import numpy as np
import matplotlib.pyplot as p
data=pd.read_csv("C:/Users/SPTIT-22/Desktop/tested.csv")
print(data)
p.hist(data['Survived'])
data[data['Sex']=='female']['Survived'].value_counts().plot(kind='bar')
p.xlabel('PassengerId')
p.ylabel('Age')
p.title('histogram plot')
