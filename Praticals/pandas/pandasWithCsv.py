import pandas as pd

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





