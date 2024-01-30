# write a program to compute fibonaci number of given number(recurssion);
num = 10
'''
def fibo(num):
    result = []
    a,b =0,1
    while a<num:
        result.append(a)
        a,b=b,a+b
    return result
print(fibo(num))

#using recursion
result = []
def fibo(a,b,num,result):
    if a>num:
        return
    result.append(a)
    fibo(b,a+b,num,result)
fibo(0,1,10,result)
print(result)
'''
def fibo(num,result):
    if result == []:
        result = [0,1]
    if num < result[-1]:
        return result
    result.append(result[-1]+result[-2])
    return fibo(num,result)

print(fibo(10,[]))
