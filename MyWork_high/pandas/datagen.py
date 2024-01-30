import os
import pandas as pd
import random

pathR = os.path.expanduser(r'~/DataAnalytic/Dataset-Indian-Names-master/Indian_Names.csv')
df = pd.read_csv(pathR)
df.columns = ["No","Names"]
dataList =[]

for i in df['Names']:
    dataList.append([i,round(random.uniform(5.0,7.0),2),round(random.uniform(50,90),2),random.randint(20,60)])

newData = pd.DataFrame(dataList,columns=['Name','Height','Weight','Age'])
newData.to_csv(r'./hwaData.csv')
print("Done")

