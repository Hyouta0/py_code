#write a function to find factors of a number and add them in list
'''
def factors(num,numList):
    if(num == 1):
        numList.append(1);
        return;

    if(num%2 == 0):
        numList.append(2);
        factors(int(num/2),numList);
    elif(num%3 == 0):
        numList.append(3);
        factors(int(num/3),numList);
    else:
        numList.append(5);
        factors(int(num/5),numList);

numList = [];
factors(50,numList);
print(numList);
'''
def factors(num):
    for i in range(1,num+1):
        if(num%i == 0):
            print(i);

factors(50);
