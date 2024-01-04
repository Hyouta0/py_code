num = input("Enter your number").strip().replace(" ","");
if len(num) == 1:
    print("1's");
elif len(num) == 2:
    print("ten");
elif len(num) == 3:
    print("hundred");
elif len(num) == 4:
    print("thousand");
else :
    print("number is above thousand");
