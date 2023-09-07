import pandas as pd
import numpy as np
import matplotlib.pyplot as p
import seaborn as sns
dfage=pd.read_csv('D:/Dataset/survey_lung_cancer_SVM.csv')
print(dfage)
dfage['AGE'].hist()
b=sns.set(style='darkgrid')
print(b)
a=sns.countplot(x='GENDER',data=dfage)
print(a)

