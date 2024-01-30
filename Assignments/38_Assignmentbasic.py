
'''
Read product file and tran_dtl file and implement inner join using loops (use two for loops)
-- implement left, right and full outer join
'''

productPath = r"../PythonWork/Data/product.csv"
tranPath = r"../PythonWork/Data/Retail_Data/tran_dtl_1_2019.csv"

productDict = {}
tranDict ={}

cnt = -1
for line in open(productPath):
    if(cnt == -1):
        cnt+=1
        continue
    pId,desc,price,category,max_qty = line.strip().split(",")
    pId = int(pId)
    productDict[pId] = [pId,desc,price,category,max_qty]

#print(productDict)

for line in open(tranPath):
    if(cnt == 0):
        cnt +=1
        continue
    tranid,pId,tran_price,tran_qty,date = line.strip().split(",")
    pId = int(pId)
    tranDict[pId] = [tranid,pId,tran_price,tran_qty,date]

innerJoin = []
for key,value in productDict.items():
    if(key in tranDict):
        line =value+tranDict[key]
        innerJoin.append(line)

#print(innerJoin)

leftOuterJoin = []
for key,value in productDict.items():
    if(key in tranDict):
        line = value+tranDict[key]
    else:
        line = value
    leftOuterJoin.append(line)

#print(leftOuterJoin)

rightOuterJoin = []
for key,value in tranDict.items():
    if(key in productDict):
        line = value+tranDict[key]
    else:
        line = value
    rightOuterJoin.append(line)

print(rightOuterJoin)

#fullOuterJoin = []

