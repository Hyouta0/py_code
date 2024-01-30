#get a number from user andcheck number of occurance of a single digit in that number. (for example . Num = 7888, check number of occurances of digit 8 in number)

num = int(input("Enter your number : "));
digit = int(input("Enter digit to search in number : "));
cnt =0;
while num > 0:
    tmp = num%10;
    num = num//10;
    if tmp == digit:
        cnt+=1;

print("digit :",digit ,"came " ,cnt," times in number : ",num);

