# write a program to compute fibonaci number of given number(recurssion);
num = 10

def fibonaci(num):
    if(num <=1):
        return num
    return(fibonaci(num-1)+fibonaci(num-2))
for i in range(num):
    print(fibonaci(i))

