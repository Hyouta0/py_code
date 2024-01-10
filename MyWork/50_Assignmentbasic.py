# write a program to compute fibonaci number of given number(recurssion);

# 1,2,3,5;

num1 =1;
num2 =1;

cnt =0;
while(cnt <4):
    cnt+=1;
    tmp = num2;
    num2 =num1;
    num1 = tmp+num2;
print(num2);
