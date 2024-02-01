'''
get a list a = [2,3,4,55,33,4,55,343,66,77,88,99] 
and write a program to find list of non adjacent numbers of every number.
'''
a = [2,3,4,55,33,4,55,343,66,77,88,99]
nonAdjacent = {}

for i in range(len(a)):
    for j in range(len(a)):
        if(j == i-1 or j==i or j== i+1):
            continue
        if(a[i] not in nonAdjacent):
            nonAdjacent[a[i]]=[a[j]]
        else:
            nonAdjacent[a[i]].append(a[j])
print(nonAdjacent)
