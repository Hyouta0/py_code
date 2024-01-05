#get a number from user and check if the number is perfect square 
num = int(input("Enter your number : "));

if num == (int(num**0.5) * int(num**0.5)):
    print( True);
else :
    print( False);
