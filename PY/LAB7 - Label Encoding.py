import pandas as pd
import numpy as no

#creating initial dataframe

bridge_types = ('Arch','Bean','Truss','Cantilever','Tied Arch','Suspention','Cable')
bridge_df = pd.DataFrame(bridge_types,columns=['Bridge_Types'])

bridge_df['Bridge_Types'] = bridge_df['Bridge_Types'].astype('category')

bridge_df['Bridge_Types_Cat'] = bridge_df['Bridge_Types'].cat.codes

print(bridge_df)