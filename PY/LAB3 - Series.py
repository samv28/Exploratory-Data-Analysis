import numpy as np
import pandas as pd

#aseries

#acreating a series
labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'b':30,'c':30}
print(pd.Series(data=my_list))
print(pd.Series(data=my_list,index=labels))
print(pd.Series(my_list,labels))

#anumpy arrays
print(pd.Series(arr))
print(pd.Series(arr,labels))

#adictionary
print(pd.Series(d))

#adata in a series
print(pd.Series(data=labels))
print(pd.Series([sum,print,len]))

#ausing index
ser1 = pd.Series([1,2,3,4],index = ['USA','Germany','USSR','Japan'])
print(ser1)
ser2 = pd.Series([1,2,3,4],index = ['USA','Germany','Italy','Japan'])
print(ser2)

print(ser1['USA'])

print(ser1+ser2)
print(ser2+ser1)