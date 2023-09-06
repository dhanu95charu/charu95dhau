import numpy as np
import pandas as pd
import matplotlib.pyplot as p
data=pd.read_csv("D:/Dataset/mtcars2.csv")
print(data)
#p.hist(x=data['mpg'])
#p.scatter(x='wt',y='mpg',data=data)
#data['transmission'].value_counts().plot(kind='bar')
import seaborn as sns
sns.boxplot(data['mpg'])
a=data['mpg'].max()
print(a)
print(data['cyl']==6,data['cars'].value_counts())
print(data['cars'],data['model-year'].value_counts())
