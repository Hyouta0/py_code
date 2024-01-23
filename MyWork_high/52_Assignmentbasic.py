'''
You are given two positive integers
1. Height of ladder and
2. Max number of steps  you can take at a time to reach the top.
Write a program to list all possible ways in which one can reach to the top of the ladder.
hgt = 3
max = 3
myList = []
for i in range(hgt):
    myList.append(0)
print(myList)

def ladder(hgt,max,lvl,list):
    if(hgt <= 0):
        lst = []
        for i in range(lvl):
            lst.append(list[i])
        print(f"last at list : {lst} level:{lvl} ")
        return
    for i in range(1,hgt+1):
        myList[lvl] = i
        hgt = hgt - i 
        ladder(hgt,max,lvl+1,list)

ladder(hgt,max,0,myList)
'''
def ladder(hgt, max_steps, lvl, lst):
    if hgt <= 0:
        print(f"Possible way: {lst[:lvl]}")
        return
    
    for i in range(1, min(max_steps, hgt) + 1):
        lst[lvl] = i
        ladder(hgt - i, max_steps, lvl + 1, lst)

hgt = 3
max_steps = 3
myList = [0] * hgt

ladder(hgt, max_steps, 0, myList)
