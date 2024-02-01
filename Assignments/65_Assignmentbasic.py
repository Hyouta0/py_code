'''
start with a hard coded list a = [3,4,5,86,34,2,3,4,7,33,44,66,88,34,32,11,22] 
and write a program (bubble sort) to sort the list in ascending order - bubble sort
'''
a = [3,4,5,86,34,2,3,4,7,33,44,66,88,34,32,11,22]

for i in range(len(a)):
    for j in range(len(a)-i):
        if(j== 0):
            continue
        if(a[j]<a[j-1]):
            tmp = a[j-1]
            a[j-1]=a[j]
            a[j]=tmp
print(a)
        
