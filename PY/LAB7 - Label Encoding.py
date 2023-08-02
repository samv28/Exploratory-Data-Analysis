import pandas as pd
import numpy as no

#acreating initial dataframe

bridge_types = ('Arch','Bean','Truss','Cantilever','Tied Arch','Suspention','Cable')
bridge_df = pd.DataFrame(bridge_types,columns=['Bridge_Types'])
bridge_df['Bridge_Types'] = bridge_df['Bridge_Types'].astype('category')
bridge_df['Bridge_Types_Cat'] = bridge_df['Bridge_Types'].cat.codes
print(bridge_df)

#ausing skikit learn

from sklearn.preprocessing import LabelEncoder

bridge_types = ('Arch','Bean','Truss','Cantilever','Tied Arch','Suspention','Cable')
bridge_df = pd.DataFrame(bridge_types,columns=['Bridge_Types'])
labelencoder = LabelEncoder()
bridge_df['Bridge_Types_Cat'] = labelencoder.fit_transform(bridge_df['Bridge_Types'])
print(bridge_df)
