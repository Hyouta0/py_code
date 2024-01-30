
a = [2,3,4,55,33,4,55,343,66,77,88,99];

for i in range(len(a)):
    if i == 0:
        print("previse number is null","and current number is : ",a[i]);
    else:
        print("previous number is : ", a[i-1]," and current number is : ",a[i]);
