'''
You are given two positive integers
1. Height of ladder and
2. Max number of steps  you can take at a time to reach the top.
Write a program to list all possible ways in which one can reach to the top of the ladder.
'''
hgt = 9
max_steps = 3
lst = [0]* hgt
comboLst = []
print(lst)

def ladder(hgt,max_steps,lvl,lst,comboLst):
    if(hgt == 0):
        print(f"Possible way : {lst[:lvl]}")
        comboLst.append(lst[:lvl])
        return
    for i in range(1,min(max_steps+1,hgt+1)):
        lst[lvl] = i 
        ladder(hgt - i,max_steps,lvl+1,lst,comboLst)

ladder(hgt,max_steps,0,lst,comboLst)
print(comboLst)

