
num = int(input("Enter number : "));
flage = False;

for i in range(2,num/2+1):
    if(num%i == 0):
        print("is not prime");
    else: 
        print("is prime");

