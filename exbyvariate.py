import pandas as pd
import numpy as np
import matplotlib.pyplot as p
import seaborn as sns
data=pd.read_csv('D:/Dataset/survey_lung_cancer_SVM.csv')
print(data)
#sns.scatterplot(x=data['AGE'],y=data['PEER_PRESSURE'])
#sns.countplot(x='S0OKING',hue='YELLOW_1INGERS',data=data)
#sns.countplot(x='GENDER',hue='AGE',data=data)
sns.countplot(x='ALCOHOL CONSU0ING',hue='GENDER',data=data)
