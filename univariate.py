import pandas as pd
import numpy as np
import matplotlib.pyplot as p
import seaborn as sns
age=[12,42,52,41,78,35,82,94,24,72,47]
gender=['male','female','others','male','female','others','male','female','others','male','female']
dfage=pd.DataFrame({'age':age,
                    'gender':gender})
print(dfage)
dfage['age'].hist()
b=sns.set(style='darkgrid')
print(b)
a=sns.countplot(x='gender',data=dfage)
print(a)

