'''
You are given two positive integers
1. Height of ladder and
2. Max number of steps  you can take at a time to reach the top.
Write a program to list all possible ways in which one can reach to the top of the ladder.
'''
hgt = 3
list = [0,0,0,0,0,0,0,0,0,0]
max =4
combList=[]
def ladder(hgt,max,list,combList,lvl):
    if(hgt == 0):
        lst = []
        for i in range(lvl):
            lst.append(list[i])
        combList.append(lst)
        return
    else:
        for i in range(hgt):
            i+=1
            step = i
            list[lvl] = step
            hgt = hgt-step
            ladder(hgt,max,list,combList,lvl+1)

ladder(hgt,max,list,combList,0)
print(combList)

