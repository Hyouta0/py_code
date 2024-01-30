import pandas as pd

path = r'./hwaData.csv'
df = pd.read_csv(path,\
                 names=['Count','Name','Height','Weight','Age'],skiprows=[0])

#print(df[df['Age'] < 41].describe())

df1 = df[df['Age'] == 40]

print(df1)

