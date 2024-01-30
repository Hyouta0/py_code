name = input("Enter your name");
addr = input("Enter your address");
age  = int(input("Enter your age"));
if age < 18:
    print(name,"you can't vote");
else:
    print(name, "you can vote at ",addr," polling booth");

