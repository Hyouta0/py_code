#write a program to find factorial of a number

def fac(num):
    if(num < 1):
        return 1
    return num*fac(num-1)
print(fac(5))