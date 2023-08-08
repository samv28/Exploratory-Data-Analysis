import pandas as pd
import numpy as np
stats = pd.read_csv('D:/SIT/EDAL/Datasets/DemographicData.csv.csv')
print(stats)

print(len(stats))


print(stats.shape)


print(stats.columns)


print(len(stats.columns))


print(stats.head())

#7 Informaton of the columns
print(stats.info())

#8 Get stats on the columns
print(stats.describe().transpose())

print(stats.columns)

stats.columns = ['CountryName', 'CountryCode', 'Birthrate', 'Internetusers','IncomeGroup']

print(stats.head()
      )
#subsetting row

#starting at index 185
print(stats[185:])

print(stats[100:110])

#reverse
print(stats[::-1])

#only 20th row
print(stats[::20])

#subsetting colums

print(stats.columns)

#subset 1 col
print(stats['CountryName'].head())

#subset multiple col
print(stats[['CountryName','Birthrate']].head())

#can specify col
print(stats[['Birthrate','CountryName']].head())

print(stats.Birthrate.head())

#combining the two
print(stats[4:8][['CountryName','Birthrate']])

print(stats[['CountryName','Birthrate']][4:8])

#Mathematical operations
result = stats.Birthrate * stats.Internetusers
print(result.head())

#add col
stats['MyCalc'] = result
print(stats.head())

#removing cal
stats = stats.drop('MyCalc',axis=1)
print(stats.head())

#filtering
Filter = stats['Internetusers']<2
print(Filter)
print(stats[Filter])

#filter by birthrate
Filter2 = stats.Birthrate>40
print(stats[Filter2])

print(stats[stats.Birthrate>40])

#applying 2 filters
print(stats[Filter & Filter2])

#apply 2 filer without filters
print(stats[(stats.Birthrate>40)&(stats.Internetusers<2)])

#filter for high incomegroup
print(stats[stats.IncomeGroup=='High income'])

#unique entrys
print(stats['IncomeGroup'].unique())

print(stats.CountryName.unique())

#findeverything about malta
print(stats[stats.CountryName=='Malta'])

#accesing individual elements

#access by integer location
print(stats.iat[3,4])

#acces by label
print(stats.at[2,'Birthrate'])