
num = 5;
numList= [1,2,3,4,5];

print("value of num before function : ",num);
print("value of numList before function : ",numList);

def myfun(num,numList):
    num+=1;
    numList[2]=10;
    print("value of num in function : ",num);
    print("Value of numList in function : ",numList);
myfun(num,numList);
print("value of num after function : ",num);
print("value of numList after function : ",numList);
