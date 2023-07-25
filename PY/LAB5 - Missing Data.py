import numpy as np
import pandas as pd

#amissing data

df = pd.DataFrame({'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]})
print(df)

print(df.dropna())

print(df.dropna(axis=1))

print(df.dropna(thresh=2))

print(df.fillna(value='FILL VALUE'))

print(df['A'].fillna(value=df['A'].mean()))

print(df['B'].fillna(value=df['B'].mean()))

print(df['C'].fillna(value=df['C'].mean()))
