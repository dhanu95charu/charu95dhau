import pandas as pd
import numpy as np

dict={'id':[123,124,125,126,127],
      'name':['abhi','dhabu','charu','dolly','chandu'],
      'dept':['cs','ec','ce','cs','cs'],
      'gender':['m','f','m','f','m'],
      'salary':[1200,24000,250000,100000,1000]}

data=pd.DataFrame(dict)
print(data)
info=data[data['gender']=='m']
a=info[info['dept']=='cs']
print(a)
info=data[data['gender']=='f']
b=info[info['dept']=='ec']
print(b)

