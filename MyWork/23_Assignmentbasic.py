
#print(input("Enter the number : ")[::-1])


num = int(input("Enter your number"));
rev_num = 0;

while(num !=0):
    digit = num%10;
    rev_num = rev_num *10+digit;
    num //=10;

print(rev_num);

