
import pandas as pd 

print("+++++++++++list+++++++++++++++++++++++++++++")
df1 = pd.DataFrame([[1,3,4],[6,7,8]])
print(df1)
df2 = pd.DataFrame([[1,2,3],[4,5,6]],\
                   columns=['one','two','three'])
print(df2)

print("+++++++++++++dictionary+++++++++++++++++++++++++")

df3 = pd.DataFrame([{"name":"krain","age":23,"height":6.2},\
                    {"name":"nishad","surname":"deshpande","age":23},\
                    {"name":"abhi","salary":25000}
                    ])
print(df3)

print("++++++++++++file+++++++++++++++++++++++++++++++")

path = r'~/code/py_code/MyWork_high/EmpData.csv'

#data = pd.read_csv(path,index_col=0)
data = pd.read_csv(path)
print(data.head(10))
