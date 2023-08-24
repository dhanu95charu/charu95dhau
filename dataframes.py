import pandas as pd
import numpy as np

dict={'first-score':[10,20,np.nan,40,np.nan],
      'second number':[np.nan,20,30,40,np.nan],
      'third number':[10,20,np.nan,50,10]}
data=pd.DataFrame(dict)
print(data.dropna())
print(data.fillna(10))
print(data.isnull())
print(data.notnull())
print(data.fillna(method="bfill"))
print(data.dropna(how="all"))
print(data.fillna(method="pad"))
