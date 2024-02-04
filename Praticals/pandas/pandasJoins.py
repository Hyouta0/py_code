'''
read ./continentReln.csv and ./countrydataReln.csv in data frame ans joine them using inner join, left join , right join ,outer-join
'''
import pandas as pd
import os

contRelnPath =os.path.expanduser(r'~/code/py_code/Praticals/pandas/continentReln.csv')
coutRelnPath = os.path.expanduser(r'~/code/py_code/Praticals/pandas/countrydataReln.csv')

contReln = pd.read_csv(contRelnPath)
coutReln  = pd.read_csv(coutRelnPath)

#print header 
print(contReln.columns)
print(coutReln.columns)

# inner join 
innerJoin = pd.merge(coutReln,contReln, on ="continent_id", how ='inner')
#print(innerJoin)

#left join 
leftJoin = pd.merge(coutReln,contReln, on ="continent_id", how ='left')
print(leftJoin)

#right join 
rightJoin = pd.merge(coutReln,contReln, on ="continent_id", how ='right')
print(leftJoin)

#outer join 
outerJoin = pd.merge(coutReln,contReln, on ="continent_id", how ='outer')
print(outerJoin)
