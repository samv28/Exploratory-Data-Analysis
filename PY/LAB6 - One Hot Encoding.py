import numpy as np
import pandas as pd

#acreate dataframe

df = pd.DataFrame({'team':['A','A','B','B','B','B','C','C'],
                   'points':[25,12,15,14,19,23,25,29]})
print(df)

#aone hot encoding

from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(handle_unknown='ignore')
encoder_df = pd.DataFrame(encoder.fit_transform(df[['team']]).toarray())
final_df = df.join(encoder_df)
print(final_df)

df1 = pd.DataFrame({'Gender':['M','M','F','M','F','F','M','F','M','F'],
                   'Degree':['BCOM','BTECH','BCA','BTECH','BCOM','BTECH','BCA','BCOM','BCA','BTECH'],
                   'Age':[24,25,24,25,30,38,23,29,29,21]})

gencoder = OneHotEncoder(handle_unknown='ignore')
gencoder_df = pd.DataFrame(encoder.fit_transform(df1[['Gender','Degree']]).toarray())
final_df1 = df1.join(gencoder_df)
print(final_df1)

bridge_types = ('Arch','Bean','Truss','Cantilever','Tied Arch','Suspention','Cable')
bridge_df = pd.DataFrame(bridge_types,columns=['Bridge_Types'])
enc = OneHotEncoder(handle_unknown='ignore')
enc_df = pd.DataFrame(enc.fit_transform(bridge_df[['Bridge_Types']]).toarray())
bridge_df = bridge_df.join(enc_df)
print(bridge_df)