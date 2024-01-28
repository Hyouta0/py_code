import pandas as pd 

print("+++++++++++Pandas with list+++++++++++++++++++++++++")
#pandas using list of list
df = pd.DataFrame([[1,2,3],[4,5,6]])
print(df)

#pandas using list whith column name 
df = pd.DataFrame([[1,2,3],[4,5,6]],columns=["one","two","three"])
print(df)

#pandas using list with column and index names 
df = pd.DataFrame([[1,2,3],[4,5,6]],\
                  columns=["one","two","three"],\
                  index = ["High","Low"])
print(df)

#pandas using list whith custome column name and index
columnName = ["Height","Weight","Age"]
indexName  = ["one","two"]
df = pd.DataFrame([[5.5,54,22],[6.0,80,23]])
df.columns = columnName
df.index = indexName
print(df)
print("printing index : ",df.index)

print("+++++++++++++++Pandas with Dict++++++++++++++++++++++")
df1 = pd.DataFrame([{"name":"kiran","surname":"biradar"},\
                    {"name":"nishad","age":23},\
                    {"name":"abhi","height":5.5}])
print(df1)
print("Header name : ",df1.columns)
print("Index of data : ",df1.index)
print("Value in dict :\n",df1.values)



