'''
You are given two positive integers
1. Height of ladder and
2. Max number of steps  you can take at a time to reach the top.
Write a program to list all possible ways in which one can reach to the top of the ladder.
'''

def ladder(hgt,max,list):
    if(hgt == 0):
        return
    for i in range(max , 1,-1):
        if(hgt>max):
            ladder(hgt,i)
