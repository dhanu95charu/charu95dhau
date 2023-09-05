import pandas as pd
import numpy as np
import matplotlib.pyplot as p
import seaborn as sns
data=pd.read_csv("C:/Users/SPTIT-22/Desktop/tested.csv")
print(data)
sns.scatterplot(x=data['Age'],y=data['Fare'])
sns.countplot(x='Pclass',hue='Survived',data=data)
sns.countplot(x='Sex',hue='Survived',data=data)
sns.countplot(x='Pclass',hue='Sex',data=data)
