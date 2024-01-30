#write a program to compute factorial of a number using function

def factorial(num):
    if(num == 1):
        return 1;
    return num*factorial(num-1);

print(factorial(4));
