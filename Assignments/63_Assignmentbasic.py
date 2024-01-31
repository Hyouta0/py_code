'''
write a function to get maximum element of list 
and second highest element in a list
'''

def twoHigest(numList):
    max =0
    sec =0
    for i in numList:
        if(max < i):
            sec = max
            max = i
    return {'higest': max , 'secHigest': sec}
print(twoHigest([4,5,3,2,6,0]))
