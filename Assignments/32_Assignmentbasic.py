
# ask user to pick any number between 0 and 100 and implement a guessing game program to identify number picked up by user. (use while loop)

num =[];
for i in range(10000):
    num.append(i);

#print("nums :",num);

idx = (len(num)-1)//2;

while(1):
    idx=(len(num)-1)//2;
    choise=input("type 'y' if your guess is "+str(num[idx])+" / type 'g' if your guess is greater than value / type 's' if your guess is smaller than value ");
    match choise:
        case 'y':
            print("i won ");
            break;
        case 's':
            num=num[0:idx];
        case 'g':
            num=num[idx+1:];


