import pandas as pd
import numpy as np

#adataframes

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
print(df)

DF = pd.DataFrame(randn(4,3),index='A B C D'.split(),columns='a b c'.split())
print(DF)

print(df['W'])

print(df['Z'])

print(df[['W','Z','X']])

print(df.W)

print(type(df['W']))
df['new'] = df['W'] + df['Y']

print(df)

#adroping col
df.drop('new',axis=1,inplace=True)
print(df)

#adroping row

#adf.drop('E',axis=0,inplace=True)
print(df)

#aselecting row
print(df.loc['A']) 

#aselecting through index
print(df.iloc[2])

print(df.loc['B','Y'])

print(df.loc[['A','B'],['W','Y']])

#aconditional selectiona
print(df)
print(df>0)

print(df[df["W"]>0])

print(df[df['W']>0]['Y'])

print(df[df['W']>0][['Y','X']])

#a or and and
print(df[(df['W']>0) & (df['Y']>1)])

print(df)

print(df.reset_index())

newind = 'CA NY WY OR CO'.split()

df['States'] = newind

print(df)

print(df.set_index('States'))

print(df)

df.set_index('States',inplace=True)

print(df)

#amulti index and index hierarchy

#aindex lbl
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

print(hier_index)

df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
print(df)

print(df.loc['G1'].loc[1])
print(df.index.names)

df.index.names = ['Group','Num']
print(df)

print(df.xs('G1'))
print(df.xs(('G1',1)))