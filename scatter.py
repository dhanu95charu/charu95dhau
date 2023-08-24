import pandas as pd
import numpy as np
import matplotlib.pyplot as p
data=pd.read_csv("C:/Users/SPTIT-22/Desktop/tested.csv")
print(data)
a=p.scatter(data['PassengerId'],data['Age'])
print(a)
p.xlabel('PassengerId')
p.ylabel('Age')
p.title('scatter plot')
