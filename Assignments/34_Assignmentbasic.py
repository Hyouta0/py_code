# Get a number from user and check number is twin prime number 

def prime(num):
    if num == 1 or num ==2 :
        return True;
    for i in range(2,int(num**0.5 + 1)):
        if num%i == 0:
            return False;

    return True;

num = int(input("Enter a num : "));
if prime(num):
    if prime(num+2):
        print("number is twin prime");
    else:
        print("number is not twin prime");
else:
    print("number is not prime number ");


