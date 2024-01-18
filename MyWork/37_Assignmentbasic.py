'''
Read product file and tran_dtl file and implement inner join using loops (use two for loops)
'''

productPath = r"../PythonWork/Data/product.csv"
tranPath = r"../PythonWork/Data/Retail_Data/tran_dtl_1_2019.csv"
#train id , product id ,quentity,price,data
#product_id,description,price,category,max_qty
#2020-04-15T19:57:01.671999_0,93  ,1,    5.99,   01-1-2019
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

print(innerJoin)

