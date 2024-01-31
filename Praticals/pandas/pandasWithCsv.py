import pandas as pd
import numpy as np

path = r'./hwaData.csv'
df = pd.read_csv(path,\
                 names=['Count','Name','Height','Weight','Age'],skiprows=[0])

#Slicing by columns
print(df.Name)
print(df['Age'])
print(df[['Name','Age','Weight','Height']])
#slicing row by index location
print(df.iloc[2,3])#second row thired column 
print("printing row : \n",df.iloc[2,])#second row
print("printing colun: \n",df.iloc[:,2])#print all second colunm
print(df.iloc[2:7])#print rows from 2 to 6
print(df.loc[1:7])#print start from 1 not 0 both inclusive
print(df.iloc[3:5,[1,3]])#print row 3 to 4 (1 and 2 col)
print(df.loc[3:5,['Name']])# print row 3 to 4 & name col

#filtering 
print(df[df.Age < 40])
print(df[df['Age'].isin([34,35,36])])

#assigning vales
df2 = df
df2.loc[2,'Age'] = np.NaN
print("ffilling data : \n",df2.Age.fillna(method='ffill'))
print("bfilling data : \n",df2.Age.fillna(method='bfill'))
df2.Age.fillna(value=df2.Age.median(),inplace =True)
print(df2)
#print(df2)


