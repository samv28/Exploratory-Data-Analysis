import numpy as np
import pandas as pd
#create dataframe

df = pd.DataFrame({'team':['A','A','B','B','B','B','C','C'],
                   'points':[25,12,15,14,19,23,25,29]})

print(df)

#one hot encoding
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(handle_unknown='ignore')
encoder_df = pd.DataFrame(encoder.fit_transform(df[['team']]).toarray())
final_df = df.join(encoder_df)
print(final_df)