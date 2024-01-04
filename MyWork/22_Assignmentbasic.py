
# !5 == 5*4*3*2*1
num = int(input("Enter the number"));
ans = 1;
while(num > 0):
    ans = ans * num;
    num-=1;

print("ans: ",ans);

