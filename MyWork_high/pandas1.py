
import pandas as pd 

df1 = pd.DataFrame([[1,3,4],[6,7,8]])
print(df1)
df2 = pd.DataFrame([[1,2,3],[4,5,6]],\
                   columns=['one','two','three'])
print(df2)

path = r'~/code/py_code/MyWork_high/EmpData.csv'

#data = pd.read_csv(path,index_col=0)
data = pd.read_csv(path)
print(data)
print(data.index)
print(data.columns)
print(type(data))
