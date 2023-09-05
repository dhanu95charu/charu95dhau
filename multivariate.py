import pandas as pd
import numpy as np
import matplotlib.pyplot as p
import seaborn as sns
data= pd.read_csv("C:\/Users/SPTIT-22/Desktop/Iris.csv")
print(data)
sns.catplot(x='SepalLengthCm',hue='SepalWidthCm',col='Species',data=data,kind="count")
sns.catplot(x='PetalLengthCm',hue='SepalWidthCm',col='Species',data=data,kind="count")

